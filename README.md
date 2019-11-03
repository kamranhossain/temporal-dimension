Temporal Dimension
==================

Processing temporal dimension data for human

Project Concept
---------------
For project concept check the CONCEPT.md file.

Requirements
------------
1.  Python 3+
2.  pydblite


Installation on Development Machine
-----------------------------------

Download code from github: git clone https://github.com/kamranhossain/temporal-dimension.git

To run the app on your local machine, you need Python 3.6+ and pydblite(in-memory database engine) installed on your computer.

1.  Create and activate virtualenv:

        python3 -m venv venv
        . venv/bin/activate

2.  Install the packages

        pip install -r requirments.txt

3.  Run program

        python temporal_processing.py
        (temporal_processing.py program will generate tables of dates and related infoes)

4.  Test with valid input date

        Inputs example: 
        Enter start date with format mm/dd/yyyy:  01/01/2010
        How many years of data(after start date): 2
        Which Country: UnitedStates
        Which State:

    Here start date = 01/01/2010 and
    Numbers of years = 2 are given input.
    Give the country name(must)
    Give the state name(optional)

    Caution:This packages support all the country and state in workalendar until version 7.0.0. Adding new country and states will be on going process.

    Form those three or four inputs calculate process temporal data between start and end date range. And generate in-memory DB data temporal_data.pdl and temporal_data.csv file

5. Test with invalid input date:

    Check date input(mm/dd/yyyy) is valid or not.The input prompt is coming until valid input.Here is an example.

        Enter start date with format mm/dd/yyyy: 31/31/2017
        Invalid date!.Please enter valid date
        Enter start date with format mm/dd/yyyy:
        Same way to check integer year, valid Country and State
        
6. Access data using index field.

    Here date ,julian date num and sequence are index fields.
    goto python command line and write 
    
        python
    
    from python interpreter import Base from pydblite
    
        >>> from pydblite import Base
    
    assign temporal_data.pdl to date_table
    
        >>> date_table=Base('temporal_data.pdl') 
    
    open date_table

        >>> date_table.open()
    
    search with julian date number
    
        >>> date_table._julian_date_num[10215]
    
    search with sequence number
    
        >>> date_table._sequence[214]

7.  There are more files like time_processing.py and retrieve_data.py.
    time_processing.py generate csv file of temporal time of 24 hours as business purspective.
    retrieve_data.py is the functions for retrieving data from in memory DB table to get data faster than function.

    There are also profiling folder where checking performance of function calling from direct library and also retrieve from in-memory DB. cProfile and time_ns(3.7+) use for checking function calls and checking performance and time uses.

Sponsors
--------
BaiB Oy, Turku Finland  https://www.baib.co.ke/
Interspeed Digital, Dhaka Bangladesh  https://interspeeddigital.com/