def catering_for_slack_groupme(engine, deferred_orders):

    tomorrow = engine.date.format_date(engine.date.get_future_date(1) ,'x/x/xxxx')
    intro = f'Deferred Order Report {tomorrow}'
    pickup_header = 'PICKUP ORDERS'
    delivery_header = 'DELIVERY ORDERS'
    br = 'BREAK'
    
    pickup_orders = deferred_orders[0]
    delivery_orders = deferred_orders[1]
    message = [intro, br, br]

    for order in pickup_orders:
        message.append(order)
        message.append(br)

    message.append(br)

    for order in delivery_orders:
        message.append(order)
        message.append(br)


    return message