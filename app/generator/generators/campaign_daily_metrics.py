import random
from datetime import date, datetime, timedelta

from sqlalchemy import select

from app.db.models import Campaign, CampaignDailyMetrics


def generate_impressions():
    return random.randint(1000, 25000)


def generate_ctr():
    return random.uniform(0.005, 0.08)


def generate_clicks(impressions, ctr):
    return max(1, int(impressions * ctr))


def generate_cpc():
    return round(random.uniform(5, 80), 2)


def generate_spend(clicks, cpc):
    return round(clicks * cpc, 2)


def generate_conversion_rate():
    return random.uniform(0.03, 0.25)


def generate_orders(clicks, conversion_rate):
    return max(0, int(clicks * conversion_rate))


def generate_units_sold(orders):
    if orders == 0:
        return 0

    return orders + random.randint(0, max(1, orders // 2))


def generate_sales(product, units_sold):
    if units_sold == 0:
        return 0

    sales = product.price * units_sold
    sales *= random.uniform(0.95, 1.05)

    return round(sales, 2)


def generate_orders_windows(orders):
    orders_7d = orders
    orders_14d = orders_7d + random.randint(0, 3)
    orders_30d = orders_14d + random.randint(0, 5)

    return (
        orders_7d,
        orders_14d,
        orders_30d,
    )


def generate_sales_windows(sales):
    sales_7d = sales

    sales_14d = round(
        sales_7d + random.uniform(0, sales * 0.10),
        2,
    )

    sales_30d = round(
        sales_14d + random.uniform(0, sales * 0.15),
        2,
    )

    return (
        sales_7d,
        sales_14d,
        sales_30d,
    )


def generate_new_to_brand(orders, sales):
    if orders == 0:
        return (
            0,
            0,
            0,
        )

    ntb_orders = int(orders * random.uniform(0.10, 0.40))

    if orders == 0:
        ntb_sales = 0
    else:
        ntb_sales = round(
            sales * (ntb_orders / orders),
            2,
        )

    percentage = round((ntb_sales / sales) * 100, 2) if sales else 0

    return (
        ntb_orders,
        ntb_sales,
        percentage,
    )


def calculate_metrics(
    impressions,
    clicks,
    spend,
    orders,
    sales,
):
    ctr = round(clicks / impressions, 4) if impressions else 0

    cpc = round(spend / clicks, 2) if clicks else 0

    cpm = round((spend / impressions) * 1000, 2) if impressions else 0

    conversion_rate = round(orders / clicks, 4) if clicks else 0

    aov = round(sales / orders, 2) if orders else 0

    acos = round(spend / sales, 4) if sales else 0

    roas = round(sales / spend, 2) if spend else 0

    roi = round((sales - spend) / spend, 2) if spend else 0

    return (
        ctr,
        cpc,
        cpm,
        conversion_rate,
        aov,
        acos,
        roas,
        roi,
    )


def generate_campaign_daily_metrics(session):
    print("Generating campaign daily metrics...")

    existing = {
        (campaign_id, report_date)
        for campaign_id, report_date in session.execute(
            select(
                CampaignDailyMetrics.campaign_id,
                CampaignDailyMetrics.report_date,
            )
        )
    }

    campaigns = session.scalars(select(Campaign)).all()

    today = date.today()

    inserted = 0

    for campaign in campaigns:
        current_date = campaign.start_date

        end_date = min(
            campaign.end_date,
            today,
        )

        while current_date <= end_date:
            key = (
                campaign.campaign_id,
                current_date,
            )

            if key in existing:
                current_date += timedelta(days=1)
                continue

            impressions = generate_impressions()

            ctr_seed = generate_ctr()

            clicks = generate_clicks(
                impressions,
                ctr_seed,
            )

            cpc_seed = generate_cpc()

            spend = generate_spend(
                clicks,
                cpc_seed,
            )

            conversion_seed = generate_conversion_rate()

            orders = generate_orders(
                clicks,
                conversion_seed,
            )

            units_sold = generate_units_sold(
                orders,
            )

            sales = generate_sales(
                campaign.product,
                units_sold,
            )

            (
                orders_7d,
                orders_14d,
                orders_30d,
            ) = generate_orders_windows(
                orders,
            )

            (
                sales_7d,
                sales_14d,
                sales_30d,
            ) = generate_sales_windows(
                sales,
            )

            (
                ntb_orders,
                ntb_sales,
                ntb_percentage,
            ) = generate_new_to_brand(
                orders,
                sales,
            )

            (
                ctr,
                cpc,
                cpm,
                conversion_rate,
                aov,
                acos,
                roas,
                roi,
            ) = calculate_metrics(
                impressions,
                clicks,
                spend,
                orders,
                sales,
            )

            session.add(
                CampaignDailyMetrics(
                    campaign_id=campaign.campaign_id,
                    report_date=current_date,
                    impressions=impressions,
                    clicks=clicks,
                    spend=spend,
                    orders=orders,
                    orders_7d=orders_7d,
                    orders_14d=orders_14d,
                    orders_30d=orders_30d,
                    units_sold=units_sold,
                    sales=sales,
                    sales_7d=sales_7d,
                    sales_14d=sales_14d,
                    sales_30d=sales_30d,
                    new_to_brand_orders=ntb_orders,
                    new_to_brand_sales=ntb_sales,
                    new_to_brand_sales_percentage=ntb_percentage,
                    cpc=cpc,
                    cpm=cpm,
                    ctr=ctr,
                    conversion_rate=conversion_rate,
                    aov=aov,
                    acos=acos,
                    roas=roas,
                    roi=roi,
                    created_at=datetime.now(),
                )
            )

            inserted += 1
            current_date += timedelta(days=1)

    session.commit()

    print(f"Inserted {inserted} campaign daily metrics.")
