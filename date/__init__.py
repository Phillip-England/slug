from ._get_past_date import get_past_date
from ._format_date import format_date
from ._first_of_month import first_of_month
from ._first_of_year import first_of_year
from ._get_future_date import get_future_date


class date:

    def __init__(self):
        self.days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.months_of_year = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    def get_past_date(self, days_in_past): return get_past_date(days_in_past)
    def format_date(self, date_tuple, date_format): return format_date(date_tuple, date_format)
    def first_of_month(self): return first_of_month()
    def first_of_year(self): return first_of_year()
    def get_future_date(self, days_in_future): return get_future_date(days_in_future)

        


            






    
