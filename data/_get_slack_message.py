import os

def get_slack_message(engine):

    intro = 'Good morning Directors! Here is a breakdown of current business results.'
    br = 'BREAK'
    line = '======================='

    cm_cem_intro = f'CURRENT MONTH - {engine.data.cm_number_of_surveys} surveys',
    cm_osat = f'OSAT - {engine.data.cm_osat}'
    cm_taste = f'Taste - {engine.data.cm_taste}'
    cm_speed = f'Speed - {engine.data.cm_speed}'
    cm_ace = f'ACE - {engine.data.cm_ace}'
    cm_clean = f'Cleanliness - {engine.data.cm_cleanliness}'
    cm_accuracy = f'Accuracy - {engine.data.cm_accuracy}'
    ndr_cem_intro = f'90 DAY ROLLING - {engine.data.ndr_number_of_surveys} surveys'
    ndr_osat = f'OSAT - {engine.data.ndr_osat}'
    ndr_taste = f'Taste - {engine.data.ndr_taste}'
    ndr_speed = f'Speed - {engine.data.ndr_speed}'
    ndr_ace = f'ACE - {engine.data.ndr_ace}'
    ndr_clean = f'Cleanliness - {engine.data.ndr_cleanliness}'
    ndr_accuracy = f'Accuracy - {engine.data.ndr_accuracy}'
    ytd_cem_intro = f'YEAR TO DATE - {engine.data.ytd_number_of_surveys} surveys'
    ytd_osat = f'OSAT - {engine.data.ytd_osat}'
    ytd_taste = f'Taste - {engine.data.ytd_taste}'
    ytd_speed = f'Speed - {engine.data.ytd_speed}'
    ytd_ace = f'ACE - {engine.data.ytd_ace}'
    ytd_clean = f'Cleanliness - {engine.data.ytd_cleanliness}'
    ytd_accuracy = f'Accuracy - {engine.data.ytd_accuracy}'

    if os.path.exists(engine.config.sales_activity_default_download_path) and os.path.exists(engine.config.daypart_activity_default_download_path):

        yesterdays_date = f'{engine.data.day}, {engine.data.date}'
        yesterday_breakfast_sales = f'BREAKFAST - ${engine.data.breakfast_sales} | {engine.data.breakfast_check_average} check average | {engine.data.breakfast_transactions} transactions'
        yesterday_lunch_sales = f'LUNCH - ${engine.data.lunch_sales} | {engine.data.lunch_check_average} check average | {engine.data.lunch_transactions} transactions'
        yesterday_midshift_sales = f'MIDSHIFT - ${engine.data.midshift_sales} | {engine.data.midshift_check_average} check average | {engine.data.midshift_transactions} transactions'
        yesterday_dinner_sales = f'DINNER - ${engine.data.dinner_sales} | {engine.data.dinner_check_average} check average | {engine.data.dinner_transactions} transactions'
        yesterday_total_sales = f'TOTAL - ${engine.data.total_sales} | {engine.data.total_check_average} check average | {engine.data.total_transactions} transactions'

        message_list = [
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
    else:
        message_list = [
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

    return message_list
