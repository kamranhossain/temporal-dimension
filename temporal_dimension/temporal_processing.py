from pydblite.pydblite import Base
import dateparser
import math
from datetime import datetime, timedelta,date
import calendar
from dateutil.relativedelta import relativedelta
import csv
import os
import time
from holidays_cal.usa.usa_fed_cal import UnitedStates

# function for getting quarter day
def get_quarters_day(date_obj):
        month = date_obj.month
        quarter = (month -1)//3+1
        year = date_obj.year
        month_day = date_obj.day
        first_month_of_quarter = 3 * quarter - 2
        second_month_of_quarter = 3 * quarter - 1
        last_month_of_quarter = 3 * quarter

        if month == first_month_of_quarter:
            return month_day
        if month == second_month_of_quarter:
            return calendar.monthrange(year,first_month_of_quarter)[1]+month_day
        if month == last_month_of_quarter:
            return calendar.monthrange(year,first_month_of_quarter)[1]+calendar.monthrange(year,second_month_of_quarter)[1]+month_day


# check date is weekday or not.
def get_weekday_flag(week_day_num):
    if week_day_num<=5:
        return 1
    else:
        return 0

# check date is month first day or not.
def get_month_first_day_flag(date,month_begin_date):
    if date == month_begin_date:
        return 1
    else:
        return 0

# check date is month last day or not.
def get_month_last_day_flag(date,month_end_date):
    if date == month_end_date:
        return 1
    else:
        return 0
        
# check date is quarter first day or not        
def get_quarter_first_day_flag(date,quarter_begin_date):
    if date == quarter_begin_date:
        return 1
    else:
        return 0

# check date is quarter last day or not.
def get_quarter_last_day_flag(date,quarter_end_date):
    if date == quarter_end_date:
        return 1
    else:
        return 0

# check date is year first day or not
def get_year_first_day_flag(date,year_begin_date):
    if date == year_begin_date:
        return 1
    else:
        return 0

# check date is year last day or not.       
def get_year_last_day_flag(date,year_end_date):
    if date == year_end_date:
        return 1
    else:
        return 0

# check date year is leap year or not.
def get_leap_year_flag(year_num):
    if (year_num % 4) == 0:
        if (year_num % 100) == 0:
            if (year_num % 400) == 0:
                return 1
        else:
            return 1        
    return 0

# compare week and month start date to get month week begin date. 
def get_month_week_begin_date(week_start_date,month_begin_date):
    if week_start_date<month_begin_date:
        return month_begin_date
    return week_start_date
    

# compare week and month end date to get month week end date. 
def get_month_week_end_date(week_end_date,month_end_date):
    if week_end_date>month_end_date:
        return month_end_date
    return week_end_date

# compare week and quarter start date to get quarter week begin date.
def get_quarter_week_begin_date(week_start_date,quarter_begin_date):
    if week_start_date<quarter_begin_date:
        return quarter_begin_date
    return week_start_date
    
# compare week and quarter end date to get quarter week end date. 
def get_quarter_week_end_date(week_end_date,quarter_end_date):
    if week_end_date>quarter_end_date:
        return quarter_end_date
    return week_end_date

# compare week and year start date to get year week begin date.
def get_year_week_begin_date(week_start_date,year_begin_date):
    if week_start_date<year_begin_date:
        return year_begin_date
    return week_start_date
    
# compare week and year end date to get year week end date. 
def get_year_week_end_date(week_end_date,year_end_date):
    if week_end_date>year_end_date:
        return year_end_date
    return week_end_date

# check week first day or not
def get_week_first_day_flag(date,week_start_date):
    if date == week_start_date:
        return 1
    return 0

# check week day last day or not
def get_week_last_day_flag(date,week_end_date):
    if date == week_end_date:
        return 1
    return 0
# check is us_fed_holiday or not
def get_is_us_holiday(cal, date):
    cal=cal
    if date == cal.is_holiday(date):
        return 1
    else:
        return 0 


# create pydblite database table
date_table = Base('temporal_data.pdl')

# check db table is exists or not.if not exists then create table.
if not date_table.exists():
    # create table with field.
    date_table.create(
        'date',
        'julian_date_num',
        'sequence',
        'week_day_num',
        'day_name',
        'day_short_name',
        'month_week_num',
        'month_week_begin_date',
        'month_week_end_date',
        'quarter_week_num',
        'quarter_week_begin_date',
        'quarter_week_end_date',
        'year_week_num',
        'year_week_begin_date',
        'year_week_end_date',
        'month_day_num',
        'month_num',
        'month_name',
        'month_short_name',
        'month_begin_date',
        'month_end_date',
        'quarter_day_num',
        'quarter_num',
        'quarter_name',
        'quarter_begin_date',
        'quarter_end_date',
        'year_day_num',
        'year_num',
        'year_begin_date',
        'year_end_date',
        'dd_mon_yyyy',
        'dd_month_yyyy',
        'mon_dd_yyyy',
        'month_dd_yyyy',
        'dd_mm_yyyy',
        'mm_dd_yyyy',
        'mm_dd_yy',
        'dd_mm_yy',
        'm_d_yy',
        'd_m_yy',
        'weekday_flag',
        'week_first_day_flag',
        'week_last_day_flag',
        'month_first_day_flag',
        'month_last_day_flag',
        'quarter_first_day_flag',
        'quarter_last_day_flag',
        'year_first_day_flag',
        'year_last_day_flag',
        'leap_year_flag',
        'is_holiday'
    )
    # create index
    date_table.create_index('date','julian_date_num','sequence')

# validate date input.
while True:
    # imput start date string
    start_date_string = input("Enter start date with format mm/dd/yyyy: ")
    try:
        valid_date = time.strptime(start_date_string, '%m/%d/%Y')
        # convert date string to date object.
        start_date = dateparser.parse(start_date_string)
        break

    except ValueError:
        print('Invalid date!.Please enter valid date')
        continue

while True:
    # input number of year which date will be generated and process data.
    num_of_year = input("How many years of data(after start date): ")
    try:
        valid_num_of_year = int(num_of_year)
        break
    except ValueError:
        print("That's not an int!")

# calculate end date.
end_date = start_date + relativedelta(years=int(num_of_year))

# day number between start and end date.
day_num = (end_date - start_date).days
# open table 
date_table = date_table.open()
# iterate date and process data.
for item in range(day_num):
    date = (start_date+timedelta(days=item)).date()
    # check date is exists or not.If exists then continue.
    if len(date_table(date=date))>0:
        continue
    sequence = len(date_table)+1
    week_day_num = date.weekday()+1
    day_name =date.strftime("%A")
    day_short_name = date.strftime("%a")
    month_day_num = date.day
    month_name = date.strftime("%B")
    month_short_name = date.strftime("%b")
    year_num = date.year
    month_num = date.month
    month_begin_date = date.replace(day=1)
    total_month_day = calendar.monthrange(year_num,month_num)[1]
    month_end_date = month_begin_date + timedelta(days=(total_month_day - 1))
    quarter_num = (month_num -1)//3+1
    quarter_name = "Qtr{}".format(quarter_num)
    quarter_begin_date = datetime(year_num, 3 * quarter_num - 2, 1).date()
    quarter_end_date = (quarter_begin_date + relativedelta(months=3, days=-1))
    year_day_num = date.timetuple().tm_yday 
    year_begin_date = date.replace(month=1, day=1)
    year_end_date = date.replace(month=12, day=31)
    dd_mon_yyyy = date.strftime('%d-%b-%Y')
    dd_month_yyyy = date.strftime('%d-%B-%Y')
    mon_dd_yyyy = date.strftime('%b-%d-%Y')
    month_dd_yyyy = date.strftime('%B-%d-%Y')
    dd_mm_yyyy = date.strftime('%d-%m-%Y')
    mm_dd_yyyy = date.strftime('%m-%d-%Y')
    mm_dd_yy = date.strftime('%m/%d/%y')
    dd_mm_yy = date.strftime('%d/%m/%y')
    m_d_yy = date.strftime('%-m/%-d/%y')
    d_m_yy = date.strftime('%-d/%-m/%y')
    weekday_flag = get_weekday_flag(week_day_num)
    month_first_day_flag = get_month_first_day_flag(date,month_begin_date)
    month_last_day_flag = get_month_last_day_flag(date,month_end_date)
    quarter_first_day_flag = get_quarter_first_day_flag(date,quarter_begin_date)
    quarter_last_day_flag = get_quarter_last_day_flag(date,quarter_end_date)
    year_first_day_flag = get_year_first_day_flag(date,year_begin_date)
    year_last_day_flag = get_year_last_day_flag(date,year_end_date)
    leap_year_flag = get_leap_year_flag(year_num)
    week_start_date = date - timedelta(days=date.weekday())
    week_end_date = week_start_date + timedelta(days=6)
    month_week_num = (month_day_num- 1) // 7 + 1
    month_week_begin_date = get_month_week_begin_date(week_start_date,month_begin_date)
    month_week_end_date = get_month_week_end_date(week_end_date,month_end_date)
    quarter_day_num = get_quarters_day(date)
    quarter_week_num = (quarter_day_num- 1) // 7 + 1
    quarter_week_begin_date = get_quarter_week_begin_date(week_start_date,quarter_begin_date)
    quarter_week_end_date = get_quarter_week_end_date(week_end_date,quarter_end_date)
    year_week_num = (year_day_num- 1) // 7 + 1
    year_week_begin_date = get_year_week_begin_date(week_start_date,year_begin_date)
    year_week_end_date = get_year_week_end_date(week_end_date,year_end_date)
    week_first_day_flag = get_week_first_day_flag(date,week_start_date)
    week_last_day_flag = get_week_last_day_flag(date,week_end_date)
    # julian_date_num = date_to_jd(year_num,month_num,day_num)
    julian_date_num = float(date.strftime('%y%j'))
    is_holiday = get_is_us_holiday(UnitedStates(), date)
    # insert data on table.
    date_table.insert(
        date=date,
        julian_date_num=julian_date_num,
        sequence=sequence,
        week_day_num=week_day_num,
        day_name=day_name,
        day_short_name = day_short_name,
        month_week_num = month_week_num,
        month_week_begin_date = month_week_begin_date,
        month_week_end_date = month_week_end_date,
        quarter_week_num = quarter_week_num,
        quarter_week_begin_date = quarter_week_begin_date,
        quarter_week_end_date = quarter_week_end_date,
        year_week_num = year_week_num,
        year_week_begin_date = year_week_begin_date,
        year_week_end_date = year_week_end_date,
        month_day_num =month_day_num,
        month_num =month_num,
        month_name =month_name,
        month_short_name = month_short_name,
        month_begin_date = month_begin_date,
        month_end_date =month_end_date,
        quarter_day_num =quarter_day_num,
        quarter_num =quarter_num,
        quarter_name = quarter_name,
        quarter_begin_date =quarter_begin_date,
        quarter_end_date =quarter_end_date,
        year_day_num =year_day_num,
        year_num =year_num,
        year_begin_date =year_begin_date,
        year_end_date=year_end_date,
        dd_mon_yyyy =dd_mon_yyyy,
        dd_month_yyyy =dd_month_yyyy,
        mon_dd_yyyy=mon_dd_yyyy,
        month_dd_yyyy =month_dd_yyyy,
        dd_mm_yyyy =dd_mm_yyyy,
        mm_dd_yyyy =mm_dd_yyyy,
        mm_dd_yy = mm_dd_yy,
        dd_mm_yy = dd_mm_yy,
        m_d_yy = m_d_yy,
        d_m_yy = d_m_yy,
        weekday_flag =weekday_flag,
        week_first_day_flag=week_first_day_flag,
        week_last_day_flag = week_last_day_flag,
        month_first_day_flag =month_first_day_flag,
        month_last_day_flag =month_last_day_flag,
        quarter_first_day_flag =quarter_first_day_flag,
        quarter_last_day_flag =quarter_last_day_flag,
        year_first_day_flag =year_first_day_flag,
        year_last_day_flag =year_last_day_flag,
        leap_year_flag =leap_year_flag,
        is_holiday = is_holiday
        )
# save data.       
date_table.commit()
# write data as CSV 
with open('temporal_data.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     # write header
     wr.writerow(list(date_table[0].keys()))
     # write value
     for item in date_table:
        wr.writerow(list(item.values()))