from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date


from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    asin: Mapped[str] = mapped_column(String(20), unique=True)
    sku: Mapped[str] = mapped_column(String(50), unique=True)
    product_name: Mapped[str] = mapped_column(String(255))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.brand_id"))
    price: Mapped[float] = mapped_column()
    launch_date: Mapped[date] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("product_categories.category_id")
    )

    # Relationships
    brand = relationship("Brand", back_populates="products")
    category = relationship("ProductCategory", back_populates="products")
