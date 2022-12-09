def groupme_deferred_order_message(engine, deferred_orders):
    pickups_complete = False
    tomorrow = engine.date.format_date(engine.date.get_future_date(1) ,'x/x/xxxx')
    message = f'Deferred Order Report {tomorrow} \n\nPICKUP ORDERS \n'

    for order in deferred_orders:

        if order[0] == 'D' and pickups_complete == False:
            message = message + '\n' + 'DELIVERY ORDERS' + '\n'
            pickups_complete = True

        message = message + order + '\n'

    return message