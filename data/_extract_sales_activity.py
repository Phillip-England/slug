import PyPDF2
import os

def extract_sales_activity(self, config):

    if os.path.exists(config.sales_activity_default_download_path):

        # pulling sales activity pdf
        report = open(config.sales_activity_default_download_path, 'rb')
        reader = PyPDF2.PdfFileReader(report)

        # extracting each word from the pdf
        content = ''
        for page in range(reader.numPages):
            content = content + reader.getPage(page).extractText()
        data = content.split()

        # I reverse the list because I want the last instance of each destinations sales. This will contain the total days sales for each destination
        data.reverse()

        # these data indicators will help us pinpoint the data we need from the report

        # carryout indicators
        carryout_indicator = 'CARRY'
        carryout_steps = 5
        carryout_sales = str

        # cfa delivery indicators
        # the word "CFA" is only found in CFA delivery
        cfa_delivery_indicator = 'CFA'
        cfa_delivery_steps = 4
        cfa_delivery_sales = str

        # curbside indicators
        # we currently have curbside off, so this will default to 0
        curbside_sales = str

        # delivery indicators
        delivery_indicator = 'DELIVERY'
        delivery_steps = 4
        delivery_sales = str

        # dine-in indicators
        dine_in_indicator = 'IN'
        dine_in_steps = 4
        dine_in_sales = str

        # drive-thru indicators
        drive_thru_indicator = 'THRU'
        drive_thru_steps = 4
        drive_thru_sales = str

        # mobile carryout indicators
        m_carryout_indicator = 'M-'
        m_carryout_steps = 4
        m_carryout_sales = str

        # mobile dine in
        m_dine_in_indicator = 'M-DINEIN'
        m_dine_in_steps = 4
        m_dine_in_sales = str

        # mobile drive thru indicators
        m_drive_thru_indicator = 'M-DRIVE-'
        m_drive_thru_steps = 4
        m_drive_thru_sales = str

        # on demand indicators
        on_demand_indicator = 'DEMAND'
        on_demand_steps = 4
        on_demand_sales = str

        # pickup indicators
        pickup_indicators = 'PICKUP'
        pickup_steps = 4
        pickup_sales = str

        # explanation of how the data is extracted in this instance.


        for i in range(len(data)):
            
            # carryout sales extraction
            if data[i] == carryout_indicator and carryout_sales == str:
                carryout_sales = data[i-carryout_steps]

            # cfa delivery extraction
            if data[i] == cfa_delivery_indicator and cfa_delivery_sales == str:
                cfa_delivery_sales = data[i-cfa_delivery_steps]

            # delivery extraction
            if data[i] == delivery_indicator and delivery_sales == str:
                delivery_sales = data[i-delivery_steps]

            # dine in extraction
            if data[i] == dine_in_indicator and dine_in_sales == str:
                dine_in_sales = data[i-dine_in_steps]

            # drive thru extraction
            if data[i] == drive_thru_indicator and drive_thru_sales == str:
                drive_thru_sales = data[i-drive_thru_steps]

            # mobile carryout extraction
            if data[i] == m_carryout_indicator and m_carryout_sales == str:
                m_carryout_sales = data[i-m_carryout_steps]

            # mobile dine in extraction
            if data[i] == m_dine_in_indicator and m_dine_in_sales == str:
                m_dine_in_sales = data[i-m_dine_in_steps]

            # mobile drive thru extraction
            if data[i] == m_drive_thru_indicator and m_drive_thru_sales == str:
                m_drive_thru_sales = data[i-m_drive_thru_steps]

            # on demand extraction
            if data[i] == on_demand_indicator and on_demand_sales == str:
                on_demand_sales = data[i-on_demand_steps]

            # pickup extraction
            if data[i] == pickup_indicators and pickup_sales == str:
                pickup_sales = data[i-pickup_steps]

        # final check to see if certain categories were exclued
        if carryout_sales == str: carryout_sales = str(0)
        if cfa_delivery_sales == str: cfa_delivery_sales = str(0)
        if curbside_sales == str: curbside_sales = str(0)
        if delivery_sales == str: delivery_sales = str(0)
        if dine_in_sales == str: dine_in_sales = str(0)
        if drive_thru_sales == str: drive_thru_sales = str(0)
        if m_carryout_sales == str: m_carryout_sales = str(0)
        if m_dine_in_sales == str: m_dine_in_sales = str(0)
        if m_drive_thru_sales == str: m_drive_thru_sales = str(0)
        if on_demand_sales == str: on_demand_sales = str(0)
        if pickup_sales == str: pickup_sales = str(0)

        self.sales_activity['carryout_sales'] = carryout_sales
        self.sales_activity['cfa_delivery_sales'] = cfa_delivery_sales
        self.sales_activity['curbside_sales'] = curbside_sales
        self.sales_activity['delivery_sales'] = delivery_sales
        self.sales_activity['dine_in_sales'] = dine_in_sales
        self.sales_activity['drive_thru_sales'] = drive_thru_sales
        self.sales_activity['m_carryout_sales'] = m_carryout_sales
        self.sales_activity['m_dine_in_sales'] = m_dine_in_sales
        self.sales_activity['m_drive_thru_sales'] = m_drive_thru_sales
        self.sales_activity['on_demand_sales'] = on_demand_sales
        self.sales_activity['pickup_sales'] = pickup_sales
    
    else:
        self.sales_activity['carryout_sales'] = 'N/A'
        self.sales_activity['cfa_delivery_sales'] = 'N/A'
        self.sales_activity['curbside_sales'] = 'N/A'
        self.sales_activity['delivery_sales'] = 'N/A'
        self.sales_activity['dine_in_sales'] = 'N/A'
        self.sales_activity['drive_thru_sales'] = 'N/A'
        self.sales_activity['m_carryout_sales'] = 'N/A'
        self.sales_activity['m_dine_in_sales'] = 'N/A'
        self.sales_activity['m_drive_thru_sales'] = 'N/A'
        self.sales_activity['on_demand_sales'] = 'N/A'
        self.sales_activity['pickup_sales'] = 'N/A'
