import csv

def extract_cem_spreadsheet_data(engine):

    try:

        report = open(engine.config.cem_spreadsheet_download_path, 'r')
        reader = csv.reader(report)

        # okay, we are collecting scores from a given date
        # we need to set up Current Month, 90 day rolling, and current year
        # our sheet is formatted in the x/x/xxxx format

        # 90 day rolling
        ninty_days_ago_date_crude = engine.date.get_past_date(90)
        ninty_days_ago_date = engine.date.format_date(ninty_days_ago_date_crude, 'x/x/xxxx')

        # first of the month
        first_of_month_date_crude = engine.date.first_of_month()
        first_of_month_date = engine.date.format_date(first_of_month_date_crude[0], 'x/x/xxxx')
        second_of_month_date = engine.date.format_date(first_of_month_date_crude[1], 'x/x/xxxx')
        third_of_month_date = engine.date.format_date(first_of_month_date_crude[2], 'x/x/xxxx')

        print(first_of_month_date)
        print(second_of_month_date)
        print(third_of_month_date)

        # first of the year
        first_of_year_date_crude = engine.date.first_of_year()
        first_of_year_date = engine.date.format_date(first_of_year_date_crude, 'x/x/xxxx')

        # data holders for 90 days
        engine.data.ninty_day_survey_list = []
        engine.data.ninty_day_day_of_week_list = []
        engine.data.ninty_day_osat_list = []
        engine.data.ninty_day_taste_list = []
        engine.data.ninty_day_speed_list = []
        engine.data.ninty_day_ace_list = []
        engine.data.ninty_day_cleanliness_list = []
        engine.data.ninty_day_accuracy_list = []

        # data holders for current month
        engine.data.current_month_survey_list = []
        engine.data.current_month_day_of_week_list = []
        engine.data.current_month_osat_list = []
        engine.data.current_month_taste_list = []
        engine.data.current_month_speed_list = []
        engine.data.current_month_ace_list = []
        engine.data.current_month_cleanliness_list = []
        engine.data.current_month_accuracy_list = []

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
        current_month_second_day_trigger = False
        current_month_third_day_trigger = False
        current_year_trigger = False

        # collecting 90 day rolling
        for row in reader:
        
            if row[date_step] == ninty_days_ago_date:
                ninty_day_trigger = True

            if ninty_day_trigger == True:
                engine.data.ninty_day_survey_list.append(row[number_of_surveys_step])
                engine.data.ninty_day_day_of_week_list.append(row[day_of_week_step])
                engine.data.ninty_day_osat_list.append(row[osat_step])
                engine.data.ninty_day_taste_list.append(row[taste_step])
                engine.data.ninty_day_speed_list.append(row[speed_step])
                engine.data.ninty_day_ace_list.append(row[ace_step])
                engine.data.ninty_day_cleanliness_list.append(row[cleanliness_step])
                engine.data.ninty_day_accuracy_list.append(row[accuracy_step])
        


        # what if the first of the month falls on a Sunday or a business day where we are not open?

        # reinitializing report. For whatever reason, it only let's us run through the report once before needing to reinitialize.
        report = open(engine.config.cem_spreadsheet_download_path, 'r')
        reader = csv.reader(report)


        # getting current month
        for row in reader:

            if row[date_step] == first_of_month_date:
                current_month_trigger = True

            if row[date_step] == second_of_month_date:
                current_month_second_day_trigger = True

            if row[date_step] == third_of_month_date:
                current_month_third_day_trigger = True

            if current_month_trigger == True or current_month_second_day_trigger == True or current_month_third_day_trigger == True:
                engine.data.current_month_survey_list.append(row[number_of_surveys_step])
                engine.data.current_month_day_of_week_list.append(row[day_of_week_step])
                engine.data.current_month_osat_list.append(row[osat_step])
                engine.data.current_month_taste_list.append(row[taste_step])
                engine.data.current_month_speed_list.append(row[speed_step])
                engine.data.current_month_ace_list.append(row[ace_step])
                engine.data.current_month_cleanliness_list.append(row[cleanliness_step])
                engine.data.current_month_accuracy_list.append(row[accuracy_step])

        if current_month_trigger == False and current_month_second_day_trigger == False and current_month_third_day_trigger == False:
            raise Exception('Could not locate 1st, 2nd, or 3rd of current month when extracting cem spreadsheet data for current month')

    except Exception as error:
        # logging errors    
        raise SystemExit(error)
    


            