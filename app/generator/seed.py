from app.db.session import SessionLocal
from app.generator.generators import (
    generate_brands,
    generate_campaign_daily_metrics,
    generate_campaigns,
    generate_marketplaces,
    generate_portfolios,
    generate_product_categories,
    generate_products,
)


def main():
    session = SessionLocal()

    try:
        print("Starting data generation...")

        generate_marketplaces(session)
        generate_brands(session)
        generate_product_categories(session)
        generate_portfolios(session)
        generate_products(session)
        generate_campaigns(session)
        generate_campaign_daily_metrics(session)

        session.commit()
        print("Done.")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()
