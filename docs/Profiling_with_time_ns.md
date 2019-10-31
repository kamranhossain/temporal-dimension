Caution: python 3.7+ needed for this

I test those functions with nanoseconds to get the accurate profiling time. For that I need to step aside from cProfile and go with Python time module. There is a function called time_ns which give  us nanoseconds. For test purpose I just put value of nth_weekday default and Open database in-memory on the top. So functions later get that as a parameters and give us result as expected.
These functions are in the file named retrieve_data.py. Here we see in image which functions are here. 

1: import and open in-memory database and assign default data

import time
from pydblite.pydblite import Base
from workalendar.core import Calendar, MON, TUE, WED, THU, FRI, SAT, SUN
from ..retrieve_data import (retrieve_nth_weekday_loop, retrieve_nth_weekday_map
        retrieve_nth_weekday_list_comp, retrieve_nth_weekday_all_fields)

date_table = Base('temporal_data.pdl')
date_table = date_table.create(mode="open")
nth_weekday = (2010, 2, 2, 3)

2: The functions of retrieve nth_weekday date from the in_memory table and call the function for profiling.

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

--------------------------------------------------------------------------------------------


Within those functions. One is loop through the index and give us the date of nth_weekday(retrieve_nth_weekday_loop). 
Second is using function map on nth_weekday index return the list of date(retrieve_nth_weekday_map)
Third is using list_comprehension on nth_weekday index return the list of date like map function(retrieve_nth_weekday_list_comp)
Forth is return all fields in table related to that nth_weekday using nth_weekday index.

All those functions has parameters  as the in memory db and nth_weekday.

Here I tested it with one year and two years inputs

From terminal we need to goto the exact folder and run our virtual env and download all the packages then run  python retrieve_data.py




Guess we have 1 year date inputs with running temporal_processing.py filename

4: Generate 1 years table

Then
(venv) k@k:~/Documents/current_work/temporal-dimension/temporal_dimension$ python retrieve_data.py

Output Sample 1:

loop_return_date_only in 21385 nenoseconds
map_function_return_list in 18732 nenoseconds
list_comperehension_return_list in 12000 nenoseconds
all_fields_related to nth_weekday_index in 9456 nenoseconds
Calendar built-in function return date in 125030 nenoseconds

Output Sample 2:

loop_return_date_only in 21541 nenoseconds
map_function_return_list in 19104 nenoseconds
list_comperehension_return_list in 12240 nenoseconds
all_fields_related to nth_weekday_index in 9312 nenoseconds
Calendar built-in function return date in 126758 nenoseconds

Output Sample 3:

loop_return_date_only in 22164 nenoseconds
map_function_return_list in 19369 nenoseconds
list_comperehension_return_list in 12516 nenoseconds
all_fields_related to nth_weekday_index in 9708 nenoseconds
Calendar built-in function return date in 124707 nenoseconds




Output Sample 4:

loop_return_date_only in 22152 nenoseconds
map_function_return_list in 18361 nenoseconds
list_comperehension_return_list in 12156 nenoseconds
all_fields_related to nth_weekday_index in 9816 nenoseconds
Calendar built-in function return date in 124022 nenoseconds

Output Sample 5:

loop_return_date_only in 22536 nenoseconds
map_function_return_list in 18696 nenoseconds
list_comperehension_return_list in 12612 nenoseconds
all_fields_related to nth_weekday_index in 9552 nenoseconds
Calendar built-in function return date in 125858 nenoseconds

Output Sample 6:

loop_return_date_only in 22188 nenoseconds
map_function_return_list in 18409 nenoseconds
list_comperehension_return_list in 12000 nenoseconds
all_fields_related to nth_weekday_index in 9553 nenoseconds
Calendar built-in function return date in 122486 nenoseconds

Output Sample 7:

loop_return_date_only in 22236 nenoseconds
map_function_return_list in 19009 nenoseconds
list_comperehension_return_list in 11832 nenoseconds
all_fields_related to nth_weekday_index in 9624 nenoseconds
Calendar built-in function return date in 124514 nenoseconds

Output Sample 8:

loop_return_date_only in 21889 nenoseconds
map_function_return_list in 19296 nenoseconds
list_comperehension_return_list in 11881 nenoseconds
all_fields_related to nth_weekday_index in 9636 nenoseconds
Calendar built-in function return date in 125473 nenoseconds

Output Sample 9:

loop_return_date_only in 22632 nenoseconds
map_function_return_list in 18565 nenoseconds
list_comperehension_return_list in 12504 nenoseconds
all_fields_related to nth_weekday_index in 9721 nenoseconds
Calendar built-in function return date in 123338 nenoseconds





Output Sample 10:

loop_return_date_only in 21852 nenoseconds
map_function_return_list in 18553 nenoseconds
list_comperehension_return_list in 12348 nenoseconds
all_fields_related to nth_weekday_index in 148275 nenoseconds
Calendar built-in function return date in 186350 nenoseconds

Guess we have 2 year date inputs with running temporal_processing.py filename

5: Generate 2 years table.

Then
(venv) k@k:~/Documents/current_work/temporal-dimension/temporal_dimension$ python retrieve_data.py

Output Sample 1:

loop_return_date_only in 23808 nenoseconds
map_function_return_list in 18876 nenoseconds
list_comperehension_return_list in 12228 nenoseconds
all_fields_related to nth_weekday_index in 9900 nenoseconds
Calendar built-in function return date in 126313 nenoseconds

Output Sample 2:

loop_return_date_only in 27780 nenoseconds
map_function_return_list in 21960 nenoseconds
list_comperehension_return_list in 12660 nenoseconds
all_fields_related to nth_weekday_index in 9816 nenoseconds
Calendar built-in function return date in 125845 nenoseconds

Output Sample 3:

loop_return_date_only in 23868 nenoseconds
map_function_return_list in 19584 nenoseconds
list_comperehension_return_list in 12744 nenoseconds
all_fields_related to nth_weekday_index in 9732 nenoseconds
Calendar built-in function return date in 127273 nenoseconds

Output Sample 4:

loop_return_date_only in 26736 nenoseconds
map_function_return_list in 20676 nenoseconds
list_comperehension_return_list in 12888 nenoseconds
all_fields_related to nth_weekday_index in 9792 nenoseconds
Calendar built-in function return date in 124153 nenoseconds

Output Sample 5:

loop_return_date_only in 24192 nenoseconds
map_function_return_list in 19632 nenoseconds
list_comperehension_return_list in 12372 nenoseconds
all_fields_related to nth_weekday_index in 9552 nenoseconds
Calendar built-in function return date in 126421 nenoseconds

Output Sample 6:

loop_return_date_only in 24577 nenoseconds
map_function_return_list in 18865 nenoseconds
list_comperehension_return_list in 12432 nenoseconds
all_fields_related to nth_weekday_index in 10428 nenoseconds
Calendar built-in function return date in 195122 nenoseconds

Output Sample 7:

loop_return_date_only in 24600 nenoseconds
map_function_return_list in 18997 nenoseconds
list_comperehension_return_list in 12240 nenoseconds
all_fields_related to nth_weekday_index in 9480 nenoseconds
Calendar built-in function return date in 128029 nenoseconds

Output Sample 8:

loop_return_date_only in 25333 nenoseconds
map_function_return_list in 18660 nenoseconds
list_comperehension_return_list in 12240 nenoseconds
all_fields_related to nth_weekday_index in 9984 nenoseconds
Calendar built-in function return date in 126505 nenoseconds




Output Sample 9:

loop_return_date_only in 25261 nenoseconds
map_function_return_list in 19320 nenoseconds
list_comperehension_return_list in 12216 nenoseconds
all_fields_related to nth_weekday_index in 10092 nenoseconds
Calendar built-in function return date in 124862 nenoseconds

Output Sample 10:

loop_return_date_only in 25488 nenoseconds
map_function_return_list in 19740 nenoseconds
list_comperehension_return_list in 12744 nenoseconds
all_fields_related to nth_weekday_index in 10488 nenoseconds
Calendar built-in function return date in 129193 nenoseconds

With these profiling we can say that all_fields function is more improved. Then list comprehension function, then map function, then loop and last main nth_weekday function in workalendar. Here we see only the time consumed by those function. We do not see the other factors as cProfile. For getting nanoseconds we use python 3.8. Nanoseconds is available from python 3.7.