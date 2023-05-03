class NewsItem:
    def __init__(self, news_json):
        try:
            self.id = news_json['id']
            self.title = news_json['title']
            self.source_name = news_json['sourceName']
            self.news_time = news_json['newsTime']
            self.news_url = news_json['newsUrl']
            self.site_type = news_json['siteType']
            self.collect_source = news_json['collectSource']
        except KeyError:
            print(f"Error getting source name")

    def __repr__(self):
        return f"NewsItem(id={self.id}, title={self.title}, source_name={self.source_name})"