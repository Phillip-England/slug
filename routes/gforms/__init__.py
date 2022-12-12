import os

from ._sales_data import sales_data
from ._track_southroads_sales import track_southroads_sales

class gforms:

    def __init__(self):
        self.sales_tracking_form_url = os.environ.get("SALES_GOOGLE_FORM")
        self.sales_form_input_class_name = 'whsOnd'
        self.sales_form_submit_class_name = 'NPEfkd'

    # routes
    def sales_data(self, driver, config, data): sales_data(self, driver, config, data)

    # scripts
    def track_southroads_sales(self, engine): track_southroads_sales(engine)