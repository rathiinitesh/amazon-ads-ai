from sqlalchemy import String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from typing import Optional

from app.db.base import Base
from .enum_models import (
    CampaignGoal,
    CampaignType,
    TargetingType,
    MatchType,
    CampaignState,
    BiddingStrategy,
    Placement,
    OptimizationStrategy,
    Priority,
)


class Campaign(Base):
    __tablename__ = "campaigns"

    campaign_id: Mapped[int] = mapped_column(primary_key=True)
    campaign_name: Mapped[str] = mapped_column(String(255), unique=True)
    campaign_goal: Mapped[CampaignGoal] = mapped_column(
        Enum(CampaignGoal), default=None
    )
    campaign_type: Mapped[CampaignType] = mapped_column(
        Enum(CampaignType), default=None
    )
    targeting_type: Mapped[TargetingType] = mapped_column(
        Enum(TargetingType), default=None
    )
    match_type: Mapped[MatchType] = mapped_column(
        Enum(MatchType), default=None, nullable=True
    )
    campaign_state: Mapped[CampaignState] = mapped_column(
        Enum(CampaignState), default=None
    )
    marketplace_id: Mapped[int] = mapped_column(
        ForeignKey("marketplaces.marketplace_id")
    )
    portfolio_id: Mapped[int] = mapped_column(ForeignKey("portfolios.portfolio_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"))
    daily_budget: Mapped[float] = mapped_column()
    bidding_strategy: Mapped[BiddingStrategy] = mapped_column(
        Enum(BiddingStrategy), default=None
    )
    placement: Mapped[Placement] = mapped_column(Enum(Placement), default=None)
    optimization_strategy: Mapped[OptimizationStrategy] = mapped_column(
        Enum(OptimizationStrategy), default=None
    )
    start_date: Mapped[date] = mapped_column()
    end_date: Mapped[Optional[date | None]] = mapped_column(nullable=True)
    priority: Mapped[Priority] = mapped_column(Enum(Priority), default=None)

    # Relationships
    marketplace = relationship("Marketplace", back_populates="campaigns")
    portfolio = relationship("Portfolio", back_populates="campaigns")
    product = relationship("Product", back_populates="campaigns")
    campaign_daily_metrics = relationship(
        "CampaignDailyMetrics", back_populates="campaign"
    )
