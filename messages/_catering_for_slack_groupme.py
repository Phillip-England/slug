def catering_for_slack_groupme(date, data):

    tomorrow = date.format_date(date.get_future_date(1) ,'x/x/xxxx')
    intro = f'Deferred Order Report {tomorrow}'
    br = 'BREAK'
    
    message = [intro, br, br]

    for order in data.pickup_orders:
        message.append(order)
        message.append(br)

    message.append(br)

    for order in data.delivery_orders:
        message.append(order)
        message.append(br)


    return message