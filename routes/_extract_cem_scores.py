import PyPDF2

def extract_cem_scores(self, engine):

    # pulling data from CEM score PDF
    report = open(engine.config.cem_report_download_path, 'rb')
    reader = PyPDF2.PdfFileReader(report)

    # extracting the data and splitting by word
    content = ''
    for page in range(reader.numPages):
        content = content + reader.getPage(page).extract_text()
    data = content.split()

    #important variables for extrating data
    osat_indicator = 'Satisfaction' # only appears once
    taste_indicator = 'ResponsesTaste' # only appears once
    fast_service_indicator = 'Service' # only appears once
    ace_indicator = 'ResponsesAttentive/Courteous' #only appears once
    cleanliness_indicator = 'Combined' # only appears once
    accuracy_indicator = 'Accuracy' # only appears once

    # variables to store data from pdf
    number_of_surveys = str
    osat = str
    taste = str
    speed = str
    clean = str
    accuracy = str
    ace = str

    # looping through the words of the pdf to scrape data
    for i in range(len(data)):

        # scraping OSAT data
        if data[i] == osat_indicator:
            # the score is found 10 steps after the indicator
            osat = data[i+10]
        
        # scraping taste data
        # we can also scrape the amount of total surveys here as the number comes directly before the taste indicator
        if data[i] == taste_indicator:
            # score is found 10 words after the indicator
            taste = data[i+10]
            #number of surveys is found directly before the indicator
            number_of_surveys = data[i - 1]


        # scraping fast service data
        if data[i] == fast_service_indicator:
            #score is found 10 words after the indicator
            speed = data[i+10]

        # scraping ace data
        if data[i] == ace_indicator:
            # score is found 10 words after the indicator
            ace = data[i+10]

        # scraping cleanliness data
        if data[i] == cleanliness_indicator:
            # score is found 10 words after the indicator
            clean = data[i+10]

        # scraping accuracy data
        if data[i] == accuracy_indicator:
            # score is found 10 words after the indicator
            accuracy = data[i+9]

        
    
        # print(data[i])
    
    cem_data_dictionary = {
        'number_of_surveys': number_of_surveys,
        'osat': osat,
        'taste': taste,
        'speed': speed,
        'ace': ace,
        'cleanliness': clean,
        'accuracy': accuracy
    }

    engine.data.set_current_month_cem_data(cem_data_dictionary)
