from sqlalchemy import select
from datetime import date

from app.db.models import Portfolio

PORTFOLIOS = [
    ("Consumer Electronics", "Electronics", "Rahul Sharma"),
    ("Home & Kitchen", "Home", "Priya Mehta"),
    ("Beauty & Personal Care", "Beauty", "Ananya Gupta"),
    ("Fashion", "Apparel", "Vikram Singh"),
    ("Sports & Outdoors", "Sports", "Karan Verma"),
    ("Pet Supplies", "Pet Care", "Neha Kapoor"),
    ("Grocery & Gourmet", "Grocery", "Arjun Nair"),
    ("Office Essentials", "Office", "Sneha Iyer"),
    ("Automotive", "Automotive", "Rohit Malhotra"),
    ("Seasonal Promotions", "Marketing", "Aditi Rao"),
    ("Clearance Campaigns", "Marketing", "Mohit Bansal"),
    ("New Product Launches", "Marketing", "Simran Kaur"),
]


def generate_portfolios(session):
    existing = {
        name for (name,) in session.execute(select(Portfolio.portfolio_name)).all()
    }

    inserted = 0

    for portfolio_name, department, manager in PORTFOLIOS:
        if portfolio_name in existing:
            continue

        session.add(
            Portfolio(
                portfolio_name=portfolio_name,
                department=department,
                manager_name=manager,
                created_at=date(2024, 1, 1),
            )
        )

        inserted += 1

    session.commit()

    print(f"Inserted {inserted} portfolios")
