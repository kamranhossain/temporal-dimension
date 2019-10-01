Temporal Dimension
==================

Processing temporal dimension data for human

Requirements
------------
1.  Python 3+
2.  pydblite


Installation on Development Machine
-----------------------------------

To run the app on your local machine, you need Python 3.6+ and pydblite(in-memory database engine installed on your computer.

1.  Create and activate virtualenv:

        python3 -m venv venv
        . venv/bin/activate

2.  Install the packages
    pip install -r requirments.txt

3.  Run program
    python temporal_processing.py

4.  Test with valid input date
Enter start date with format mm/dd/yyyy:  01/01/2010
How many years of data(after start date): 2

Here 
Start date = 01/01/2010 and
Numbers of years =2 are given input.


Form those two inputs calculate process temporal data between start and end date range. And generate temporal_data.pdl and temporal_data.csv

5. Test with invalid input date:
--- Check date input(mm/dd/yyyy) is valid or not.The input prompt is coming until valid input.Here is an example.

Enter start date with format mm/dd/yyyy: 31/31/2017
Invalid date!.Please enter valid date
Enter start date with format mm/dd/yyyy:

6. Access data using index field.
--- Here date ,julian date num and sequence are index fields.

goto python command line
``` $ python ```
import Base from pydblite
``` >>> from pydblite import Base ```

assign temporal_data.pdl to date_table
``` >>> date_table=Base('temporal_data.pdl') ```

open date_table
``` >>> date_table.open() ```

search with julian date number
``` >>> date_table._julian_date_num[10215] ```

search with sequence number
``` >>> date_table._sequence[214] ```
