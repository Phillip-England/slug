import PyPDF2
import os

def extract_cem_scores(self, config):

    if os.path.exists(config.cem_report_download_path_current_month) and os.path.exists(config.cem_report_download_path_ninty_day_rolling) and os.path.exists(config.cem_report_download_path_year_to_date):

        # pulling data from CEM score PDF
        cm_report = open(config.cem_report_download_path_current_month, 'rb')
        cm_reader = PyPDF2.PdfFileReader(cm_report)

        ndr_report = open(config.cem_report_download_path_ninty_day_rolling, 'rb')
        ndr_reader = PyPDF2.PdfFileReader(ndr_report)

        ytd_report = open(config.cem_report_download_path_year_to_date, 'rb')
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
                        self.cems['cm_osat'] = data[i+osat_steps]

                    if report_type == 'ndr':
                        self.cems['ndr_osat'] = data[i+osat_steps]

                    if report_type == 'ytd':
                        self.cems['ytd_osat'] = data[i+osat_steps]
                
                # scraping taste data
                # we can also scrape the amount of total surveys here as the number comes directly before the taste indicator
                if data[i] == taste_indicator:

                    if report_type == 'cm':
                        self.cems['cm_taste'] = data[i+taste_steps]
                        self.cems['cm_number_of_surveys'] = data[i - 1]

                    if report_type == 'ndr':
                        self.cems['ndr_taste'] = data[i+taste_steps]
                        self.cems['ndr_number_of_surveys'] = data[i - 1]

                    if report_type == 'ytd':
                        self.cems['ytd_taste'] = data[i+taste_steps]
                        self.cems['ytd_number_of_surveys'] = data[i - 1]

                # scraping fast service data
                if data[i] == fast_service_indicator:

                    if report_type == 'cm':
                        self.cems['cm_speed'] = data[i+fast_service_steps]

                    if report_type == 'ndr':
                        self.cems['ndr_speed'] = data[i+fast_service_steps]

                    if report_type == 'ytd':
                        self.cems['ytd_speed'] = data[i+fast_service_steps]

                # scraping ace data
                if data[i] == ace_indicator:

                    if report_type == 'cm':
                        self.cems['cm_ace'] = data[i+ace_steps]

                    if report_type == 'ndr':
                        self.cems['ndr_ace'] = data[i+ace_steps]

                    if report_type == 'ytd':
                        self.cems['ytd_ace'] = data[i+ace_steps]


                # scraping cleanliness data
                if data[i] == cleanliness_indicator:

                    if report_type == 'cm':
                        self.cems['cm_cleanliness'] = data[i+cleanliness_steps]

                    if report_type == 'ndr':
                        self.cems['ndr_cleanliness'] = data[i+cleanliness_steps]

                    if report_type == 'ytd':
                        self.cems['ytd_cleanliness'] = data[i+cleanliness_steps]


                # scraping accuracy data
                if data[i] == accuracy_indicator:

                    if report_type == 'cm':
                        self.cems['cm_accuracy'] = data[i+accuracy_steps]

                    if report_type == 'ndr':
                        self.cems['ndr_accuracy'] = data[i+accuracy_steps]

                    if report_type == 'ytd':
                        self.cems['ytd_accuracy'] = data[i+accuracy_steps]

    else:
        self.cem['cm_osat'] = 'N/A'
        self.cem['cm_taste'] = 'N/A'
        self.cem['cm_number_of_surveys'] = 'N/A'
        self.cem['cm_speed'] = 'N/A'
        self.cem['cm_ace'] = 'N/A'
        self.cem['cm_cleanliness'] = 'N/A'
        self.cem['cm_accuracy'] = 'N/A'
        self.cem['ndr_osat'] = 'N/A'
        self.cem['ndr_taste'] = 'N/A'
        self.cem['ndr_number_of_surveys'] = 'N/A'
        self.cem['ndr_speed'] = 'N/A'
        self.cem['ndr_ace'] = 'N/A'
        self.cem['ndr_cleanliness'] = 'N/A'
        self.cem['ndr_accuracy'] = 'N/A'
        self.cem['ytd_osat'] = 'N/A'
        self.cem['ytd_taste'] = 'N/A'
        self.cem['ytd_number_of_surveys'] = 'N/A'
        self.cem['ytd_speed'] = 'N/A'
        self.cem['ytd_ace'] = 'N/A'
        self.cem['ytd_cleanliness'] = 'N/A'
        self.cem['ytd_accuracy'] = 'N/A'
