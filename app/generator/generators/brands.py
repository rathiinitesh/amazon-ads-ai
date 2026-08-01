from sqlalchemy import select
from app.db.models import Brand

BRANDS = [
    "Samsung",
    "Apple",
    "Sony",
    "LG",
    "Philips",
    "Boat",
    "JBL",
    "Logitech",
    "Anker",
    "Dell",
    "HP",
    "Lenovo",
    "ASUS",
    "Nike",
    "Adidas",
    "Puma",
    "Levi's",
    "Under Armour",
    "Milton",
    "Cello",
    "Prestige",
    "Hawkins",
    "Wonderchef",
    "Borosil",
    "Nestle",
    "Kellogg's",
    "Nescafe",
    "Dove",
    "Nivea",
    "L'Oreal",
    "Maybelline",
    "Mamaearth",
    "Himalaya",
    "Colgate",
    "Dettol",
    "Whiskas",
    "Pedigree",
    "Dyson",
    "Amazon Basics",
    "Solimo",
    "Symbol",
    "EchoCraft",
    "UrbanNest",
    "PeakFit",
    "NovaHome",
    "PureGlow",
    "TechSphere",
    "SmartLiving",
    "EcoWare",
    "ZenKitchen",
]


def generate_brands(session):
    existing_brands = {
        brand_name for (brand_name,) in session.execute(select(Brand.brand_name)).all()
    }

    count = 0
    for brand_name in BRANDS:
        if brand_name in existing_brands:
            continue
        session.add(
            Brand(
                brand_name=brand_name,
            )
        )
        count += 1

    session.commit()

    print(f"Inserted {count} brands")
