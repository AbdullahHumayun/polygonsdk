import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from datetime import datetime
import pytz
import pandas as pd

def format_date(input_str):
    # Parse the input string as a datetime object
    input_datetime = datetime.fromisoformat(input_str.replace("Z", "+00:00"))

    # Convert the datetime object to Eastern Time
    utc_timezone = pytz.timezone("UTC")
    eastern_timezone = pytz.timezone("US/Eastern")
    input_datetime = input_datetime.astimezone(utc_timezone)
    eastern_datetime = input_datetime.astimezone(eastern_timezone)

    # Format the output string
    output_str = eastern_datetime.strftime("%Y-%m-%d at %I:%M%p %Z")
    return output_str
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


        self.data_dict = { 
        'Actual': self.actual,
        'Comment': self.comment,
        'Country': self.country,
        'Currency': self.currency,
        'Date': self.date,
        'Time': self.time,
        'Forecast': self.forecast,
        'Id': self.id,
        'Importance': self.importance,
        'Indicator': self.indicator,
        'Link': self.link,
        'Period': self.period,
        'Previous': self.previous,
        'Scale': self.scale,
        'Source': self.source,
        'Title': self.title,
        'Unit': self.unit
    }
        self.df = pd.DataFrame(self.data_dict)
    def __str__(self):
        return f"Event(id={self.id}, date={self.date}, time={self.time}, title={self.title}, importance={self.importance})"

    def __repr__(self):
        return self.__str__()