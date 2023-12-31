import pandas as pd

class NewsItem:
    def __init__(self, news_json):
        try:
            self.id = news_json['id'] if 'id' in news_json else None
            self.title = [i['title'] if 'title' in i else None for i in news_json]
            self.source_name = [i['sourceName'] if 'sourceName' in i else None for i in news_json]
            self.news_time = [i['newsTime']if 'newsTime' in i else None for i in news_json]
            self.news_url = [i['newsUrl'] if 'newsUrl' in i else None for i in news_json]
            self.site_type = [i['siteType'] if 'siteType' in i else None for i in news_json]
            self.collect_source = [i['collectSource']if 'collectSource' in i else None for i in news_json]



            self.data_dict = { 

                'ID': self.id,
                'Title': self.title,
                'Source Name': self.source_name,
                'News Time': self.news_time,
                'News URL': self.news_url,
                'Site Type': self.site_type,
                'Collect Source': self.collect_source
            }


            self.df = pd.DataFrame(self.data_dict)
        except KeyError:
            print(f"Error getting source name")

    def __repr__(self):
        return f"NewsItem(id={self.id}, title={self.title}, source_name={self.source_name})"