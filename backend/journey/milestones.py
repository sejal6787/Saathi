TIMING_RULES = {
    "ANC_VISIT": {},
    "LAB_TEST": {},
    "ULTRASOUND": {},
    "DELIVERY": {},
    "POSTNATAL_VISIT": {},
}


MILESTONES = [
    {
    "name": "ANC Visit 1",
    "event_type": "ANC_VISIT",
    "description": "First antenatal care visit",
    "stage": "pregnancy",
    "timing": {
        "start_week": 0,
        "end_week": 12,
    },
    },
    {
    "name": "ANC Visit 2",
    "event_type": "ANC_VISIT",
    "description": "Second antenatal care visit",
    "stage": "pregnancy",
    "timing": {
        "start_week": 14,
        "end_week": 26,
    },
    },
    {
    "name": "ANC Visit 3",
    "event_type": "ANC_VISIT",
    "description": "Third antenatal care visit",
    "stage": "pregnancy",
    "timing": {
        "start_week": 28,
        "end_week": 34,
    },
    },
    {
    "name": "ANC Visit 4",
    "event_type": "ANC_VISIT",
    "description": "Fourth antenatal care visit",
    "stage": "pregnancy",
    "timing": {
        "start_week": 36,
        "end_week": None,
    },
    },


    {
        "name": "Lab Test",
        "event_type": "LAB_TEST",
        "description": "Routine pregnancy laboratory test",
        "stage": "pregnancy",
        "timing": None,
    },
    {
        "name": "Ultrasound",
        "event_type": "ULTRASOUND",
        "description": "Pregnancy ultrasound examination",
        "stage": "pregnancy",
        "timing": None,
    },
    {
        "name": "Delivery",
        "event_type": "DELIVERY",
        "description": "Delivery event",
        "stage": "pregnancy",
        "timing": None,
    },
    {
        "name": "Postnatal Visit",
        "event_type": "POSTNATAL_VISIT",
        "description": "Postnatal care visit",
        "stage": "pregnancy",
        "timing": None,
    },
]