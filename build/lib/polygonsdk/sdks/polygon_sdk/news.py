class News:
    def __init__(self, results):
        self.news_url = results.get('amp_url', None)
        self.article_url = results.get('article_url', None)
        self.author = results.get('author', None)
        self.description = results.get('description', None)
        self.image_url = results.get('image_url', None)
        self.keywords = results.get('keywords', None)
        self.pub_time = results.get('published_utc', None)
        publisher = results.get('publisher', None)
        self.tickers = results.get('tickers', None)
        self.favicon_url = publisher.get('favicon_url', None)
        self.homepage_url = publisher.get('homepage_url', None)
        self.logo_url = publisher.get('logo_url', None)
        self.name = publisher.get('name', None)
        self.title = results.get('title', None)

