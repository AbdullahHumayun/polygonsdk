"""FETCHES TICKER-NEWS FROM POLYGON BY CATEGORY - SENDS TO DISCORD."""


from polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
from dataclasses import dataclass

api_key = YOUR_API_KEY
async_sdk = AsyncPolygonSDK(api_key)
@dataclass
class Publisher:
    def __init__(self, name, homepage_url, logo_url, favicon_url):
        self.name = name
        self.homepage_url = homepage_url
        self.logo_url = logo_url
        self.favicon_url = favicon_url
@dataclass
class NewsArticle:
    def __init__(self, id, publisher, title, author, published_utc, article_url, tickers, image_url, description, keywords):
        self.id = id
        self.publisher = publisher
        self.title = title
        self.author = author
        self.published_utc = published_utc
        self.article_url = article_url
        self.tickers = tickers
        self.image_url = image_url
        self.description = description
        self.keywords = keywords
        
keyword_hooks= {
        "Trading Ideas": "YOUR DISCORD WEBHOOK URL",
        "Long Ideas": "YOUR DISCORD WEBHOOK URL",
        "Short Sellers":"YOUR DISCORD WEBHOOK URL",
        "Trading Penny Stocks":"YOUR DISCORD WEBHOOK URL",
        "penny stocks to watch":"YOUR DISCORD WEBHOOK URL",
        "top penny stocks":"YOUR DISCORD WEBHOOK URL",
        "Short Ideas": "YOUR DISCORD WEBHOOK URL",
        "Penny Stock News":"YOUR DISCORD WEBHOOK URL",
        "Tech":"YOUR DISCORD WEBHOOK URL",
        "Rumors":"YOUR DISCORD WEBHOOK URL",
        "Penny Stocks": "YOUR DISCORD WEBHOOK URL",
        "best penny stocks":"YOUR DISCORD WEBHOOK URL",
        "list of penny stocks":"YOUR DISCORD WEBHOOK URL",

        "Large Cap": "YOUR DISCORD WEBHOOK URL",
        "Upgrades": "YOUR DISCORD WEBHOOK URL",
        "Downgrades":"YOUR DISCORD WEBHOOK URL",
        "Price Target": "YOUR DISCORD WEBHOOK URL",
        "Small Cap": "YOUR DISCORD WEBHOOK URL",
        "Analyst Ratings": "YOUR DISCORD WEBHOOK URL",
        "Initial Public Offerings": "YOUR DISCORD WEBHOOK URL",
        "Financing Agreements": "YOUR DISCORD WEBHOOK URL",
        "Conference Calls/ Webcasts":"YOUR DISCORD WEBHOOK URL",
        "Calendar of Events": "YOUR DISCORD WEBHOOK URL",
        "Law & Legal Issues":"YOUR DISCORD WEBHOOK URL",
        "Company Announcement":"YOUR DISCORD WEBHOOK URL",
        "Earnings":"YOUR DISCORD WEBHOOK URL",
        "earningscall-transcripts":"YOUR DISCORD WEBHOOK URL",
        "Earnings Releases and Operating Results":"YOUR DISCORD WEBHOOK URL",
        "Partnerships":"YOUR DISCORD WEBHOOK URL",
        "Mergers and Acquisitions":"YOUR DISCORD WEBHOOK URL",
        "Movers":"YOUR DISCORD WEBHOOK URL",
        "Cryptocurrency":"YOUR DISCORD WEBHOOK URL",
        "Top Stories":"YOUR DISCORD WEBHOOK URL",
        "Global":"YOUR DISCORD WEBHOOK URL",
        "Government":"YOUR DISCORD WEBHOOK URL",
        "European Regulatory News": "YOUR DISCORD WEBHOOK URL",
        "Sector ETFs": "YOUR DISCORD WEBHOOK URL",
        "Broad U.S. Equity ETFs": "YOUR DISCORD WEBHOOK URL",
        "Management statements": "YOUR DISCORD WEBHOOK URL",
        "ETFs": "YOUR DISCORD WEBHOOK URL",
        "investing": "YOUR DISCORD WEBHOOK URL",
        "Company Regulatory Filings": "YOUR DISCORD WEBHOOK URL",
        "Insider's Buy/Sell": "YOUR DISCORD WEBHOOK URL"

    }