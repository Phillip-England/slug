def get_slack_message(self):

    intro = 'Good morning Directors! Here is a breakdown of current business results.'
    br = 'BREAK'
    line = '======================='

    yesterdays_date = f'{self.day}, {self.date}'
    yesterday_breakfast_sales = f'BREAKFAST - ${self.breakfast_sales} | {self.breakfast_check_average} check average | {self.breakfast_transactions} transactions'
    yesterday_lunch_sales = f'LUNCH - ${self.lunch_sales} | {self.lunch_check_average} check average | {self.lunch_transactions} transactions'
    yesterday_midshift_sales = f'MIDSHIFT - ${self.midshift_sales} | {self.midshift_check_average} check average | {self.midshift_transactions} transactions'
    yesterday_dinner_sales = f'DINNER - ${self.dinner_sales} | {self.dinner_check_average} check average | {self.dinner_transactions} transactions'
    yesterday_total_sales = f'TOTAL - ${self.total_sales} | {self.total_check_average} check average | {self.total_transactions} transactions'

    cm_cem_intro = f'CURRENT MONTH - {self.cm_number_of_surveys} surveys',
    cm_osat = f'OSAT - {self.cm_osat}'
    cm_taste = f'Taste - {self.cm_taste}'
    cm_speed = f'Speed - {self.cm_speed}'
    cm_ace = f'ACE - {self.cm_ace}'
    cm_clean = f'Cleanliness - {self.cm_cleanliness}'
    cm_accuracy = f'Accuracy - {self.cm_accuracy}'
    ndr_cem_intro = f'90 DAY ROLLING - {self.ndr_number_of_surveys} surveys'
    ndr_osat = f'OSAT - {self.ndr_osat}'
    ndr_taste = f'Taste - {self.ndr_taste}'
    ndr_speed = f'Speed - {self.ndr_speed}'
    ndr_ace = f'ACE - {self.ndr_ace}'
    ndr_clean = f'Cleanliness - {self.ndr_cleanliness}'
    ndr_accuracy = f'Accuracy - {self.ndr_accuracy}'
    ytd_cem_intro = f'YEAR TO DATE - {self.ytd_number_of_surveys} surveys'
    ytd_osat = f'OSAT - {self.ytd_osat}'
    ytd_taste = f'Taste - {self.ytd_taste}'
    ytd_speed = f'Speed - {self.ytd_speed}'
    ytd_ace = f'ACE - {self.ytd_ace}'
    ytd_clean = f'Cleanliness - {self.ytd_cleanliness}'
    ytd_accuracy = f'Accuracy - {self.ytd_accuracy}'


    message_list_without_yesterdays_sales = [
        intro,
        br,
        br,
        line,
        br,
        cm_cem_intro,
        br,
        cm_osat,
        br,
        cm_taste,
        br,
        cm_speed,
        br,
        cm_ace,
        br,
        cm_clean,
        br,
        cm_accuracy,
        br,
        br,
        line,
        br,
        ndr_cem_intro,
        br,
        ndr_osat,
        br,
        ndr_taste,
        br,
        ndr_speed,
        br,
        ndr_ace,
        br,
        ndr_clean,
        br,
        ndr_accuracy,
        br,
        br,
        line,
        br,
        ytd_cem_intro,
        br,
        ytd_osat,
        br,
        ytd_taste,
        br,
        ytd_speed,
        br,
        ytd_ace,
        br,
        ytd_clean,
        br,
        ytd_accuracy,
    ]


    message_list_with_yesterdays_sales = [
        intro,
        br,
        br,
        line,
        br,
        yesterdays_date,
        br,
        yesterday_breakfast_sales,
        br,
        yesterday_lunch_sales,
        br,
        yesterday_midshift_sales,
        br,
        yesterday_dinner_sales,
        br,
        yesterday_total_sales,
        br,
        br,
        line,
        br,
        cm_cem_intro,
        br,
        cm_osat,
        br,
        cm_taste,
        br,
        cm_speed,
        br,
        cm_ace,
        br,
        cm_clean,
        br,
        cm_accuracy,
        br,
        br,
        line,
        br,
        ndr_cem_intro,
        br,
        ndr_osat,
        br,
        ndr_taste,
        br,
        ndr_speed,
        br,
        ndr_ace,
        br,
        ndr_clean,
        br,
        ndr_accuracy,
        br,
        br,
        line,
        br,
        ytd_cem_intro,
        br,
        ytd_osat,
        br,
        ytd_taste,
        br,
        ytd_speed,
        br,
        ytd_ace,
        br,
        ytd_clean,
        br,
        ytd_accuracy,
    ]

    if self.found_yesterday_daypart_activity == False and self.found_yesterday_sales_activity == False:
        return message_list_without_yesterdays_sales
    else:
        return message_list_with_yesterdays_sales
