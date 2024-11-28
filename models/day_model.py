from config.enums import AdventCalendar, AdventPart


class DayModel:
    def __init__(self, calendar: AdventCalendar, part: AdventPart):
        self.calendar = calendar
        self.part = part
