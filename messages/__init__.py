from ._groupme_deferred_order_message import groupme_deferred_order_message


class messages:
    def __init__(self):
        pass

    def groupme_deferred_order_message(self, engine, deferred_orders): return groupme_deferred_order_message(engine, deferred_orders)