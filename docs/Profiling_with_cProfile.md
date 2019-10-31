I save the nth weekday as (2010, 2, 3, 4) where 2010 is year, 2 is month, 3 is which day like Fri or Sat etc and 4 is week num of that month. Here are some function for checking the performance of see the weekday data. The index will give us all the fields related of that search. I make function only with index nth_weekday which give all fields respective nth_weekday and also make other 3 functions which give us only date related to that weekday. 

The functions of retrieve nth_weekday date from the in_memory table(from retrieve_data.py file)

Within those functions. One is loop through the index and give us the date of nth_weekday(retrieve_nth_weekday_loop). 
Second is using function map on nth_weekday index return the list of date(retrieve_nth_weekday_map)
Third is using list_comprehension on nth_weekday index return the list of date like map function(retrieve_nth_weekday_list_comp)
Forth is return all fields in table related to that nth_weekday using nth_weekday index.

All those functions has parameters  as the in memory db and nth_weekday.

From terminal we need to goto the exact folder and run our virtual env and download all the packages then run  python to goto the Python console. 

(venv) k@k:~/Documents/current_work/temporal-dimension/temporal_dimension$ python

Import all related functions for testing.

>>> from retrieve_data import retrieve_nth_weekday_loop, retrieve_nth_weekday_map, retrieve_nth_weekday_all_fields, retrieve_nth_weekday_list_comp

get temporal_data table in memory so we check those functions
>>> from pydblite import Base
>>> date_table = Base('temporal_data.pdl')
>>> date_table.open()
<pydblite.pydblite._BasePy3 object at 0x7fa131c42320>

import cProfile for profiling
>>> import cProfile
check  retrieve_nth_weekday_loop functions

>>> cProfile.run('retrieve_nth_weekday_loop(date_table, (2011, 12, 2, 3))')
         7 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 pydblite.py:100(__getitem__)
        1    0.000    0.000    0.000    0.000 pydblite.py:104(<listcomp>)
        1    0.000    0.000    0.000    0.000 retrieve_data.py:26(retrieve_nth_weekday_loop)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}

It calls 7 functions

check  retrieve_nth_weekday_map function
>>> cProfile.run('retrieve_nth_weekday_map(date_table, (2011, 12, 2, 3))')
         8 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 pydblite.py:100(__getitem__)
        1    0.000    0.000    0.000    0.000 pydblite.py:104(<listcomp>)
        1    0.000    0.000    0.000    0.000 retrieve_data.py:31(retrieve_nth_weekday_map)
        1    0.000    0.000    0.000    0.000 retrieve_data.py:32(<lambda>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}

It calls 8 functions

check  retrieve_nth_weekday_list_comp function
>>> cProfile.run('retrieve_nth_weekday_list_comp(date_table, (2011, 12, 2, 3))') 
         8 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 pydblite.py:100(__getitem__)
        1    0.000    0.000    0.000    0.000 pydblite.py:104(<listcomp>)
        1    0.000    0.000    0.000    0.000 retrieve_data.py:35(retrieve_nth_weekday_list_comp)
        1    0.000    0.000    0.000    0.000 retrieve_data.py:36(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}

It calls 8 functions





check  retrieve_nth_weekday_all_fields function
>>> cProfile.run('retrieve_nth_weekday_all_fields(date_table, (2011, 12, 2, 3))')
         7 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 pydblite.py:100(__getitem__)
        1    0.000    0.000    0.000    0.000 pydblite.py:104(<listcomp>)
        1    0.000    0.000    0.000    0.000 retrieve_data.py:39(retrieve_nth_weekday_all_fields)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}

It calls 7 functions

import main function of workalendar to checking the performance

>>> from workalendar.core import Calendar, FRI

run Profiling on main function 
>>> cProfile.run('Calendar.get_nth_weekday_in_month(2011, 1, FRI)')
         11 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 core.py:255(get_nth_weekday_in_month)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        7    0.000    0.000    0.000    0.000 {method 'weekday' of 'datetime.date' objects}


It calls 11 functions

exact date returns by those functions

retrieve_nth_weekday_loop(date_table, (2011, 12, 2, 3))
datetime.date(2011, 12, 20)
It return date

>>> retrieve_nth_weekday_map(date_table, (2011, 12, 2, 3))
[datetime.date(2011, 12, 20)]
It return list of date

>>> retrieve_nth_weekday_list_comp(date_table, (2011, 12, 2, 3))
[datetime.date(2011, 12, 20)]
It return list of date





>>> retrieve_nth_weekday_all_fields(date_table, (2011, 12, 2, 3))
[{'date': datetime.date(2011, 12, 20), 'julian_date_num': 11354.0, 'sequence': 719, 'week_day_num': 2, 'day_name': 'Tuesday', 'day_short_name': 'Tue', 'month_week_num': 3, 'month_week_begin_date': datetime.date(2011, 12, 19), 'month_week_end_date': datetime.date(2011, 12, 25), 'quarter_week_num': 12, 'quarter_week_begin_date': datetime.date(2011, 12, 19), 'quarter_week_end_date': datetime.date(2011, 12, 25), 'year_week_num': 51, 'year_week_begin_date': datetime.date(2011, 12, 19), 'year_week_end_date': datetime.date(2011, 12, 25), 'month_day_num': 20, 'month_num': 12, 'month_name': 'December', 'month_short_name': 'Dec', 'month_begin_date': datetime.date(2011, 12, 1), 'month_end_date': datetime.date(2011, 12, 31), 'quarter_day_num': 81, 'quarter_num': 4, 'quarter_name': 'Qtr4', 'quarter_begin_date': datetime.date(2011, 10, 1), 'quarter_end_date': datetime.date(2011, 12, 31), 'year_day_num': 354, 'year_num': 2011, 'year_begin_date': datetime.date(2011, 1, 1), 'year_end_date': datetime.date(2011, 12, 31), 'dd_mon_yyyy': '20-Dec-2011', 'dd_month_yyyy': '20-December-2011', 'mon_dd_yyyy': 'Dec-20-2011', 'month_dd_yyyy': 'December-20-2011', 'dd_mm_yyyy': '20-12-2011', 'mm_dd_yyyy': '12-20-2011', 'mm_dd_yy': '12/20/11', 'dd_mm_yy': '20/12/11', 'm_d_yy': '12/20/11', 'd_m_yy': '20/12/11', 'weekday_flag': 1, 'week_first_day_flag': 0, 'week_last_day_flag': 0, 'month_first_day_flag': 0, 'month_last_day_flag': 0, 'quarter_first_day_flag': 0, 'quarter_last_day_flag': 0, 'year_first_day_flag': 0, 'year_last_day_flag': 0, 'leap_year_flag': 0, 'is_holiday': 0, 'holiday_name': None, 'nth_weekday': (2011, 12, 2, 3), '__id__': 718, '__version__': 0}]
It return all fields corresponding with that nth_weekday

>>> Calendar.get_nth_weekday_in_month(2011, 1, FRI)
datetime.date(2011, 1, 7)
the main function return date

cProfile limitation is it show us 3 digit after decimal. For this we need to check with nano second.