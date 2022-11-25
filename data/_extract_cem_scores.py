import PyPDF2

def extract_cem_scores(engine):

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

    # looping through the words of the pdf to scrape data
    for i in range(len(data)):

        # scraping OSAT data
        if data[i] == osat_indicator:
            # the score is found 10 steps after the indicator
            engine.data.osat = data[i+osat_steps]
        
        # scraping taste data
        # we can also scrape the amount of total surveys here as the number comes directly before the taste indicator
        if data[i] == taste_indicator:
            # score is found 10 words after the indicator
            engine.data.taste = data[i+taste_steps]
            #number of surveys is found directly before the indicator
            engine.data.number_of_surveys = data[i - 1]


        # scraping fast service data
        if data[i] == fast_service_indicator:
            #score is found 10 words after the indicator
            engine.data.speed = data[i+fast_service_steps]

        # scraping ace data
        if data[i] == ace_indicator:
            # score is found 10 words after the indicator
            engine.data.ace = data[i+ace_steps]

        # scraping cleanliness data
        if data[i] == cleanliness_indicator:
            # score is found 10 words after the indicator
            engine.data.cleanliness = data[i+cleanliness_steps]

        # scraping accuracy data
        if data[i] == accuracy_indicator:
            # score is found 10 words after the indicator
            engine.data.accuracy = data[i+accuracy_steps]

