from sqlalchemy import select

from app.db.models.marketplace import Marketplace
from app.generator.config import GeneratorConfig


def generate_marketplaces(session):
    """
    Seed the marketplaces table.
    This function is idempotent—running it multiple times
    won't insert duplicate marketplaces.
    """

    existing_codes = {
        code for (code,) in session.execute(select(Marketplace.marketplace_code)).all()
    }

    marketplaces_to_create = []

    for code, name, currency in GeneratorConfig.MARKETPLACES:
        if code in existing_codes:
            continue

        marketplaces_to_create.append(
            Marketplace(
                marketplace_code=code,
                marketplace_name=name,
                currency=currency,
            )
        )

    if marketplaces_to_create:
        session.add_all(marketplaces_to_create)

    print(f"Inserted {len(marketplaces_to_create)} marketplaces")
