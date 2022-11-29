def format_date(date_tuple, date_format):

    # the month and day value will always be two digets, example 10 or 08
    month = date_tuple[0]
    day = date_tuple[1]
    year = date_tuple[2]

    if date_format == 'x/x/xxxx':
        # removing additional 0s in front of day and month if needed     
        if day[0] == '0':
            day = day[1]
        if month[0] == '0':
            month = month[1]
        return f'{month}/{day}/{year}'