import datetime

def get_future_date(days_in_future):


    # getting current date
    start_date = datetime.date(
        datetime.datetime.now().year, 
        datetime.datetime.now().month,
        datetime.datetime.now().day
    )

    # getting the past day
    delta = datetime.timedelta(days=days_in_future)
    past_date = start_date + delta


    # getting past date out of original format
    month = ''
    day = ''
    year = ''
    dash_count = 0
    for char in str(past_date):
        if char == '-':
            dash_count = dash_count + 1
            continue
        if dash_count == 0:
            year = year + char
        if dash_count == 1:
            month = month + char
        if dash_count == 2:
            day = day + char

    return (month, day, year)