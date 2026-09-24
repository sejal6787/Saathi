from datetime import date
from journey.engine import build_journey
from journey.gap_detector import detect_gaps


class FakeEvent:
    def __init__(self, event_type, event_date):
        self.event_type = event_type
        self.event_date = event_date


class FakePregnancy:
    def __init__(self, last_menstrual_period, expected_delivery_date):
        self.last_menstrual_period = last_menstrual_period
        self.expected_delivery_date = expected_delivery_date


events = [
    FakeEvent("LAB_TEST", date(2026, 7, 20)),
    FakeEvent("DELIVERY", date(2026, 11, 5)),
]


pregnancy = FakePregnancy(
    last_menstrual_period = date(2026, 1, 1),
    expected_delivery_date= None
)


print("Test date:", date(2026, 12, 20))

result = build_journey(
    events,
    pregnancy,
    date(2026, 12, 20)
)

print(result)



test_pregnancy = FakePregnancy(
    last_menstrual_period=date(2026, 1, 1),
    expected_delivery_date=date(2026, 9, 1)
)

test_events = [
    FakeEvent("ANC_VISIT", date(2026, 3, 1))
]

test_journey_result = build_journey(
    test_events,
    test_pregnancy,
    date(2026, 9, 23)
)

test_gaps = detect_gaps(
    test_journey_result,
    test_pregnancy,
    date(2026, 9, 23)
)

print("Delivery gap test:")
print(test_gaps)