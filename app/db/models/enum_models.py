from enum import Enum


class CampaignGoal(str, Enum):
    SALES = "Sales"
    BRAND_AWARENESS = "Brand Awareness"
    PRODUCT_LAUNCH = "Product Launch"
    TRAFFIC = "Traffic"
    STORE_VISITS = "Store Visits"


class CampaignType(str, Enum):
    SPONSORED_PRODUCTS = "Sponsored Products"
    SPONSORED_BRANDS = "Sponsored Brands"
    SPONSORED_DISPLAY = "Sponsored Display"


class TargetingType(str, Enum):
    AUTO = "Auto"
    MANUAL = "Manual"


class MatchType(str, Enum):
    BROAD = "Broad"
    PHRASE = "Phrase"
    EXACT = "Exact"
    PRODUCT_TARGETING = "Product Targeting"
    CATEGORY_TARGETING = "Category Targeting"


class CampaignState(str, Enum):
    ENABLED = "Enabled"
    PAUSED = "Paused"
    ARCHIVED = "Archived"


class BiddingStrategy(str, Enum):
    DYNAMIC_DOWN = "Dynamic Down"
    DYNAMIC_UP_AND_DOWN = "Dynamic Up and Down"
    FIXED_BIDS = "Fixed Bids"


class Placement(str, Enum):
    TOP_OF_SEARCH = "Top of Search"
    REST_OF_SEARCH = "Rest of Search"
    PRODUCT_PAGES = "Product Pages"


class OptimizationStrategy(str, Enum):
    MAXIMISE_CLICKS = "Maximise Clicks"
    MAXIMISE_CONVERSIONS = "Maximise Conversions"
    TARGET_ACOS = "Target ACOS"
    TARGET_ROAS = "Target ROAS"
    MANUAL = "Manual"


class Priority(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class MessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
