import PyPDF2
import os

def extract_cem_scores(engine):

    if os.path.exists(engine.config.cem_report_download_path_current_month) and os.path.exists(engine.config.cem_report_download_path_ninty_day_rolling) and os.path.exists(engine.config.cem_report_download_path_year_to_date):

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
                        engine.data.cems['cm_osat'] = data[i+osat_steps]

                    if report_type == 'ndr':
                        engine.data.cems['ndr_osat'] = data[i+osat_steps]

                    if report_type == 'ytd':
                        engine.data.cems['ytd_osat'] = data[i+osat_steps]
                
                # scraping taste data
                # we can also scrape the amount of total surveys here as the number comes directly before the taste indicator
                if data[i] == taste_indicator:

                    if report_type == 'cm':
                        engine.data.cems['cm_taste'] = data[i+taste_steps]
                        engine.data.cems['cm_number_of_surveys'] = data[i - 1]

                    if report_type == 'ndr':
                        engine.data.cems['ndr_taste'] = data[i+taste_steps]
                        engine.data.cems['ndr_number_of_surveys'] = data[i - 1]

                    if report_type == 'ytd':
                        engine.data.cems['ytd_taste'] = data[i+taste_steps]
                        engine.data.cems['ytd_number_of_surveys'] = data[i - 1]

                # scraping fast service data
                if data[i] == fast_service_indicator:

                    if report_type == 'cm':
                        engine.data.cems['cm_speed'] = data[i+fast_service_steps]

                    if report_type == 'ndr':
                        engine.data.cems['ndr_speed'] = data[i+fast_service_steps]

                    if report_type == 'ytd':
                        engine.data.cems['ytd_speed'] = data[i+fast_service_steps]

                # scraping ace data
                if data[i] == ace_indicator:

                    if report_type == 'cm':
                        engine.data.cems['cm_ace'] = data[i+ace_steps]

                    if report_type == 'ndr':
                        engine.data.cems['ndr_ace'] = data[i+ace_steps]

                    if report_type == 'ytd':
                        engine.data.cems['ytd_ace'] = data[i+ace_steps]


                # scraping cleanliness data
                if data[i] == cleanliness_indicator:

                    if report_type == 'cm':
                        engine.data.cems['cm_cleanliness'] = data[i+cleanliness_steps]

                    if report_type == 'ndr':
                        engine.data.cems['ndr_cleanliness'] = data[i+cleanliness_steps]

                    if report_type == 'ytd':
                        engine.data.cems['ytd_cleanliness'] = data[i+cleanliness_steps]


                # scraping accuracy data
                if data[i] == accuracy_indicator:

                    if report_type == 'cm':
                        engine.data.cems['cm_accuracy'] = data[i+accuracy_steps]

                    if report_type == 'ndr':
                        engine.data.cems['ndr_accuracy'] = data[i+accuracy_steps]

                    if report_type == 'ytd':
                        engine.data.cems['ytd_accuracy'] = data[i+accuracy_steps]

    else:
        engine.data.cem['cm_osat'] = 'N/A'
        engine.data.cem['cm_taste'] = 'N/A'
        engine.data.cem['cm_number_of_surveys'] = 'N/A'
        engine.data.cem['cm_speed'] = 'N/A'
        engine.data.cem['cm_ace'] = 'N/A'
        engine.data.cem['cm_cleanliness'] = 'N/A'
        engine.data.cem['cm_accuracy'] = 'N/A'
        engine.data.cem['ndr_osat'] = 'N/A'
        engine.data.cem['ndr_taste'] = 'N/A'
        engine.data.cem['ndr_number_of_surveys'] = 'N/A'
        engine.data.cem['ndr_speed'] = 'N/A'
        engine.data.cem['ndr_ace'] = 'N/A'
        engine.data.cem['ndr_cleanliness'] = 'N/A'
        engine.data.cem['ndr_accuracy'] = 'N/A'
        engine.data.cem['ytd_osat'] = 'N/A'
        engine.data.cem['ytd_taste'] = 'N/A'
        engine.data.cem['ytd_number_of_surveys'] = 'N/A'
        engine.data.cem['ytd_speed'] = 'N/A'
        engine.data.cem['ytd_ace'] = 'N/A'
        engine.data.cem['ytd_cleanliness'] = 'N/A'
        engine.data.cem['ytd_accuracy'] = 'N/A'
