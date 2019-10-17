from pydblite.pydblite import Base

def retrieve_is_holiday():
    date_table = Base('temporal_data.pdl')
    date_table.create(mode="open")
    is_holiday_list = [r['is_holiday'] for r in date_table if r['is_holiday'] != None]
    print(is_holiday_list)
    

def retrieve_holidays_name():
    date_table = Base('temporal_data.pdl')
    date_table.create(mode="open")
    holiday_name_list = [r['holiday_name'] for r in date_table if r['holiday_name'] != None]
    print(holiday_name_list)

def retrieve_nth_weekday(year, month, weekday, n=1):
    date_table = Base('temporal_data.pdl')
    date_table.create(mode="open")
    for r in date_table:
        if r['year_num'] == year and \
            r['month_num'] == month  and \
            r['month_week_num']== n and \
            r['day_short_name'] == weekday:
            print(r['date'])
    