import cProfile
import time
from pydblite.pydblite import Base
from workalendar.core import Calendar, MON, TUE, WED, THU, FRI, SAT, SUN
from ..retrieve_data import (retrieve_nth_weekday_loop, retrieve_nth_weekday_map
        retrieve_nth_weekday_list_comp, retrieve_nth_weekday_all_fields)

date_table = Base('temporal_data.pdl')
date_table = date_table.create(mode="open")
# nth_weekday = input("Give the year, month, weekday, nth number(2010, 2, 2, 3): ")
nth_weekday = (2010, 2, 2, 3)




# call loop function
start_time_ns = time.time_ns()
retrieve_nth_weekday_loop(date_table, nth_weekday)
elapsed_time_ns = time.time_ns() - start_time_ns
print("loop_return_date_only in {} nenoseconds".format(elapsed_time_ns))

# call map function
start_time_ns = time.time_ns()
retrieve_nth_weekday_map(date_table, nth_weekday)
elapsed_time_ns = time.time_ns() - start_time_ns
print("map_function_return_list in {} nenoseconds".format(elapsed_time_ns))

# call list comprehension function
start_time_ns = time.time_ns()
retrieve_nth_weekday_list_comp(date_table, nth_weekday)
elapsed_time_ns = time.time_ns() - start_time_ns
print("list_comperehension_return_list in {} nenoseconds".format(elapsed_time_ns))


# call all fields function
start_time_ns = time.time_ns()
retrieve_nth_weekday_all_fields(date_table, nth_weekday)
elapsed_time_ns = time.time_ns() - start_time_ns
print("all_fields_related to nth_weekday_index in {} nenoseconds".format(elapsed_time_ns))

# call workalendar main nth_weekday function
start_time_ns = time.time_ns()
Calendar.get_nth_weekday_in_month(2010, 2, FRI, 3)
elapsed_time_ns = time.time_ns() - start_time_ns
print("Calendar built-in function return date in {} nenoseconds".format(elapsed_time_ns))
