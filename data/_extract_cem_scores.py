import PyPDF2
import datetime

def extract_cem_scores(engine):

    try:

        # pulling data from CEM score PDF
        cm_report = open(engine.config.cem_report_download_path_current_month, 'rb')
        cm_reader = PyPDF2.PdfFileReader(cm_report)

        ndr_report = open(engine.config.cem_report_download_path_ninty_day_rolling, 'rb')
        ndr_reader = PyPDF2.PdfFileReader(ndr_report)

        ytd_report = open(engine.config.cem_report_download_path_year_to_date, 'rb')
        ytd_reader = PyPDF2.PdfFileReader(ytd_report)

        # extracting the data and splitting by word
        cm_content = ''
        ndr_content = ''
        ytd_content = ''

        for page in range(cm_reader.numPages):
            cm_content = cm_content + cm_reader.getPage(page).extract_text()

        for page in range(ndr_reader.numPages):
            ndr_content = ndr_content + ndr_reader.getPage(page).extract_text()

        for page in range(ytd_reader.numPages):
            ytd_content = ytd_content + ytd_reader.getPage(page).extract_text()


        cm_data = cm_content.split()
        ndr_data = ndr_content.split()
        ytd_data = ytd_content.split()

        # setting up loop keywords
        report_types = ['cm', 'ndr', 'ytd']

        #important variables for extrating data
        osat_indicator = 'Satisfaction' # only appears once
        osat_steps = 10
        taste_indicator = 'ResponsesTaste' # only appears once
        taste_steps = 10
        fast_service_indicator = 'Service' # only appears once
        fast_service_steps = 10
        ace_indicator = 'ResponsesAttentive/Courteous' #only appears once
        ace_steps = 10
        cleanliness_indicator = 'Combined' # only appears once
        cleanliness_steps = 10
        accuracy_indicator = 'Accuracy' # only appears once
        accuracy_steps = 9

        # variables to store data from pdf
        number_of_surveys = str
        osat = str
        taste = str
        speed = str
        clean = str
        accuracy = str
        ace = str

        for report_type in report_types:

            if report_type == 'cm':
                data = cm_data

            if report_type == 'ndr':
                data = ndr_data

            if report_type == 'ytd':
                data = ytd_data


            # looping through the words of the pdf to scrape data
            for i in range(len(data)):

                # scraping OSAT data
                if data[i] == osat_indicator:
                    # the score is found 10 steps after the indicator

                    if report_type == 'cm':
                        engine.data.cm_osat = data[i+osat_steps]

                    if report_type == 'ndr':
                        engine.data.ndr_osat = data[i+osat_steps]

                    if report_type == 'ytd':
                        engine.data.ytd_osat = data[i+osat_steps]
                
                # scraping taste data
                # we can also scrape the amount of total surveys here as the number comes directly before the taste indicator
                if data[i] == taste_indicator:

                    if report_type == 'cm':
                        engine.data.cm_taste = data[i+taste_steps]
                        engine.data.cm_number_of_surveys = data[i - 1]

                    if report_type == 'ndr':
                        engine.data.ndr_taste = data[i+taste_steps]
                        engine.data.ndr_number_of_surveys = data[i - 1]

                    if report_type == 'ytd':
                        engine.data.ytd_taste = data[i+taste_steps]
                        engine.data.ytd_number_of_surveys = data[i - 1]



                # scraping fast service data
                if data[i] == fast_service_indicator:

                    if report_type == 'cm':
                        engine.data.cm_speed = data[i+fast_service_steps]

                    if report_type == 'ndr':
                        engine.data.ndr_speed = data[i+fast_service_steps]

                    if report_type == 'ytd':
                        engine.data.ytd_speed = data[i+fast_service_steps]


                # scraping ace data
                if data[i] == ace_indicator:

                    if report_type == 'cm':
                        engine.data.cm_ace = data[i+ace_steps]

                    if report_type == 'ndr':
                        engine.data.ndr_ace = data[i+ace_steps]

                    if report_type == 'ytd':
                        engine.data.ytd_ace = data[i+ace_steps]


                # scraping cleanliness data
                if data[i] == cleanliness_indicator:

                    if report_type == 'cm':
                        engine.data.cm_cleanliness = data[i+cleanliness_steps]

                    if report_type == 'ndr':
                        engine.data.ndr_cleanliness = data[i+cleanliness_steps]

                    if report_type == 'ytd':
                        engine.data.ytd_cleanliness = data[i+cleanliness_steps]


                # scraping accuracy data
                if data[i] == accuracy_indicator:

                    if report_type == 'cm':
                        engine.data.cm_accuracy = data[i+accuracy_steps]

                    if report_type == 'ndr':
                        engine.data.ndr_accuracy = data[i+accuracy_steps]

                    if report_type == 'ytd':
                        engine.data.ytd_accuracy = data[i+accuracy_steps]


        # checking all our datapoints and filling in n/a if it was not found

        datapoints = [
            'cm_osat',
            'ndr_osat',
            'ytd_osat',
            'cm_taste',
            'ndr_taste',
            'ytd_taste',
            'cm_speed',
            'ndr_speed',
            'ytd_speed',
            'cm_ace',
            'ndr_ace',
            'ytd_ace',
            'cm_cleanliness',
            'ndr_cleanliness',
            'ytd_cleanliness',
            'cm_accuracy',
            'ndr_accuracy',
            'ytd_accuracy',
            'cm_number_of_surveys',
            'ndr_number_of_surveys',
            'ytd_number_of_surveys',
        ]

        for datapoint in datapoints:
            if hasattr(engine.data, datapoint) == False:
                setattr(engine.data, datapoint, 'N/A')

    except Exception as error:
        engine.driver.close()
        raise SystemExit(error)
