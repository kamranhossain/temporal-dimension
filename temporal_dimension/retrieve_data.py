from pydblite.pydblite import Base
import cProfile
import time
from workalendar.core import Calendar, MON, TUE, WED, THU, FRI, SAT, SUN

date_table = Base('temporal_data.pdl')
date_table = date_table.create(mode="open")
# nth_weekday = input("Give the year, month, weekday, nth number(2010, 2, 2, 3): ")
nth_weekday = (2010, 2, 2, 3)

def retrieve_is_holiday(date_table):
    is_holiday_list = [r['is_holiday'] for r in date_table if r['is_holiday'] != None]
    return is_holiday_list
    

def retrieve_holidays_name(date_table):
    holiday_name_list = [r['holiday_name'] for r in date_table if r['holiday_name'] != None]
    return holiday_name_list

def retrieve_nth_weekday_loop(date_table, nth_weekday):
    for r in date_table._nth_weekday[nth_weekday]:
        return (r['date'])
        
def retrieve_nth_weekday_map(date_table, nth_weekday):
    date = list(map(lambda r:r['date'] , date_table._nth_weekday[nth_weekday]))
    return date

def retrieve_nth_weekday_list_comp(date_table, nth_weekday):
    date = [r['date'] for r in date_table._nth_weekday[nth_weekday]]
    return date[0]

def retrieve_nth_weekday_all_fields(date_table, nth_weekday):
    return date_table._nth_weekday[nth_weekday]
