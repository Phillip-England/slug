def cems_for_slack_groupme(data):

    intro = 'Here is a breakdown of our current CEM scores'
    br = 'BREAK'
    line = '======================='

    cm_cem_intro = f"CURRENT MONTH - {data.cems.get('cm_number_of_surveys')} surveys"
    cm_osat = f"OSAT - {data.cems.get('cm_osat')}"
    cm_taste = f"Taste - {data.cems.get('cm_taste')}"
    cm_speed = f"Speed - {data.cems.get('cm_speed')}"
    cm_ace = f"ACE - {data.cems.get('cm_ace')}"  
    cm_clean = f"Cleanliness - {data.cems.get('cm_cleanliness')}"
    cm_accuracy = f"Accuracy - {data.cems.get('cm_accuracy')}"
    ndr_cem_intro = f"90 DAY ROLLING - {data.cems.get('ndr_number_of_surveys')} surveys"
    ndr_osat = f"OSAT - {data.cems.get('ndr_osat')}"
    ndr_taste = f"Taste - {data.cems.get('ndr_taste')}"
    ndr_speed = f"Speed - {data.cems.get('ndr_speed')}"
    ndr_ace = f"ACE - {data.cems.get('ndr_ace')}"
    ndr_clean = f"Cleanliness - {data.cems.get('ndr_cleanliness')}"
    ndr_accuracy = f"Accuracy - {data.cems.get('ndr_accuracy')}"
    ytd_cem_intro = f"YEAR TO DATE - {data.cems.get('ytd_number_of_surveys')} surveys"
    ytd_osat = f"OSAT - {data.cems.get('ytd_osat')}"
    ytd_taste = f"Taste - {data.cems.get('ytd_taste')}"
    ytd_speed = f"Speed - {data.cems.get('ytd_speed')}"
    ytd_ace = f"ACE - {data.cems.get('ytd_ace')}"
    ytd_clean = f"Cleanliness - {data.cems.get('ytd_cleanliness')}"
    ytd_accuracy = f"Accuracy - {data.cems.get('ytd_accuracy')}"

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
