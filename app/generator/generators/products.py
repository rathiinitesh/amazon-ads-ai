import random
import string
from datetime import date, timedelta

from sqlalchemy import select

from app.db.models import Brand
from app.db.models import Product
from app.db.models import ProductCategory


PRODUCT_CATALOG = {
    "Apple": {
        "Mobile Phones": [
            ("iPhone 16", 79999),
            ("iPhone 16 Plus", 89999),
            ("iPhone 16 Pro", 119999),
            ("iPhone 16 Pro Max", 139999),
        ],
        "Tablets": [
            ("iPad Air", 59999),
            ("iPad Pro", 99999),
        ],
        "Headphones": [
            ("AirPods Pro", 24999),
            ("AirPods Max", 59999),
        ],
    },
    "Samsung": {
        "Mobile Phones": [
            ("Galaxy S25", 74999),
            ("Galaxy S25 Ultra", 124999),
            ("Galaxy Z Fold", 164999),
        ],
        "Smart Watches": [
            ("Galaxy Watch 8", 32999),
        ],
    },
    "Sony": {
        "Headphones": [
            ("WH-1000XM6", 29999),
            ("WF-1000XM6", 19999),
        ]
    },
    "boAt": {
        "Headphones": [
            ("Airdopes 311", 1999),
            ("Airdopes 141", 1499),
            ("Rockerz 550", 2499),
        ]
    },
    "Dell": {
        "Laptops": [
            ("Inspiron 15 Ryzen 7", 69999),
            ("XPS 13", 139999),
        ]
    },
}


def generate_asin():
    return "B0" + "".join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=8,
        )
    )


def generate_sku(brand, product_name):
    return (brand[:3].upper() + "-" + product_name.replace(" ", "-").upper())[:30]


def generate_products(session):
    existing = {sku for (sku,) in session.execute(select(Product.sku))}

    brands = {b.brand_name: b for b in session.scalars(select(Brand))}

    categories = {c.category_name: c for c in session.scalars(select(ProductCategory))}

    inserted = 0

    for brand_name, category_map in PRODUCT_CATALOG.items():
        brand = brands.get(brand_name)

        if not brand:
            continue

        for category_name, products in category_map.items():
            category = categories.get(category_name)

            if not category:
                continue

            for product_name, price in products:
                sku = generate_sku(
                    brand_name,
                    product_name,
                )

                if sku in existing:
                    continue

                session.add(
                    Product(
                        asin=generate_asin(),
                        sku=sku,
                        product_name=f"{brand_name} {product_name}",
                        brand_id=brand.brand_id,
                        category_id=category.category_id,
                        price=price,
                        launch_date=date.today()
                        - timedelta(
                            days=random.randint(
                                100,
                                1200,
                            )
                        ),
                        is_active=True,
                    )
                )

                inserted += 1

    session.commit()

    print(f"Inserted {inserted} products")
