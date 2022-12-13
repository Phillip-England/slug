def catering_for_slack_groupme(date, data):

    tomorrow = date.format_date(date.get_future_date(1) ,'x/x/xxxx')
    intro = f'Deferred Order Report {tomorrow}'
    br = 'BREAK'

    if len(data.pickup_orders) != 0 and len(data.delivery_orders) != 0:
        
        message = [intro, br, br]

        for order in data.pickup_orders:
            message.append(order)
            message.append(br)

        message.append(br)

        for order in data.delivery_orders:
            message.append(order)
            message.append(br)

        return message
    
    else:

        return [f'Deffered Order Report {tomorrow}', br, 'No Catering Orders']