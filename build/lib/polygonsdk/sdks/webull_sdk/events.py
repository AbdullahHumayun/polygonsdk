import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from ..helpers.helpers import format_date

class Event:
    def __init__(self, data):
        self.actual = data.get('actual', None)
        self.comment = data.get('comment', None)
        self.country = data['country']
        self.currency = data['currency']
        self.date = data['date']
        self.time = format_date(self.date)
        self.forecast = data['forecast']
        self.id = data['id']
        self.importance = data['importance']
        self.indicator = data['indicator']
        self.link = data['link']
        self.period = data['period']
        self.previous = data['previous']
        self.scale = data['scale']
        self.source = data['source']
        self.title = data['title']
        self.unit = data['unit']

    def __str__(self):
        return f"Event(id={self.id}, date={self.date}, time={self.time}, title={self.title}, importance={self.importance})"

    def __repr__(self):
        return self.__str__()