import PyPDF2

def extract_cem_spreadsheet_data(engine):

    report = open(engine.config.cem_spreadsheet_download_path, 'rb')
    reader = PyPDF2.PdfFileReader(report)

    content = ''
    for page in range(reader.numPages):
        content = content + reader.getPage(page).extractText()

    data = content.split()

    # okay, we are collecting scores from a given date
    # we need to set up Current Month, 90 day rolling, and current year
    # our sheet is formatted in the x/x/xxxx format

    # 90 day rolling
    ninty_days_ago_date_crude = engine.date.get_past_date(90)
    ninty_days_ago_date = engine.date.format_date(ninty_days_ago_date_crude, 'x/x/xxxx')

    # first of the month
    first_of_month_date_crude = engine.date.first_of_month()
    first_of_month_date = engine.date.format_date(first_of_month_date_crude, 'x/x/xxxx')

    print(ninty_days_ago_date)
    print(first_of_month_date)


    for i in range(len(data)):
        pass
            