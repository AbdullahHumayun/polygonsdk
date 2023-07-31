
from dataclasses import dataclass
from typing import List, Optional
from typing import Dict, Any

from discord_webhook import DiscordEmbed

@dataclass
class Session:

    change: float = 0.0
    change_percent: float = 0.0
    close: float = 0.0
    early_trading_change: float = 0.0
    early_trading_change_percent: float = 0.0
    high: float = 0.0
    late_trading_change: float = 0.0
    late_trading_change_percent: float = 0.0
    low: float = 0.0
    open: float = 0.0
    previous_close: float = 0.0
    volume: int = 0

    @staticmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Session':
        return cls(
            change=data.get('change', 0.0),
            change_percent=data.get('change_percent', 0.0),
            close=data.get('close', 0.0),
            early_trading_change=data.get('early_trading_change', 0.0),
            early_trading_change_percent=data.get('early_trading_change_percent', 0.0),
            high=data.get('high', 0.0),
            late_trading_change=data.get('late_trading_change', 0.0),
            late_trading_change_percent=data.get('late_trading_change_percent', 0.0),
            low=data.get('low', 0.0),
            open=data.get('open', 0.0),
            previous_close=data.get('previous_close', 0.0),
            volume=data.get('volume', 0)
        )



@dataclass
class UnderlyingAsset:
    change_to_break_even: Optional[str] = None
    price: Optional[str] = None
    ticker: Optional[str] = None
    value: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'UnderlyingAsset':
        return cls( 
            change_to_break_even = data.get('change_to_breaK_even', None),
            price = data.get('price', None),
            ticker = data.get('ticker', None)
        )

@dataclass
class Greeks:
    delta: float
    gamma: float
    theta: float
    vega: float

    @classmethod
    def from_dict(cls, data: dict) -> 'Greeks':
        return cls(
            vega = data.get('vega'),
            gamma = data.get('gamma'),
            theta = data.get('theta'),
            delta = data.get('delta')
        )


@dataclass
class LastQuote:
    ask: float
    ask_size: int
    bid: float
    bid_size: int
    last_updated: int
    midpoint: float
    timeframe: Optional[str] = None  # adding this new field

    @classmethod
    def from_dict(cls, data: dict) -> 'LastQuote':
        return cls(
            ask=data.get('ask'),
            ask_size=data.get('ask_size'),
            bid=data.get('bid'),
            bid_size=data.get('bid_size'),
            last_updated=data.get('last_updated'),
            midpoint=data.get('midpoint'),
            timeframe=data.get('timeframe')  # account for the new field here too
        )


@dataclass
class LastTrade:
    conditions: Optional[List[int]]
    exchange: Optional[int]
    price: Optional[float]
    size: Optional[int]
    timeframe: Optional[str]
    last_updated: Optional[str]
    id: Optional[int]
    sip_timestamp: Optional[str]

    @classmethod
    def from_dict(cls, data: dict) -> 'LastTrade':
        return cls(
            conditions=data.get('conditions'),
            exchange=data.get('exchange'),
            price=data.get('price'),
            size=data.get('size'),
            timeframe=data.get('timeframe'),
            last_updated=data.get('last_updated'),
            id=data.get('id'),
            sip_timestamp=data.get('sip_timestamp'),
        )
    


@dataclass
class UniversalSnapshotResult:
    market_status: Optional[str] = None
    implied_volatility: Optional[float] = None
    open_interest: Optional[int] = None
    name: Optional[str] = None
    
    type: Optional[str] = None
    session: Optional[Session] = None
    last_quote: Optional[LastQuote] = None
    last_trade: Optional[LastTrade] = None
    greeks: Optional[Greeks] = None
    underlying_asset: Optional[UnderlyingAsset] = None
    ticker: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'UniversalSnapshotResult':
        return cls(
            market_status=data.get('market_status', None),
            implied_volatility=data.get('implied_volatility', None),
            open_interest=data.get('open_interest', None),
            name=data.get('name', None),
            ticker=data.get('ticker', None),
            type=data.get('type', None),
            session=Session.from_dict(data.get('session', {})),
            last_quote=LastQuote.from_dict(data.get('last_quote', {})),
            greeks = Greeks.from_dict(data.get('greeks', {})),
            underlying_asset = UnderlyingAsset.from_dict(data.get('underlying_asset', {})),
            last_trade=LastTrade.from_dict(data.get('last_trade', {}))
        )
    
    @classmethod
    def from_list(cls, data: List[dict]) -> List['UniversalSnapshotResult']:
        return [cls.from_dict(item) for item in data]
    

    def to_embed(self) -> DiscordEmbed:
        """Create a Discord embed from this article."""
        embed = DiscordEmbed(title=f"Ticker 📰 News", description=f"```py\nOption snapshot result - {self.ticker}```")
        # Adding author as a field

        if self.open_interest is not None and self.implied_volatility is not None and self.market_status is not None:
            embed.add_embed_field(name=f"IV & OI:", value=f"> IV: **{self.implied_volatility}**\n> OI: **{self.open_interest}**")

        if self.session is not None:
            if self.session.change and self.session.change_percent and self.session.close and self.session.low and self.session.volume and self.session.early_trading_change and self.session.early_trading_change_percent and self.session.high and self.session.open and self.session.previous_close:
                embed.add_embed_field(name="Day Stats:", value=f"> Open: **${self.session.open}**\n> High: **${self.session.high}**\n> Last: **${self.session.close}**\n> Low: **${self.session.low}\n> Prev. Close: **${self.session.previous_close}**\n> Volume: **{self.session.volume}**", inline=False)
       
        if self.last_quote is not None:
            if self.last_quote.ask and self.last_quote.bid and self.last_quote.bid_size and self.last_quote.ask_size and self.last_quote.midpoint:
                embed.add_embed_field(name=f"Last Quote:", value=f"> Bid: **${self.last_quote.bid}**\n> Bid Size: **{self.last_quote.bid_size}**\n> Mid: **${self.last_quote.midpoint}**\n> Ask: **${self.last_quote.ask}**\n> Ask Size: **{self.last_quote.ask_size}**")
        
    
        if self.last_trade is not None:
            if self.last_trade.conditions and self.last_trade.exchange and self.last_trade.price and self.last_trade.sip_timestamp and self.last_trade.size:

                embed.add_embed_field(name=f"Last Trade:", value=f"> Size: **{self.last_trade.size}**\n> Price: **${self.last_trade.price}**\n> Exchange: **{self.last_trade.exchange}**\n> Conditions: **{self.last_trade.conditions}**\n> Timestamp: **{self.last_trade.sip_timestamp}**")
        
        if self.underlying_asset is not None:
            if self.underlying_asset.change_to_break_even and self.underlying_asset.ticker:
                value_or_price = self.underlying_asset.value if self.underlying_asset.value else self.underlying_asset.price
                embed.add_embed_field(
                    name="Underlying:",
                    value=f"> Value/Price: **${value_or_price}**\n"
                        f"> Change to Break Even: **{self.underlying_asset.change_to_break_even}**\n"
                        f"> Ticker: **{self.underlying_asset.ticker}**"
                )

        return embed
    

    def to_unusual_embed(self) -> Optional[DiscordEmbed]:
        """Create a Discord embed specifically for unusual options."""
        # Checks to ensure some conditions are met
        if not (self.session and self.open_interest is not None and self.session.volume is not None and self.session.volume > self.open_interest):
            return None

        embed = DiscordEmbed(title="Unusual Option Activity 📈", description=f"```py\nUnusual option contract detected - {self.ticker}\nAn unusual option means that there is more contract volume than implied volatility.```")

        embed.add_embed_field(name="Day Stats:", value=f"> Open: **${self.session.open}**\n> High: **${self.session.high}**\n> Last: **${self.session.close}**\n> Low: **${self.session.low}\n> Prev. Close: **${self.session.previous_close}**\n> Volume: **{self.session.volume}**", inline=False)
        embed.add_embed_field(name=f"Vol vs. OI:",value=f"> Vol: **{self.session.volume}**\n> OI: **{self.open_interest}**")
        embed.add_embed_field(name=f"Last Trade:", value=f"> Size: **{self.last_trade.size}**\n> Price: **${self.last_trade.price}**\n> Exchange: **{self.last_trade.exchange}**\n> Conditions: **{self.last_trade.conditions}**\n> Timestamp: **{self.last_trade.sip_timestamp}**")

        return embed