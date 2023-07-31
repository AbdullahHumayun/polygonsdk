import pandas as pd

class TickerNews:
    def __init__(self, results):
        
        
        self.id = [i['id'] if 'id' in i else None for i in results]


        self.publisher = [i['publisher'] if 'publisher' in i else None for i in results]
        self.title = [i['title'] if 'title' in i else None for i in results]
        self.author = [i['author'] if 'author' in i else None for i in results]
        self.published_utc = [i['published_utc'] if 'published_utc' in i else None for i in results]
        self.article_url = [i['article_url'] if 'article_url' in i else None for i in results]
        self.tickers = [i['tickers'] if 'tickers' in i else None for i in results]
        self.image_url = [i['image_url'] if 'image_url' in i else None for i in results]
        self.description = [i['description'] if 'description' in i else None for i in results]
        self.keywords = [i['keywords'] if 'keywords' in i else None for i in results]


        self.data_dict = {
            'Title': self.title,
            'Author': self.author,
            'Published Time': self.published_utc,
            'Article URL': self.article_url,
            'Tickers Mentioned': self.tickers,
            'Image URL': self.image_url,
            'Description': self.description,
            'Keywords': self.keywords

        }

        self.df = pd.DataFrame(self.data_dict)