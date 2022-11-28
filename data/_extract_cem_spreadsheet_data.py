import PyPDF2

def extract_cem_spreadsheet_data(engine):

    # we want to do a couple things here. First, we need to get the current month.
    past_date = engine.date.get_past_date(90)
    print(past_date)

    
    # report = open(engine.config.cem_spreadsheet_download_path, 'rb')
    # reader = PyPDF2.PdfFileReader(report)

    # content = ''
    # for page in range(reader.numPages):
    #     content = content + reader.getPage(page).extractText()
    
    # data = content.split()

    # for i in range(len(data)):
    #     pass
        # print(data[i])