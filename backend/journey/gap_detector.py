def detect_gaps(journey, pregnancy, today):

    gaps = []

    for milestone in journey["verification_needed"]:

        if (
            milestone["event_type"] == "ANC_VISIT"
            and pregnancy.last_menstrual_period is None
        ):
            message = "Pregnancy timing could not be determined — verification needed."

        elif (
            milestone["event_type"] == "DELIVERY"
            and pregnancy.expected_delivery_date is not None
            and today > pregnancy.expected_delivery_date
        ):
            message = "Expected delivery date has passed and no delivery record is available — verification needed."

        elif milestone["event_type"] == "POSTNATAL_VISIT":
            message = "Postnatal follow-up period has passed and no postnatal record is available — verification needed."

        else:
            message = f"No record found for {milestone['name']} — verification needed."

        gaps.append({
            "milestone": milestone["name"],
            "event_type": milestone["event_type"],
            "message": message
        })

    return gaps