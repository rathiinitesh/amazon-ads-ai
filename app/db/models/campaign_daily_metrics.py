from datetime import date, datetime

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class CampaignDailyMetrics(Base):
    __tablename__ = "campaign_daily_metrics"

    __table_args__ = (
        UniqueConstraint(
            "campaign_id",
            "report_date",
            name="uq_campaign_report_date",
        ),
    )

    metric_id: Mapped[int] = mapped_column(primary_key=True)
    campaign_id: Mapped[int] = mapped_column(ForeignKey("campaigns.campaign_id"))
    report_date: Mapped[date] = mapped_column()
    impressions: Mapped[int] = mapped_column()
    clicks: Mapped[int] = mapped_column()
    spend: Mapped[float] = mapped_column()
    orders: Mapped[int] = mapped_column()
    orders_7d: Mapped[int] = mapped_column()
    orders_14d: Mapped[int] = mapped_column()
    orders_30d: Mapped[int] = mapped_column()
    units_sold: Mapped[int] = mapped_column()
    sales: Mapped[float] = mapped_column()
    sales_7d: Mapped[float] = mapped_column()
    sales_14d: Mapped[float] = mapped_column()
    sales_30d: Mapped[float] = mapped_column()
    new_to_brand_orders: Mapped[int] = mapped_column()
    new_to_brand_sales: Mapped[float] = mapped_column()
    new_to_brand_sales_percentage: Mapped[float] = mapped_column()
    cpc: Mapped[float] = mapped_column()
    cpm: Mapped[float] = mapped_column()
    ctr: Mapped[float] = mapped_column()
    conversion_rate: Mapped[float] = mapped_column()
    aov: Mapped[float] = mapped_column()
    acos: Mapped[float] = mapped_column()
    roas: Mapped[float] = mapped_column()
    roi: Mapped[float] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

    # Relationships
    campaign = relationship("Campaign", back_populates="campaign_daily_metrics")
