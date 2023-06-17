from datetime import datetime, timedelta

class CustomDate:
    def __init__(self, date_str):
        self.date = self._parse_date(date_str)

    def _parse_date(self, date_str):
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            try:
                date = datetime.strptime(date_str, '%m/%d/%Y')
            except ValueError:
                raise ValueError("Invalid date format. Supported formats: YYYY-MM-DD, MM/DD/YYYY")
        return date.date()

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

    def __repr__(self):
        return self.__str__()

    def days_after(self, days):
        delta = timedelta(days=days)
        new_date = self.date + delta
        return CustomDate(new_date.strftime('%Y-%m-%d'))

    def days_before(self, days):
        delta = timedelta(days=days)
        new_date = self.date - delta
        return CustomDate(new_date.strftime('%Y-%m-%d'))