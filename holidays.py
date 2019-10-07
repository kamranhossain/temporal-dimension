from calendar import monthrange
from datetime import date, timedelta
from dateutil import easter

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)


class Calendar(object):
    FIXED_HOLIDAYS = ()
    WEEKEND_DAYS = ()

    def __init__(self):
        self._holidays = {}

    def get_fixed_days(self, year):
        """Return the fixed days according to the FIXED_DAYS class property
        """
        days = []
        for month, day, lable in self.FIXED_HOLIDAYS:
            days.append((date(year, month, day), lable))
        return days

    def get_variable_days(self, year):
        return []

    def get_calendar_holidays(self, year):
        return self.get_fixed_days(year) + self.get_variable_days(year)

    def holidays(self, year=None):
        "Computes holidays (non-working days) for a given year"
        if not year:
            year = date.today().year

        if year in self._holidays:
            return self._holidays[year]

        # Here we process the holiday specific calendar
        temp_calendar = tuple(self.get_calendar_holidays(year))

        # it is sorted
        self._holidays[year] = sorted(temp_calendar)
        return self._holidays[year]

    def get_weekend_days(self):
        if self.WEEKEND_DAYS:
            return self.WEEKEND_DAYS
        raise NotImplementedError("Your Calendar class must implement the"
                                  " `get_weekend_days` method")
 

    def get_easter_sunday(self, year):
        "Return the date of the easter (sunday) -- following the easter method"
        return easter.easter(year, self.EASTER_METHOD)

    def get_easter_monday(self, year):
        "Return the date of the monday after easter"
        sunday = self.get_easter_sunday(year)
        return sunday + timedelta(days=1)

    @staticmethod
    def get_nth_weekday_in_month(year, month, weekday, n=1):
        day = date(year, month, 1)
        counter = 0
        while True:
            if day.month != month:
                # Don't forget to break if "n" is too big
                return None
            if day.weekday() == weekday:
                counter += 1
            if counter == n:
                break
            day = day + timedelta(days=1)
        return day

    @staticmethod
    def get_last_weekday_in_month(year, month, weekday):
        day = date(year, month, monthrange(year, month)[1])
        while True:
            if day.weekday() == weekday:
                break
            day = day - timedelta(days=1)
        return day


class WesternCalendar(Calendar):
    """
    General usage calendar for Western countries.
    (chiefly Europe and Northern America)
    """
    EASTER_METHOD = 3  # 3 is 'Western'
    WEEKEND_DAYS = (SAT, SUN)

    FIXED_HOLIDAYS = (
        (1, 1, 'New year'),
    )

    def get_weekend_days(self):
        "Week-end days are SATurday and SUNday."
        return self.WEEKEND_DAYS

class UnitedStates(WesternCalendar):
    "USA calendar"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (7, 4, 'Independence Day'),
    )

    include_veterans_day = True
    veterans_day_label = 'Veterans Day'
    martin_luther_king_label = 'Birthday of Martin Luther King, Jr.'

    def get_martin_luther_king_date(self, year):
        """
        Martin Luther King is on 3rd MON of January, starting of 1985.
        """
        if year < 1985:
            raise ValueError(
                "Martin Luther King Day became a holiday in 1985"
            )
        return UnitedStates.get_nth_weekday_in_month(year, 1, MON, 3)

    def get_martin_luther_king_day(self, year):
        """
        Return holiday record for Martin Luther King Jr. Day.
        """
        day = self.get_martin_luther_king_date(year)
        return (day, self.martin_luther_king_label)


    def get_variable_days(self, year):
        days = super(UnitedStates, self).get_variable_days(year)

        # Martin Luther King's Day started only in 1985
        if year >= 1985:
            days.append(self.get_martin_luther_king_day(year))
        
        return days
    
    def shift_days():
        pass

    def get_veterans_day(self, year):
        """
        Return Veterans Day (November 11th).
        Placed here because some States are renaming it.
        """
        return (date(year, 11, 11), self.veterans_day_label)

    def get_fixed_holidays(self, year):
        days = super(UnitedStates, self).get_fixed_holidays(year)
        if self.include_veterans_day:
            days.append(self.get_veterans_day(year))
        return days

    def get_calendar_holidays(self, year):
        days = super(UnitedStates, self).get_calendar_holidays(year)
        return days