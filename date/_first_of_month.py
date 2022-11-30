import datetime

def first_of_month():

    # getting the current month and year
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year

    # we also need to return the second and third of the month, because what if a business day fell on a Sunday?

    return [
            (str(current_month), '1', str(current_year)),
            (str(current_month), '2', str(current_year)),
            (str(current_month), '3', str(current_year))
            ]