# -*- coding: utf-8 -*-
"""
Working day tools
"""
from copy import copy
import warnings
from calendar import monthrange
from datetime import date, timedelta, datetime

from dateutil import easter

from .exceptions import UnsupportedDateType

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)


class classproperty(object):

    def __init__(self, getter):
        self.getter = getter
        self.__doc__ = getter.__doc__

    def __get__(self, instance, owner):
        return self.getter(owner)


def cleaned_date(day, keep_datetime=False):
    """
    Return a "clean" date type.

    * keep a `date` unchanged
    * convert a datetime into a date,
    * convert any "duck date" type into a date using its `date()` method.
    """
    if not isinstance(day, (date, datetime)):
        raise UnsupportedDateType(
            "`{}` is of unsupported type ({})".format(day, type(day)))
    if not keep_datetime:
        if hasattr(day, 'date') and callable(day.date):
            day = day.date()
    return day


class Calendar(object):

    FIXED_holidays = ()
    WEEKEND_DAYS = ()

    def __init__(self):
        self._holidays = {}

    @classproperty
    def name(cls):
        class_name = cls.__name__
        if cls.__doc__:
            doc = cls.__doc__.split('\n')
            doc = map(lambda s: s.strip(), doc)
            return next(s for s in doc if s)
        return class_name

    def get_fixed_holidays(self, year):
        """Return the fixed days according to the FIXED_holidays class property
        """
        days = []
        for month, day, label in self.FIXED_holidays:
            days.append((date(year, month, day), label))
        return days

    def get_variable_days(self, year):
        return []

    def get_calendar_holidays(self, year):
        """Get calendar holidays.
        If you want to override this, please make sure that it **must** return
        a list of tuples (date, holiday_name)."""
        return self.get_fixed_holidays(year) + self.get_variable_days(year)

    def holidays(self, year=None):
        """Computes holidays (non-working days) for a given year.
        Return a 2-item tuple, composed of the date and a label."""
        if not year:
            year = date.today().year

        if year in self._holidays:
            return self._holidays[year]

        # Here we process the holiday specific calendar
        temp_calendar = tuple(self.get_calendar_holidays(year))

        # it is sorted
        self._holidays[year] = sorted(temp_calendar)
        return self._holidays[year]

    def get_holiday_label(self, day):
        """Return the label of the holiday, if the date is a holiday"""
        day = cleaned_date(day)
        return {day: label for day, label in self.holidays(day.year)
                }.get(day)

    def holidays_set(self, year=None):
        "Return a quick date index (set)"
        return set([day for day, label in self.holidays(year)])

    def get_weekend_days(self):
        """Return a list (or a tuple) of weekdays that are *not* working days.

        e.g: return (SAT, SUN,)

        """
        if self.WEEKEND_DAYS:
            return self.WEEKEND_DAYS
        else:
            raise NotImplementedError("Your Calendar class must provide "
                                      "WEEKEND_DAYS or implement the "
                                      "`get_weekend_days` method")

    def is_working_day(self, day,
                       extra_working_days=None, extra_holidays=None):
        """Return True if it's a working day.
        In addition to the regular holidays, you can add exceptions.

        By providing ``extra_working_days``, you'll state that these dates
        **are** working days.

        By providing ``extra_holidays``, you'll state that these dates **are**
        holidays, even if not in the regular calendar holidays (or weekends).

        Please note that the ``extra_working_days`` list has priority over the
        ``extra_holidays`` list.

        """
        day = cleaned_date(day)
        if extra_working_days:
            extra_working_days = tuple(map(cleaned_date, extra_working_days))
        if extra_holidays:
            extra_holidays = tuple(map(cleaned_date, extra_holidays))

        # Extra lists exceptions
        if extra_working_days and day in extra_working_days:
            return True

        # Regular rules
        if day.weekday() in self.get_weekend_days():
            return False

        return not self.is_holiday(day, extra_holidays=extra_holidays)

    def is_holiday(self, day, extra_holidays=None):
        """Return True if it's an holiday.
        In addition to the regular holidays, you can add exceptions.

        By providing ``extra_holidays``, you'll state that these dates **are**
        holidays, even if not in the regular calendar holidays (or weekends).

        """
        day = cleaned_date(day)

        if extra_holidays:
            extra_holidays = tuple(map(cleaned_date, extra_holidays))

        if extra_holidays and day in extra_holidays:
            return True

        return day in self.holidays_set(day.year)

    def add_working_days(self, day, delta,
                         extra_working_days=None, extra_holidays=None,
                         keep_datetime=False):
        """Add `delta` working days to the date.

        You can provide either a date or a datetime to this function that will
        output a ``date`` result. You can alter this behaviour using the
        ``keep_datetime`` option set to ``True``.

        the ``delta`` parameter might be positive or negative. If it's
        negative, you may want to use the ``sub_working_days()`` method with
        a positive ``delta`` argument.

        By providing ``extra_working_days``, you'll state that these dates
        **are** working days.

        By providing ``extra_holidays``, you'll state that these dates **are**
        holidays, even if not in the regular calendar holidays (or weekends).

        Please note that the ``extra_working_days`` list has priority over the
        ``extra_holidays`` list.
        """
        day = cleaned_date(day, keep_datetime)

        if extra_working_days:
            extra_working_days = tuple(map(cleaned_date, extra_working_days))

        if extra_holidays:
            extra_holidays = tuple(map(cleaned_date, extra_holidays))

        days = 0
        temp_day = day
        if type(temp_day) is datetime and not keep_datetime:
            temp_day = temp_day.date()
        day_added = 1 if delta >= 0 else -1
        delta = abs(delta)
        while days < delta:
            temp_day = temp_day + timedelta(days=day_added)
            if self.is_working_day(temp_day,
                                   extra_working_days=extra_working_days,
                                   extra_holidays=extra_holidays):
                days += 1
        return temp_day

    def sub_working_days(self, day, delta,
                         extra_working_days=None, extra_holidays=None,
                         keep_datetime=False):
        """
        Substract `delta` working days to the date.

        This method is a shortcut / helper. Users may want to use either::

            cal.add_working_days(my_date, -7)
            cal.sub_working_days(my_date, 7)

        The other parameters are to be used exactly as in the
        ``add_working_days`` method.

        A negative ``delta`` argument will be converted into its absolute
        value. Hence, the two following calls are equivalent::

            cal.sub_working_days(my_date, -7)
            cal.sub_working_days(my_date, 7)

        As in ``add_working_days()`` you can set the parameter
        ``keep_datetime`` to ``True`` to make sure that if your ``day``
        argument is a ``datetime``, the returned date will also be a
        ``datetime`` object.

        """
        delta = abs(delta)
        return self.add_working_days(
            day, -delta,
            extra_working_days, extra_holidays, keep_datetime=keep_datetime)

    def find_following_working_day(self, day):
        """Looks for the following working day, if not already a working day.

        **WARNING**: this function doesn't take into account the calendar
        holidays, only the days of the week and the weekend days parameters.
        """
        day = cleaned_date(day)

        while day.weekday() in self.get_weekend_days():
            day = day + timedelta(days=1)
        return day

    @staticmethod
    def get_nth_weekday_in_month(year, month, weekday, n=1, start=None):
        """Get the nth weekday in a given month. e.g:

        >>> # the 1st monday in Jan 2013
        >>> Calendar.get_nth_weekday_in_month(2013, 1, MON)
        datetime.date(2013, 1, 7)
        >>> # The 2nd monday in Jan 2013
        >>> Calendar.get_nth_weekday_in_month(2013, 1, MON, 2)
        datetime.date(2013, 1, 14)
        """
        # If start is `None` or Falsy, no need to check and clean
        if start:
            start = cleaned_date(start)

        day = date(year, month, 1)
        if start:
            day = start
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
        """Get the last weekday in a given month. e.g:

        >>> # the last monday in Jan 2013
        >>> Calendar.get_last_weekday_in_month(2013, 1, MON)
        datetime.date(2013, 1, 28)
        """
        day = date(year, month, monthrange(year, month)[1])
        while True:
            if day.weekday() == weekday:
                break
            day = day - timedelta(days=1)
        return day

    @staticmethod
    def get_first_weekday_after(day, weekday):
        """Get the first weekday after a given day. If the day is the same
        weekday, the same day will be returned.

        >>> # the first monday after Apr 1 2015
        >>> Calendar.get_first_weekday_after(date(2015, 4, 1), MON)
        datetime.date(2015, 4, 6)

        >>> # the first tuesday after Apr 14 2015
        >>> Calendar.get_first_weekday_after(date(2015, 4, 14), TUE)
        datetime.date(2015, 4, 14)
        """
        day_delta = (weekday - day.weekday()) % 7
        day = day + timedelta(days=day_delta)
        return day

    def get_working_days_delta(self, start, end, include_start=False):
        """
        Return the number of working day between two given dates.
        The order of the dates provided doesn't matter.

        In the following example, there are 5 days, because of the week-end:

        >>> cal = WesternCalendar()  # does not include easter monday
        >>> day1 = date(2018, 3, 29)
        >>> day2 = date(2018, 4, 5)
        >>> cal.get_working_days_delta(day1, day2)
        5

        In France, April 1st 2018 is a holiday because it's Easter monday:

        >>> cal = France()
        >>> cal.get_working_days_delta(day1, day2)
        4

        This method should even work if your ``start`` and ``end`` arguments
        are datetimes.

        By default, if the day after you start is not a working day,
        the count will start at 0. If include_start is set to true,
        this day will be taken into account.

        Example:

        >>> cal = France()
        >>> day1 = parse('09/05/2018 00:01', dayfirst=True)
        >>> day2 = parse('10/05/2018 19:01', dayfirst=True) # holiday in france
        >>> cal.get_working_days_delta(day_1, day_2)
        0

        >>> cal.get_working_days_delta(day_1, day_2, include_start=True)
        1
        """
        start = cleaned_date(start)
        end = cleaned_date(end)

        if start == end:
            return 0

        if start > end:
            start, end = end, start

        # Starting count here
        count = 1 if include_start and self.is_working_day(start) else 0
        while start < end:
            start += timedelta(days=1)
            if self.is_working_day(start):
                count += 1
        return count


class ChristianMixin(Calendar):
    EASTER_METHOD = None  # to be assigned in the inherited mixin
    include_epiphany = False
    include_clean_monday = False
    include_annunciation = False
    include_ash_wednesday = False
    ash_wednesday_label = "Ash Wednesday"
    include_palm_sunday = False
    include_holy_thursday = False
    include_good_friday = False
    good_friday_label = "Good Friday"
    include_easter_monday = False
    include_easter_saturday = False
    include_easter_sunday = False
    include_all_saints = False
    include_immaculate_conception = False
    immaculate_conception_label = "Immaculate Conception"
    include_christmas = True
    include_christmas_eve = False
    include_ascension = False
    include_assumption = False
    include_whit_sunday = False
    whit_sunday_label = 'Whit Sunday'
    include_whit_monday = False
    whit_monday_label = 'Whit Monday'
    include_corpus_christi = False
    include_boxing_day = False
    boxing_day_label = "Boxing Day"
    include_all_souls = False

    def get_ash_wednesday(self, year):
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=46)

    def get_palm_sunday(self, year):
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=7)

    def get_holy_thursday(self, year):
        "Return the date of the last thursday before easter"
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=3)

    def get_good_friday(self, year):
        "Return the date of the last friday before easter"
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=2)

    def get_clean_monday(self, year):
        "Return the clean monday date"
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=48)

    def get_easter_saturday(self, year):
        "Return the Easter Saturday date"
        sunday = self.get_easter_sunday(year)
        return sunday - timedelta(days=1)

    def get_easter_sunday(self, year):
        "Return the date of the easter (sunday) -- following the easter method"
        return easter.easter(year, self.EASTER_METHOD)

    def get_easter_monday(self, year):
        "Return the date of the monday after easter"
        sunday = self.get_easter_sunday(year)
        return sunday + timedelta(days=1)

    def get_ascension_thursday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=39)

    def get_whit_monday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=50)

    def get_whit_sunday(self, year):
        easter = self.get_easter_sunday(year)
        return easter + timedelta(days=49)

    def get_corpus_christi(self, year):
        return self.get_easter_sunday(year) + timedelta(days=60)

    def shift_christmas_boxing_days(self, year):
        """ When Christmas and/or Boxing Day falls on a weekend, it is rolled
            forward to the next weekday.
        """
        christmas = date(year, 12, 25)
        boxing_day = date(year, 12, 26)
        boxing_day_label = "{} Shift".format(self.boxing_day_label)
        results = []
        if christmas.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(christmas)
            results.append((shift, "Christmas Shift"))
            results.append((shift + timedelta(days=1), boxing_day_label))
        elif boxing_day.weekday() in self.get_weekend_days():
            shift = self.find_following_working_day(boxing_day)
            results.append((shift, boxing_day_label))
        return results

    def get_variable_days(self, year):  # noqa
        "Return the christian holidays list according to the mixin"
        days = super(ChristianMixin, self).get_variable_days(year)
        if self.include_epiphany:
            days.append((date(year, 1, 6), "Epiphany"))
        if self.include_clean_monday:
            days.append((self.get_clean_monday(year), "Clean Monday"))
        if self.include_annunciation:
            days.append((date(year, 3, 25), "Annunciation"))
        if self.include_ash_wednesday:
            days.append(
                (self.get_ash_wednesday(year), self.ash_wednesday_label)
            )
        if self.include_palm_sunday:
            days.append((self.get_palm_sunday(year), "Palm Sunday"))
        if self.include_holy_thursday:
            days.append((self.get_holy_thursday(year), "Holy Thursday"))
        if self.include_good_friday:
            days.append((self.get_good_friday(year), self.good_friday_label))
        if self.include_easter_saturday:
            days.append((self.get_easter_saturday(year), "Easter Saturday"))
        if self.include_easter_sunday:
            days.append((self.get_easter_sunday(year), "Easter Sunday"))
        if self.include_easter_monday:
            days.append((self.get_easter_monday(year), "Easter Monday"))
        if self.include_assumption:
            days.append((date(year, 8, 15), "Assumption of Mary to Heaven"))
        if self.include_all_saints:
            days.append((date(year, 11, 1), "All Saints Day"))
        if self.include_all_souls:
            days.append((date(year, 11, 2), "All Souls Day"))
        if self.include_immaculate_conception:
            days.append((date(year, 12, 8), self.immaculate_conception_label))
        if self.include_christmas:
            days.append((date(year, 12, 25), "Christmas Day"))
        if self.include_christmas_eve:
            days.append((date(year, 12, 24), "Christmas Eve"))
        if self.include_boxing_day:
            days.append((date(year, 12, 26), self.boxing_day_label))
        if self.include_ascension:
            days.append((
                self.get_ascension_thursday(year), "Ascension Thursday"))
        if self.include_whit_monday:
            days.append((self.get_whit_monday(year), self.whit_monday_label))
        if self.include_whit_sunday:
            days.append((self.get_whit_sunday(year), self.whit_sunday_label))
        if self.include_corpus_christi:
            days.append((self.get_corpus_christi(year), "Corpus Christi"))
        return days


class WesternCalendar(Calendar):
    """
    General usage calendar for Western countries.

    (chiefly Europe and Northern America)

    """
    EASTER_METHOD = easter.EASTER_WESTERN
    WEEKEND_DAYS = (SAT, SUN)
    shift_new_years_day = False

    FIXED_HOLIDAYS = (
        (1, 1, 'New year'),
    )

    def get_variable_days(self, year):
        days = super(WesternCalendar, self).get_variable_days(year)
        new_year = date(year, 1, 1)
        if self.shift_new_years_day:
            if new_year.weekday() in self.get_weekend_days():
                days.append((
                    self.find_following_working_day(new_year),
                    "New Year shift"))
        return days