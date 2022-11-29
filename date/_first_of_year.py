import datetime

def first_of_year():

    # getting the current year
    current_year = datetime.datetime.now().year

    return ('1', '1', str(current_year))