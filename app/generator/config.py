from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class GeneratorConfig:
    # Marketplaces
    MARKETPLACES = [
        ("US", "Amazon.com", "USD"),
        ("CA", "Amazon.ca", "CAD"),
        ("UK", "Amazon.co.uk", "GBP"),
        ("DE", "Amazon.de", "EUR"),
        ("FR", "Amazon.fr", "EUR"),
        ("IT", "Amazon.it", "EUR"),
        ("ES", "Amazon.es", "EUR"),
        ("IN", "Amazon.in", "INR"),
        ("JP", "Amazon.co.jp", "JPY"),
        ("AU", "Amazon.com.au", "AUD"),
    ]

    # Master data
    NUM_BRANDS = 50
    NUM_CATEGORIES = 20
    NUM_PRODUCTS = 500
    NUM_PORTFOLIOS = 25
    NUM_CAMPAIGNS = 2500

    # Campaign duration
    START_DATE = date(2025, 1, 1)
    END_DATE = date(2025, 12, 31)

    # Performance
    MIN_DAILY_BUDGET = 10
    MAX_DAILY_BUDGET = 500

    MIN_CPC = 0.20
    MAX_CPC = 5.00

    MIN_CTR = 0.003
    MAX_CTR = 0.08

    MIN_CONVERSION_RATE = 0.02
    MAX_CONVERSION_RATE = 0.25

    RANDOM_SEED = 42
