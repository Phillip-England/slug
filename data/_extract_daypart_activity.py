import PyPDF2
import os

def extract_daypart_activity(self, config):

    #checking if our pdf exists. If our bot ran the report for a Sunday date or a date we are closed, it will not proceed
    if os.path.exists(config.daypart_activity_default_download_path):

        # pulling daypart activity report data from PDF
        report = open(config.daypart_activity_default_download_path, 'rb')
        reader = PyPDF2.PdfFileReader(report)

        # extracting data from the pdf and splitting the data by word                                     
        content = ''
        for page in range(reader.numPages):
            content = content + reader.getPage(page).extractText()
        data = content.split()

        # explanation of how the next section works. The pdf has been split into a list of words. As we iterate through the words of the pdf, we will encounter key words which help us identify that we are close to the data points we want to scrape. For example, when we encounter "Time:From", we know that we are getting close to all the information about the date the pdf is reffering to. Then, we can pluck out the following words and store them in a variable.

        #this method does risk the program breaking if the pdf changes structure in the future, we may need to implement some sort of failsafe for this method if we experience and issues.

        # date indicators
        date_indicator = 'Time:From'
        day_of_week_steps = 1
        month_steps = 2
        day_steps = 3
        year_steps = 4

        # breakfast indicators
        breakfast_indicator = 'Breakfast'
        breakfast_sales_steps = 4
        breakfast_transaction_steps = 6
        breakfast_check_average_steps = 5

        # lunch indicators
        lunch_indicator = 'Lunch'
        lunch_sales_steps = 4
        lunch_transaction_steps = 3
        lunch_check_average_steps = 5

        # midshift indicators
        midshift_indicator = 'Afternoon'
        midshift_sales_steps = 4
        midshift_transaction_steps = 3
        midshift_check_average_steps = 5

        # dinner indicators
        dinner_indicator = 'Dinner'
        dinner_sales_steps = 4
        dinner_transaction_steps = 3
        dinner_check_average_steps = 5

        # total indicators
        total_indicator = 'Totals:'
        total_sales_steps = 2
        total_transaction_steps = 1
        total_check_average_steps = 3

        # scraping the pdf for the data
        for i in range(len(data)):

            # data about the date
            if data[i] == date_indicator:
                day_of_week_untrimmed = data[i+day_of_week_steps]
                day_of_week = day_of_week_untrimmed.rstrip(day_of_week_untrimmed[-1])
                business_month = data[i+month_steps]
                business_day = data[i+day_steps]
                business_year = data[i+year_steps]
                self.daypart_activity['date'] = f'{business_month} {business_day} {business_year}'
                self.daypart_activity['day'] = day_of_week

            #breakfast sales data
            if data[i] == breakfast_indicator:
                self.daypart_activity['breakfast_sales'] = data[i + breakfast_sales_steps]
                self.daypart_activity['breakfast_transactions'] = data[i + breakfast_transaction_steps]
                self.daypart_activity['breakfast_check_average'] = data[i + breakfast_check_average_steps]

            #lunch sales data
            if data[i] == lunch_indicator:
                self.daypart_activity['lunch_sales'] = data[i + lunch_sales_steps]
                self.daypart_activity['lunch_transactions'] = data[i + lunch_transaction_steps]
                self.daypart_activity['lunch_check_average'] = data[i + lunch_check_average_steps]

            #midshift sales data
            if data[i] == midshift_indicator:
                self.daypart_activity['midshift_sales'] = data[i + midshift_sales_steps]
                self.daypart_activity['midshift_transactions'] = data[i + midshift_transaction_steps]
                self.daypart_activity['midshift_check_average'] = data[i + midshift_check_average_steps]

            #dinner sales data
            if data[i] == dinner_indicator:
                self.daypart_activity['dinner_sales'] = data[i + dinner_sales_steps]
                self.daypart_activity['dinner_transactions'] = data[i + dinner_transaction_steps]
                self.daypart_activity['dinner_check_average'] = data[i + dinner_check_average_steps]

            #daily totals
            if data[i] == total_indicator and data[i-1] == 'Report':
                self.daypart_activity['total_sales'] = data[i + total_sales_steps]
                self.daypart_activity['total_transactions'] = data[i + total_transaction_steps]
                self.daypart_activity['total_check_average'] = data[i + total_check_average_steps]

            
    
    else:
        
        self.daypart_activity['breakfast_sales'] = 'N/A'
        self.daypart_activity['breakfast_transactions'] = 'N/A'
        self.daypart_activity['breakfast_check_average'] = 'N/A'
        self.daypart_activity['lunch_sales'] = 'N/A'
        self.daypart_activity['lunch_transactions'] = 'N/A'
        self.daypart_activity['lunch_check_average'] = 'N/A'
        self.daypart_activity['midshift_sales'] = 'N/A'
        self.daypart_activity['midshift_transactions'] = 'N/A'
        self.daypart_activity['midshift_check_average'] = 'N/A'
        self.daypart_activity['dinner_sales'] = 'N/A'
        self.daypart_activity['dinner_transactions'] = 'N/A'
        self.daypart_activity['dinner_check_average'] = 'N/A'
        self.daypart_activity['total_sales'] = 'N/A'
        self.daypart_activity['total_transactions'] = 'N/A'
        self.daypart_activity['total_check_average'] = 'N/A'
