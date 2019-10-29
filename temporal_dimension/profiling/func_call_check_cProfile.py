import cProfile
from pydblite.pydblite import Base
from workalendar.core import Calendar, MON, TUE, WED, THU, FRI, SAT, SUN
from ..retrieve_data import (retrieve_nth_weekday_loop, retrieve_nth_weekday_map
        retrieve_nth_weekday_list_comp, retrieve_nth_weekday_all_fields)


date_table = Base('temporal_data.pdl')
date_table = date_table.create(mode="open")
# nth_weekday = input("Give the year, month, weekday, nth number(2010, 2, 2, 3): ")
nth_weekday = (2010, 2, 2, 3)

cProfile.run('retrieve_nth_weekday_map(date_table, nth_weekday)')
cProfile.run('retrieve_nth_weekday_loop(date_table, nth_weekday)')
cProfile.run('retrieve_nth_weekday_all_fields(date_table, nth_weekday)')
cProfile.run('retrieve_nth_weekday_list_comp(date_table, nth_weekday)')
cProfile.run('Calendar.get_nth_weekday_in_month(2010, 2, FRI, 3)')
