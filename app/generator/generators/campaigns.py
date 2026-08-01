import random
from datetime import timedelta

from sqlalchemy import select

from app.db.models import (
    Campaign,
    Product,
    Marketplace,
    Portfolio,
)

from app.db.models.enum_models import (
    BiddingStrategy,
    CampaignGoal,
    CampaignState,
    CampaignType,
    MatchType,
    OptimizationStrategy,
    Placement,
    Priority,
    TargetingType,
)


CAMPAIGN_TEMPLATES = [
    (
        CampaignType.SPONSORED_PRODUCTS,
        TargetingType.AUTO,
        None,
        "SP",
        "Auto",
    ),
    (
        CampaignType.SPONSORED_PRODUCTS,
        TargetingType.MANUAL,
        MatchType.BROAD,
        "SP",
        "Broad",
    ),
    (
        CampaignType.SPONSORED_PRODUCTS,
        TargetingType.MANUAL,
        MatchType.PHRASE,
        "SP",
        "Phrase",
    ),
    (
        CampaignType.SPONSORED_PRODUCTS,
        TargetingType.MANUAL,
        MatchType.EXACT,
        "SP",
        "Exact",
    ),
    (
        CampaignType.SPONSORED_BRANDS,
        TargetingType.MANUAL,
        MatchType.EXACT,
        "SB",
        "Brand",
    ),
    (
        CampaignType.SPONSORED_DISPLAY,
        TargetingType.MANUAL,
        MatchType.PRODUCT_TARGETING,
        "SD",
        "Remarketing",
    ),
]

PORTFOLIO_MAPPING = {
    "Electronics": "Consumer Electronics",
    "Home & Kitchen": "Home & Kitchen",
    "Beauty": "Beauty & Personal Care",
    "Fashion": "Fashion",
    "Sports": "Sports & Outdoors",
    "Pet Supplies": "Pet Supplies",
    "Office Products": "Office Essentials",
    "Grocery": "Grocery & Gourmet",
}


def random_campaign_state():
    return random.choices(
        [
            CampaignState.ENABLED,
            CampaignState.PAUSED,
            CampaignState.ARCHIVED,
        ],
        weights=[80, 15, 5],
        k=1,
    )[0]


def random_budget():
    return random.choice(
        [
            500,
            750,
            1000,
            1500,
            2000,
            2500,
            5000,
            10000,
        ]
    )


def random_bidding_strategy():
    return random.choices(
        [
            BiddingStrategy.DYNAMIC_DOWN,
            BiddingStrategy.DYNAMIC_UP_AND_DOWN,
            BiddingStrategy.FIXED_BIDS,
        ],
        weights=[60, 30, 10],
        k=1,
    )[0]


def random_priority():
    return random.choice(
        [
            Priority.LOW,
            Priority.MEDIUM,
            Priority.HIGH,
        ]
    )


def random_placement():
    return random.choice(
        [
            Placement.TOP_OF_SEARCH,
            Placement.PRODUCT_PAGES,
            Placement.REST_OF_SEARCH,
        ]
    )


def random_optimization_strategy():
    return random.choice(
        [
            OptimizationStrategy.MAXIMISE_CLICKS,
            OptimizationStrategy.MAXIMISE_CONVERSIONS,
            OptimizationStrategy.TARGET_ACOS,
            OptimizationStrategy.TARGET_ROAS,
        ]
    )


def get_campaign_goal(campaign_type):
    if campaign_type == CampaignType.SPONSORED_PRODUCTS:
        return CampaignGoal.SALES

    if campaign_type == CampaignType.SPONSORED_BRANDS:
        return CampaignGoal.BRAND_AWARENESS

    return CampaignGoal.PRODUCT_LAUNCH


def build_campaign_name(product_name, prefix, suffix):
    return f"{prefix} | {product_name} | {suffix}"


def get_portfolio(product, portfolio_lookup):
    category = product.category

    if category.parent_category is not None:
        category_name = category.parent_category.category_name
    else:
        category_name = category.category_name

    portfolio_name = PORTFOLIO_MAPPING.get(category_name)

    if portfolio_name is None:
        raise ValueError(f"No portfolio mapping found for '{category_name}'")

    return portfolio_lookup[portfolio_name]


def get_marketplace(marketplaces):
    return random.choices(
        marketplaces,
        weights=[70, 10, 5, 5, 3, 3, 2, 1, 1, 0.5],
        k=1,
    )[0]


def generate_campaigns(session):
    print("Generating campaigns...")

    products = session.scalars(select(Product)).all()

    marketplaces = session.scalars(select(Marketplace)).all()

    portfolios = session.scalars(select(Portfolio)).all()

    portfolio_lookup = {portfolio.portfolio_name: portfolio for portfolio in portfolios}

    existing_campaigns = {
        campaign_name
        for (campaign_name,) in session.execute(select(Campaign.campaign_name))
    }

    inserted = 0

    for product in products:
        portfolio = get_portfolio(
            product,
            portfolio_lookup,
        )

        marketplace = get_marketplace(
            marketplaces,
        )

        for (
            campaign_type,
            targeting_type,
            match_type,
            prefix,
            suffix,
        ) in CAMPAIGN_TEMPLATES:
            campaign_name = build_campaign_name(
                product.product_name,
                prefix,
                suffix,
            )

            if campaign_name in existing_campaigns:
                continue

            start_date = product.launch_date + timedelta(days=random.randint(0, 90))

            end_date = start_date + timedelta(days=random.randint(180, 730))

            campaign = Campaign(
                campaign_name=campaign_name,
                campaign_goal=get_campaign_goal(campaign_type),
                campaign_type=campaign_type,
                targeting_type=targeting_type,
                match_type=match_type,
                campaign_state=random_campaign_state(),
                marketplace_id=marketplace.marketplace_id,
                portfolio_id=portfolio.portfolio_id,
                product_id=product.product_id,
                daily_budget=random_budget(),
                bidding_strategy=random_bidding_strategy(),
                placement=random_placement(),
                optimization_strategy=random_optimization_strategy(),
                priority=random_priority(),
                start_date=start_date,
                end_date=end_date,
            )

            session.add(campaign)

            existing_campaigns.add(campaign_name)

            inserted += 1

    session.commit()

    print(f"Inserted {inserted} campaigns")
