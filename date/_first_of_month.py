import datetime

def first_of_month():

    # getting the current month and year
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year

    return (str(current_month), '1', str(current_year))