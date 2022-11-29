import csv

def extract_cem_spreadsheet_data(engine):

    report = open(engine.config.cem_spreadsheet_download_path, 'r')
    reader = csv.reader(report)
    print(reader)

    # okay, we are collecting scores from a given date
    # we need to set up Current Month, 90 day rolling, and current year
    # our sheet is formatted in the x/x/xxxx format

    # 90 day rolling
    ninty_days_ago_date_crude = engine.date.get_past_date(90)
    ninty_days_ago_date = engine.date.format_date(ninty_days_ago_date_crude, 'x/x/xxxx')

    # first of the month
    first_of_month_date_crude = engine.date.first_of_month()
    first_of_month_date = engine.date.format_date(first_of_month_date_crude, 'x/x/xxxx')

    # first of the year
    first_of_year_date_crude = engine.date.first_of_year()
    first_of_year_date = engine.date.format_date(first_of_year_date_crude, 'x/x/xxxx')

    # data holders for operations
    number_of_surveys_holder = []
    osat_holder = []
    taste_holder = []
    speed_holder = []
    ace_holder = []
    cleanliness_holder = []
    accuracy_holder = []

    # steps
    date_step = 1
    day_of_week_step = 2
    number_of_surveys_step = 3
    osat_step = 4
    taste_step = 5
    speed_step = 6
    ace_step = 7
    cleanliness_step = 8
    accuracy_step = 9

    # triggers
    ninty_day_trigger = False
    current_month_trigger = False
    current_year_trigger = False

    # collecting 90 day rolling
    for row in reader:
    
        if row[date_step] == ninty_days_ago_date:
            ninty_day_trigger = True

        if ninty_day_trigger == True:
            number_of_surveys_holder.append(row[number_of_surveys_step])
            osat_holder.append(row[osat_step])
            taste_holder.append(row[taste_step])
            speed_holder.append(row[speed_step])
            ace_holder.append(row[ace_step])
            cleanliness_holder.append(row[cleanliness_step])
            accuracy_holder.append(row[accuracy_step])
    
    # setting 90 day rolling lists
    engine.data.ninty_day_survey_list = number_of_surveys_holder
    engine.data.ninty_day_osat_list = osat_holder
    engine.data.ninty_day_taste_list = taste_holder
    engine.data.ninty_day_speed_list = speed_holder
    engine.data.ninty_day_ace_list = ace_holder
    engine.data.ninty_day_cleanliness_list = cleanliness_holder
    engine.data.ninty_day_accuracy_list = accuracy_holder

    # clearing out our holders
    number_of_surveys_holder.clear()
    osat_holder.clear()
    taste_holder.clear()
    speed_holder.clear()
    ace_holder.clear()
    cleanliness_holder.clear()
    accuracy_holder.clear()


            