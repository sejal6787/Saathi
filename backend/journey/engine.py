from journey.milestones import MILESTONES
from datetime import date, timedelta


def get_milestone_stage(milestone):
    return milestone["stage"]


def get_milestone_status(
    milestone,
    pregnancy_age_weeks,
    pregnancy=None,
    today=None
):
    timing = milestone["timing"]

    if timing is None:
        return "verification_needed"

    if pregnancy_age_weeks is None:
        return "verification_needed"

    start_week = timing["start_week"]
    end_week = timing["end_week"]

    if pregnancy_age_weeks < start_week:
        return "upcoming"

    if end_week is None:
        if pregnancy is not None and milestone["name"] == "ANC Visit 4":

            if pregnancy.expected_delivery_date is None:
                return "verification_needed"
            
            if today <= pregnancy.expected_delivery_date:
                return "current"
            
            return "verification_needed"

        return "current"

    if pregnancy_age_weeks <= end_week:
        return "current"

    return "verification_needed"


def build_journey(events, pregnancy, today=None):

    if today is None:
        today = date.today()

    if pregnancy.last_menstrual_period is not None:
        pregnancy_age_days = (
                today - pregnancy.last_menstrual_period
            ).days
        pregnancy_age_weeks = pregnancy_age_days // 7
    else:
        pregnancy_age_weeks = None

    completed = []
    upcoming = []
    verification_needed = []
    current = []

    recorded_event_types = {
        event.event_type
        for event in events
    }

    anc_visit_count = sum(
        1
        for event in events
        if event.event_type == "ANC_VISIT"
    )

    delivery_event = next(
        (
            event
            for event in events
            if event.event_type == "DELIVERY"
        ),
        None
    )

    delivery_date = (
        delivery_event.event_date
        if delivery_event is not None
        else None
    )

    for milestone in MILESTONES:

        stage = get_milestone_stage(milestone)

        # ANC Visit handling
        if milestone["event_type"] == "ANC_VISIT":

            anc_number = int(
                milestone["name"].split()[-1]
            )

            if anc_visit_count >= anc_number:
                completed.append(milestone)

            else:
                status = get_milestone_status(
                    milestone,
                    pregnancy_age_weeks,
                    pregnancy,
                    today
                )

                if status == "current":
                    current.append(milestone)

                elif status == "upcoming":
                    upcoming.append(milestone)

                elif status == "verification_needed":
                    verification_needed.append(milestone)

        # Delivery handling
        elif milestone["event_type"] == "DELIVERY":

            if "DELIVERY" in recorded_event_types:
                completed.append(milestone)

            elif pregnancy.expected_delivery_date is None:
                verification_needed.append(milestone)

            elif today < pregnancy.expected_delivery_date:
                upcoming.append(milestone)

            else:
                verification_needed.append(milestone)

        # Postnatal Visit handling
        elif milestone["event_type"] == "POSTNATAL_VISIT":

            if "POSTNATAL_VISIT" in recorded_event_types:
                completed.append(milestone)

            elif delivery_date is None:
                upcoming.append(milestone)

            elif today <= delivery_date + timedelta(days=42):
                current.append(milestone)

            else:
                verification_needed.append(milestone)

        # Other milestones
        elif milestone["event_type"] in recorded_event_types:
            completed.append(milestone)

        else:
            status = get_milestone_status(
                milestone,
                pregnancy_age_weeks,
                pregnancy,
                today
            )

            if status == "current":
                current.append(milestone)

            elif status == "upcoming":
                upcoming.append(milestone)

            elif status == "verification_needed":
                verification_needed.append(milestone)

    return {
        "completed": completed,
        "current": current,
        "upcoming": upcoming,
        "verification_needed": verification_needed
    }


def get_next_milestone(journey):

    status_map = {}

    for status in ["completed", "current", "upcoming", "verification_needed"]:
        for item in journey[status]:
            status_map[item["name"]] = status

    for milestone in MILESTONES:

        name = milestone["name"]
        status = status_map.get(name)

        if status != "completed":
            return {
                **milestone,
                "status": status
            }

    return None