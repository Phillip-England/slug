from ._extract_daypart_activity import extract_daypart_activity
from ._extract_cem_scores import extract_cem_scores
from ._extract_sales_activity import extract_sales_activity
from ._extract_deferred_orders import extract_deferred_orders

class data:
    def __init__(self):
        self.daypart_activity = {}
        self.sales_activity = {}
        self.cems = {}
        self.pickup_orders = []
        self.delivery_orders = []

    def extract_daypart_activity(self, config): extract_daypart_activity(self, config)
    def extract_cem_scores(self, config): extract_cem_scores(self, config)
    def extract_sales_activity(self, config): extract_sales_activity(self, config)
    def extract_deferred_orders(self, config): extract_deferred_orders(self, config)

