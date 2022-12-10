import os
import PyPDF2

def extract_deferred_orders(engine):
    
    #checking if our pdf exists. If our bot ran the report for a Sunday date or a date we are closed, it will not proceed
    if os.path.exists(engine.config.deferred_order_default_download_path):

        # pulling daypart activity report data from PDF
        report = open(engine.config.deferred_order_default_download_path, 'rb')
        reader = PyPDF2.PdfFileReader(report)

        # extracting data from the pdf and splitting the data by word                                     
        content = ''
        for page in range(reader.numPages):
            content = content + reader.getPage(page).extractText()
        data = content.split()

        # we are going to use dollar amounts as our indicator. The first dollar sign in the report will trigger us to start searching for data using steps

        pickup_orders = []
        delivery_orders = []
        destination_step = 1
        order_time_step = 5
        order_am_or_pm_step = 6

        for i in range(len(data)):

            if data[i][0] == '$':

                cost = data[i]
                destination = data[i+destination_step]
                time = f'{data[i+order_time_step]}{data[i+order_am_or_pm_step]}'


                if destination == 'DELIVERY':
                    delivery_orders.append(f'{destination} {time} {cost}')

                if destination == 'PICKUP':
                    pickup_orders.append(f'{destination} {time} {cost}')

        return (pickup_orders, delivery_orders)