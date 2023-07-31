from dataclasses import dataclass, field
from typing import List, Optional
from discord_webhook import DiscordEmbed
from hooks.hook_dicts import CATEGORY_WEBHOOKS

CATEGORY_KEYWORDS = {
    "EQUITY_MARKET_NEWS": ["Analyst Ratings", "Directors and Officers", "Stock Market News", 
                            "Equities", "Intraday Update", "Upgrades", "Downgrades", 
                            "Initiation", "Analyst Ratings"],
    "ANALYSIS_AND_ADVICE": ["investing", "how-to-investthirteen-steps-2", "Trading Ideas", 
                             "Analyst Color"],
    "SPECIFIC_MARKETS": ["Warrants and Certificates", "Penny Stock Basics", "Trading Penny Stocks", 
                          "best penny stocks", "list of penny stocks", "penny stock", 
                          "penny stock news", "penny stocks", "penny stocks to buy", 
                          "penny stocks to watch", "top penny stocks", "Cryptocurrency", 
                          "Markets", "Tech", "SEC", "Small Cap", "Large Cap", "Mid Cap"],
    "CORP_ACTION_GOVERNANCE": ["Annual Meetings & Shareholder Rights", "Directors and Officers", 
                                "Changes in company's own shares", "Management statements", 
                                "Management Changes", "Net Asset Value"],
    "PRODUCT_PARTNERSHIP": ["Product / Services Announcement", "Partnerships"],
    "CORPORATE_FINANCE": ["Financing Agreements", "Business Contracts", "Mergers and Acquisitions", 
                           "Earnings", "Dividend Reports and Estimates"],
    "EVENTS": ["Calendar of Events", "Conference Calls/ Webcasts"],
    "REGULATORY": ["Regulatory information", "European Regulatory News", "SEC", "Law & Legal Issues"],
    "HEALTH_CLINICAL": ["Health", "Clinical Study"],
    "GENERAL": ["News", "Media", "Commodities", "Movers", "Bonds", "Advisory", 
                 "Press Release", "Pre-Market Outlook"]
  
}




@dataclass
class Publisher:
    favicon_url: Optional[str] = None
    homepage_url: Optional[str] = None
    logo_url: Optional[str] = None
    name: Optional[str] = None

@dataclass
class NewsArticle:
    
    article_url: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    image_url: Optional[str] = None
    
    published_utc: Optional[str] = None
    publisher: Optional[Publisher] = None
    tickers: Optional[List[str]] = None
    title: Optional[str] = None
    category: Optional[str] = None
    amp_url: Optional[str] = None
    keywords: Optional[List[str]] = field(default_factory=list)
    discord_webhook: Optional[str] = None

    def __post_init__(self):
        self.assign_category()
        
    def assign_category(self):
        # Assign the category and discord_webhook based on the article's keywords
        for category, keywords in CATEGORY_KEYWORDS.items():
            if any(keyword in self.keywords for keyword in keywords):
                self.category = category
                self.discord_webhook = CATEGORY_WEBHOOKS[category]
                break

    def to_embed(self) -> DiscordEmbed:
        """Create a Discord embed from this article."""
        embed = DiscordEmbed(title=f"Ticker 📰 News", description=f"```py\n{self.title}\n\n{self.description}```")
        # Adding author as a field
        if self.author:
            embed.add_embed_field(name="Author", value=self.author)
        
        # Adding publisher name as a field
        if self.publisher and self.publisher.name:
            embed.add_embed_field(name="Publisher", value=self.publisher.name)
        
        # Adding published date as a field
        if self.published_utc:
            embed.add_embed_field(name="Published", value=self.published_utc)
        
        # Adding image to embed
        if self.image_url:
            embed.set_image(url=self.image_url)
        
        if self.category:
            embed.add_embed_field(name=f"Category:", value=f"> **{self.category}**")
        
        # Adding tickers as a field
        if self.tickers:
            embed.add_embed_field(name="Tickers", value=f"> **{', '.join(self.tickers)}**")

        if self.amp_url:
            embed.add_embed_field(name=f"URL:", value=f"> {self.article_url}", inline=False)
        
        return embed