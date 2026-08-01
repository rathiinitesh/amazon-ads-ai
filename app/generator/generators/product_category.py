from sqlalchemy import select

from app.db.models import ProductCategory


CATEGORIES = {
    "Electronics": [
        "Mobile Phones",
        "Laptops",
        "Tablets",
        "Headphones",
        "Smart Watches",
    ],
    "Home & Kitchen": [
        "Cookware",
        "Furniture",
        "Storage",
        "Home Decor",
    ],
    "Beauty": [
        "Skin Care",
        "Hair Care",
        "Makeup",
        "Personal Care",
    ],
    "Sports": [
        "Fitness Equipment",
        "Outdoor",
        "Cycling",
    ],
    "Fashion": [
        "Men",
        "Women",
        "Kids",
    ],
    "Pet Supplies": [
        "Dog",
        "Cat",
    ],
    "Office Products": [
        "Office Supplies",
        "Printers",
    ],
    "Grocery": [
        "Coffee",
        "Snacks",
        "Beverages",
    ],
}


def generate_product_categories(session):
    category_lookup = {}
    for category_name in CATEGORIES.keys():
        category = session.scalar(
            select(ProductCategory).where(
                ProductCategory.category_name == category_name,
                ProductCategory.parent_category_id.is_(None),
            )
        )

        if category is None:
            category = ProductCategory(
                category_name=category_name,
            )

            session.add(category)
            session.flush()

        category_lookup[category_name] = category

    for parent_name, subcategories in CATEGORIES.items():
        parent = category_lookup[parent_name]

        for subcategory in subcategories:
            exists = session.scalar(
                select(ProductCategory).where(
                    ProductCategory.category_name == subcategory,
                    ProductCategory.parent_category_id == parent.category_id,
                )
            )

            if exists:
                continue

            session.add(
                ProductCategory(
                    category_name=subcategory,
                    parent_category_id=parent.category_id,
                )
            )
    session.commit()
