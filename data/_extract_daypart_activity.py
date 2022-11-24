import PyPDF2

def extract_daypart_activity(engine):

    # pulling daypart activity report data from PDF
    report = open(engine.config.daypart_activity_default_download_path, 'rb')
    reader = PyPDF2.PdfFileReader(report)

    # extracting data from the pdf and splitting the data by word                                     
    content = ''
    for page in range(reader.numPages):
        content = content + reader.getPage(page).extractText()
    data = content.split()

    # setting up variables for data points
    business_date = str
    day_of_week = str
    breakfast_data = []
    lunch_data = []
    mid_data = []
    dinner_data = []
    total_data = []
    number_of_data_points = 6

    # explanation of how the next section works. The pdf has been split into a list of words. As we iterate through the words of the pdf, we will encounter key words which help us identify that we are close to the data points we want to scrape. For example, when we encounter "Time:From", we know that we are getting close to all the information about the date the pdf is reffering to. Then, we can pluck out the following words and store them in a variable.

    #this method does risk the program breaking if the pdf changes structure in the future, we may need to implement some sort of failsafe for this method if we experience and issues.

    # scraping the pdf for the data
    for i in range(len(data)):

        # data about the date
        if data[i] == 'Time:From':
            day_of_week_untrimmed = data[i+1]
            day_of_week = day_of_week_untrimmed.rstrip(day_of_week_untrimmed[-1])
            business_month = data[i+2]
            business_day = data[i+3]
            business_year = data[i+4]

        #breakfast sales data
        if data[i] == 'Breakfast':
            for x in range(number_of_data_points):
                breakfast_data.append(data[i+x])

        #lunch sales data
        if data[i] == 'Lunch':
            for x in range(number_of_data_points):
                lunch_data.append(data[i+x])

        #midshift sales data
        if data[i] == 'Afternoon':
            for x in range(number_of_data_points):
                mid_data.append(data[i+x])

        #dinner sales data
        if data[i] == 'Dinner':
            for x in range(number_of_data_points):
                dinner_data.append(data[i+x])

        #daily totals
        if data[i] == 'Totals:' and data[i-1] == 'Report':
            for x in range(number_of_data_points):
                total_data.append(data[i+x])
    
    # taking the data out of the lists and storing them in solid variables
    engine.data.date = f'{business_month} {business_day} {business_year}'
    engine.data.day = day_of_week
    engine.data.breakfast_sales = breakfast_data[4]
    engine.data.breakfast_transactions = breakfast_data[3]
    engine.data.breakfast_check_average = breakfast_data[5]
    engine.data.lunch_sales = lunch_data[4]
    engine.data.lunch_transactions = lunch_data[3]
    engine.data.lunch_check_average = lunch_data[5]
    engine.data.midshift_sales = mid_data[4]
    engine.data.midshift_transactions = mid_data[3]
    engine.data.midshift_check_average = mid_data[5]
    engine.data.dinner_sales = dinner_data[4]
    engine.data.dinner_transactions = dinner_data[3]
    engine.data.dinner_check_average = dinner_data[5]
    engine.data.total_sales = total_data[2]
    engine.data.total_transactions = total_data[1]
    engine.data.total_check_average = total_data[3]