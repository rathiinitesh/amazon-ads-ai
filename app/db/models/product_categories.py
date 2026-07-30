from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ProductCategory(Base):
    __tablename__ = "product_categories"

    category_id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column(String(100))
    parent_category_id: Mapped[int] = mapped_column(
        ForeignKey("product_categories.category_id"), nullable=True
    )

    # Relationships
    parent_category = relationship(
        "ProductCategory", remote_side=[category_id], back_populates="sub_categories"
    )
    sub_categories = relationship("ProductCategory", back_populates="parent_category")
