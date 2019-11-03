# Abstract

This is a concise description:

**The technical problem area:**

1. Temporal dimension processing is common in Data Marts, Data Warehouses, and Databases that record events.  This is different than Time Series Databases, or Stream processing, which have many similarities but those are more concerned with time ticks like in financial systems or in logging of system activities.

2. Python has support for dates and time with many packages and modules.  These may not performance as fast as possible, they do not work for processing with databases of events since it would force record at a time processing instead of using query operations.  The many date-time packages do not have a uniform or unifying processing that considers all of the real issues with processing of dates and time.

**The conceptual problem area:**

1. Temporal databases do not address the needs present in real-world. Processing real-world events need to consider how humans might perceive dates and time.  We are more concerned with human concepts of date time than system recording of timestamps.

2. Dates and time have their own logical representations that include attributes like holidays, sleeping, working time, delays.

3. Dates and time have various banding for precisions, humans cannot perceive milli-seconds and may not have clocks that are synchronized, the logical operations may need to consider timezones, banding for time as to whether it is minutes, every 20 minutes, every hour, or day or few days or quarter.  Many bands are the equivalent of precision or temporal dimension.

**The logical problem scenarios** :

1. three people who lives in three different timezones are working together, they need to have a periodic meeting, when is the best dates and times for those meetings to occur so that they are most productive, are fair to the cultural and lifestyle preferences, and would allow eac person to be productive.

2. Multiple packages of material needs to be ordered and delivered within a time span so that they can be assembled, they are perishable goods like foods that cannot be stored for long, so the delivery needs to happen within some optimal time banding for it to work.  It is in an environment where the transportation traffic is unreliable and the people are not reliable so what precisions is reasonable, likely, and effective and what are the best times of day for this to be coordinated.  Then plan needs to adjust in real-time as the activity happens and more information is known.



**The foundational technical implementation solution**

1. pre-calculate all dates and time for some duration, the dates, time, holidays, date attributes, and all the possible formats for dates and time are finite and known and thus can be pre-calculated and cached in-memory such that it would increase the performance of any optimization processes that used it.

2. Implement a set of functions in Python that support Allen intervals that performs fast at the minimal amount of computing cycles and can be used with any optimization processes, be it Machine learning or Linear programming.  The diagram below visualizes this simply, the table give the formal semantics need to be programmed.

3. create this as a python package

**The opportunity**

1. to create a consolidated python package that addresses this area using existing open source, modules within python, but recoding it for performance and to provide the real-world processing.

2. If someone is interested in research, this topic is wide open and available to apply to optimization processes be it Linear programming or Machine learning and it has not been adequately addressed by academia or commercial products, so it is both interesting for research and has the potential for creating commercial solutions in the future.

## Background

Temporal dimension processing is common in Data Marts, Data Warehouses, and Databases that record events.  This is different than Time Series Databases, or Stream processing, which have many similarities but those are more concerned with time ticks like in financial systems or in logging of system activities.

Just for processing national holidays it can be a challenge.  
See: [https://www.vertabelo.com/blog/technical-articles/viewing-holidays-with-data-modelers-eyes](https://www.vertabelo.com/blog/technical-articles/viewing-holidays-with-data-modelers-eyes)  where they try and model just this aspect of the problem so that it can be queried as data.

See: [https://en.wikipedia.org/wiki/Temporal\_database](https://en.wikipedia.org/wiki/Temporal_database)  which describes it as time so it does not present the real-world logical issues that are needed for processing real-world events and how humans might perceive dates and time.  We are more concerned with human concepts of date time than system recording of timestamps.

Read: [https://en.wikipedia.org/wiki/Allen%27s\_interval\_algebra#Relations](https://en.wikipedia.org/wiki/Allen%27s_interval_algebra#Relations) to understand how reasoning across temporal dimensions require special processing and modeling to address the sets of data to be retrieved  see: [https://memim.com/allen%27s-interval-algebra.html](https://memim.com/allen%27s-interval-algebra.html)

**An Ontology for Temporal dimension** [https://www.w3.org/TR/2017/REC-owl-time-20171019/#motivation](https://www.w3.org/TR/2017/REC-owl-time-20171019/#motivation)  this can implement Allen interval algebra

**Python Modules**

- --dateutl module [http://labix.org/python-dateutil](http://labix.org/python-dateutil)
- --for calendar [https://pymotw.com/2/calendar/index.html#module-calendar](https://pymotw.com/2/calendar/index.html#module-calendar)
- --for timezone  [http://pytz.sourceforge.net/](http://pytz.sourceforge.net/)
- --For date formatting [https://appdividend.com/2019/01/29/python-date-format-tutorial-how-to-format-date-example/](https://appdividend.com/2019/01/29/python-date-format-tutorial-how-to-format-date-example/)
- --For parsing dates [https://dateparser.readthedocs.io/en/latest/](https://dateparser.readthedocs.io/en/latest/)
- --This is a date parser/formatting module example [https://github.com/stestagg/dateformat](https://github.com/stestagg/dateformat)
- --Date formats by country [https://en.wikipedia.org/wiki/Date\_format\_by\_country](https://en.wikipedia.org/wiki/Date_format_by_country)  note that it shows the few possibilities but the rest can be generated.  Focus on US, UK, Germany, as examples formats to generate for the date table. This is a full table by country
  - --This file can be used to generate many formats for the countries [https://gist.github.com/mlconnor/1887156](https://gist.github.com/mlconnor/1887156)

**Python datastore**

- --Consider using a fast python database inmemory since the point of all this is to have a fast implementation for use with python but also with a datawarehouse for the generated date table  [https://pydblite.readthedocs.io/en/latest/benchmarks.html](https://pydblite.readthedocs.io/en/latest/benchmarks.html)   Or something like one of these [https://opensourceforu.com/2017/05/three-python-databases-pickledb-tinydb-zodb/](https://opensourceforu.com/2017/05/three-python-databases-pickledb-tinydb-zodb/)  it is small dataset so this needs to be very fast, in memory.

**Temporal Date file changes**

So some of this is not only for processing efficiency, the temporal processing cannot  be done without doing the below and anything not done is then a limitation on the processing.

- --Date Dimension data file [http://www.ipcdesigns.com/dim\_date/index.html#tabledef](http://www.ipcdesigns.com/dim_date/index.html#tabledef)  can be downloaded from the site and it has the explanations.  Or use the one I sent in an email, start with the one that is most complete and has the documentation with it.

- Julian day for date difference and calculations - this is a way to do calculations on last # of days or to calculate how many days have passed without record counting which would be inefficient.  Without this many temporal processing can&#39;t be done.  [https://en.wikipedia.org/wiki/Julian\_day](https://en.wikipedia.org/wiki/Julian_day)

- Treatment of Common Date type for SQL
  - [https://docs.microsoft.com/en-us/sql/t-sql/functions/date-and-time-data-types-and-functions-transact-sql?view=sql-server-2017](https://docs.microsoft.com/en-us/sql/t-sql/functions/date-and-time-data-types-and-functions-transact-sql?view=sql-server-2017)
  - [https://cloud.google.com/bigquery/docs/reference/standard-sql/date\_functions](https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions)

- pre-generate all common date formats for US and EU (see above) so queries and query results can be expressed in whatever way someone decides they want the output, this is necessary when trying to combine with external data where the date may not be typed and insert be as a string and the detection and transformation was not done to convert it to a date type when loading, this is a very common problem.

- Oracle Date Formats [https://docs.oracle.com/cd/E41183\_01/DR/Date\_Format\_Types.html](https://docs.oracle.com/cd/E41183_01/DR/Date_Format_Types.html)

- Examples of date formats to generate [https://devhints.io/datetime](https://devhints.io/datetime)

 - Examples of functions supported by Oracle for dates [https://docs.oracle.com/cd/E41183\_01/DR/Date\_Functions.html#DALc02a\_2726006080\_11805](https://docs.oracle.com/cd/E41183_01/DR/Date_Functions.html#DALc02a_2726006080_11805)

 - Formatting options for Sql Server [https://www.mssqltips.com/sqlservertip/1145/date-and-time-conversions-using-sql-server/](https://www.mssqltips.com/sqlservertip/1145/date-and-time-conversions-using-sql-server/)

These are data related to dates that would have other tables that reference the date table.  Create a simple ER Diagram for the relationships between the data.

- Common day categories, i.e. weekends, this varies by culture, country, and religion but the common ones are Sat/Sun, Fri/Sat, only sun, 1/2 sat-then Sunday

- National holiday schedule, Capital stock market calendar   -- these are serious since for example without knowing the Chinese calendar is it not possible to understand the news related to China or India calendar for each country.   China has entire weeks and months where work slows down.

- Religious calendars - some countries and cultures strictly observe their religious calendars regardless of the politics of the country and this directly impacts the topics of the news from and about those countries.

- --Some Python/JS implementations
  - [https://github.com/peopledoc/workalendar](https://github.com/peopledoc/workalendar)
  - [https://github.com/dr-prodigy/python-holidays](https://github.com/dr-prodigy/python-holidays)
  - [https://github.com/commenthol/date-holidays#data](https://github.com/commenthol/date-holidays#data)

- Language - we have this issue already with date detection, so any date table that hasn&#39;t translated the labels for months and days will not work for non-English task workflows.



**Timezone**

- Time and temporal dimensions // Time Zone designations, abbreviations, and the distance to GMT.  This is not trivial to calculate.  This varies in the US significantly, some states like Arizona do not observe daylight saving time so it is easy to have the wrong time for data that is geolocated, which is the case for most news.

Create and Populate Time Dimension with 24 Hour+ Values - CodeProject

- [https://www.codeproject.com/Tips/642912/Create-Populate-Time-Dimension-with-Hourplus-Va](https://www.codeproject.com/Tips/642912/Create-Populate-Time-Dimension-with-Hourplus-Va)
- [https://radacad.com/script-for-creating-and-generating-members-for-time-dimension](https://radacad.com/script-for-creating-and-generating-members-for-time-dimension)

**Some options for expanding the processing:**

- [https://www.timeanddate.com/services/api/](https://www.timeanddate.com/services/api/)  they have a 3 month trial to access the API but do not state what the cost is afterwards.  It might be possible to just crawl it for some data related to particular countries although it is unlikely to be complete for past and future years
- Stackoverflow posting on data sources [https://opendata.stackexchange.com/questions/1926/list-of-public-holidays-by-countries](https://opendata.stackexchange.com/questions/1926/list-of-public-holidays-by-countries)

# Design and Implementation

For the naming convention it needs some semantic and syntactic structure to be easy to understand quickly so that anyone using this could avoid mistakes.

One possible structure is  Scope first, largest to smallest, then the qualifier and Type

The scope would be year \&gt; quarter \&gt; month \&gt; day \&gt; time  the type would be num for number, name for the label, and the name can have a qualifier like short or long.  The other type might be format, which is neither a name or a number but how it is to be presented.

In one case the type might be julian\_num, or julian\_integer which would be unique and a value that can be used to do calculations so this becomes a very important value.  The rest of mostly labels, although it might type as number it is not truly an integer to calculate anything on so while this is a misnomer in this case it is acceptable if we are clear to use integer as being different from num.

It can stay with python variable naming conventions of mostly full words and underscores to separate them with the variable names as lower case.  Then the variable should be sorted in a logical order for increasing scope, so years first and day last, the type when having the same prefix would be names first then numbers.  The documentation should list out all the names and a description that explains the convention used to create the variable names and then have an example so it is easy to remember.

**Naming Conventions proposal:**

For country/language you can use one of these

- [https://pypi.org/project/country-list/](https://pypi.org/project/country-list/)
- [https://pypi.org/project/pycountry/](https://pypi.org/project/pycountry/)

To keep if very simple just use the data from these files

- [https://datahub.io/core/country-list](https://datahub.io/core/country-list)
- [https://datahub.io/core/language-codes](https://datahub.io/core/language-codes)

**Holiday Table**
country\_code
language\_code
start\_date
end\_date
holiday\_nam
holiday\_type

**Country**

1. id (Integer PK)
2. country\_name (String)

**Language**

1. id (Integer PK)
2. language\_name(String)

**translation table:**
country\_code
language\_code
temporal\_label
temporal\_value
temporal\_type  [name, short\_name, format]

The table of data has an implicit default use of English as the reference language.
Using the translation table other data can be generated in different languages.

**Date**

1. id (Integer  PK)
2.date (date)
3. julian\_date\_num (Float)
4. sequence (Integer)

**Week**
1. week\_day\_num (Integer)
2. day\_name (String)
3. day\_short\_name (String)
4. month\_week\_num (Integer)
5. month\_week\_begin\_date (Date)
6. month\_week\_end\_date (Date)
7. quarter\_week\_num (Integer)
8. quarter\_week\_begin\_date (Date)
9. quarter\_week\_end\_date (Date)
10. year\_week\_num (Integer)
11. year\_week\_begin\_date (Date)
12. year\_week\_end\_date (Date)

**Month**
1. month\_day\_num (Integer)
2. month\_num ( Integer)
3. month\_name (String)
4. month\_short\_name (String)
5. month\_begin\_date (Date)
6. month\_end\_date (Date)

**Quarter**
1. quarter\_day\_num (Integer)
2. quarter\_num (Integer)
3. quarter\_name (String)
4. quarter\_begin\_date (Date)
5. quarter\_end\_date (Date)

**Year**
1.year\_day\_num(Integer)
2. year\_num (Integer)
3. year\_begin\_date (Date)
4. year\_end\_date (Date)

**FormatedDate**
1. d\_mon\_yyyy (String)
2. d\_month\_yyyy (String)
3. mon\_d\_yyyy (String)
4. month\_d\_yyyy (String)
5. d\_m\_yyyy (String)
6. m\_d\_yyyy (String)

**Calculated**
1. weekday\_flag (1)(Integer)
2. week\_first\_day\_flag(0)(Integer)
3. week\_last\_day\_flag (1) (Integr)
4. month\_first\_day\_flag(0)(Integer)
5. month\_last\_day\_flag (1) (Integer)
6. quarter\_first\_day\_flag(0)(Integer)
7. quarter\_last\_day\_flag (0) (Integer)
8. year\_first\_day\_flag(1)(Integer)
9. year\_last\_day\_flag (0) (Integer)
10. leap\_year\_flag(1) (Integer)

# Task:
- the two files need to be consolidated so that it is all in one file but do not repeat redundant information..
- the names of the columns need some consistency to be easily understood, for example a typing convention
- the file needs additional columns generated from the dates so that various formats are already pre-calculated, this take some analysis as I gave all the links information so propose something.
- then how to store the database so that it executes very fast in memory, pickle or pydblite, this needs some testing to see which performs best.
- this has two requirements, one is some internal storage that python can query but it should also have an external CSV file that can be separately loaded for other uses like if someone wants these dimensions in a SQL database for them to query join to other data.
- then an API to call it with various functions, see above links and propose what those calls should be.  This needs a rest API and then a UX to call the various API so test it.
- then an interface to test it all, and make sure it runs very fast, to the code should be profiled and optimized.
- it should have full unit test, fully documented, lint so that it is professional python code.


# References for prior research review

this is an older research paper that give some idea of the conceptual issues and describes Allen intervals
[http://new.aaai.org/Papers/AAAI/1986/AAAI86-063.pdf](http://new.aaai.org/Papers/AAAI/1986/AAAI86-063.pdf)

Here is the theoretic problem with a more recent paper
[https://ieeexplore.ieee.org/abstract/document/1314421](https://ieeexplore.ieee.org/abstract/document/1314421)

This is an example that includes CSP
[https://ieeexplore.ieee.org/abstract/document/4811823](https://ieeexplore.ieee.org/abstract/document/4811823)

This gives another paper published in an AI journal
[https://www.sciencedirect.com/science/article/pii/S0004370206000403](https://www.sciencedirect.com/science/article/pii/S0004370206000403)

This is reference to a real-world implementation in the energy sector
[https://www.theoj.org/joss-papers/joss.00825/10.21105.joss.00825.pdf](https://www.theoj.org/joss-papers/joss.00825/10.21105.joss.00825.pdf)

This is another example of an extension of Pyomo just mostly to show that it is very commonly used now in the research community and referred to in publications but also can be extended.
[https://link.springer.com/article/10.1007/s12532-017-0127-0](https://link.springer.com/article/10.1007/s12532-017-0127-0)

This presentation show how Pyomo can use PySP for Stochastic programming and then how it can be speed-up using GPU&#39;s
[https://www.osti.gov/servlets/purl/1120428](https://www.osti.gov/servlets/purl/1120428)

This is a much more complex example but it will just show how adopting Pyomo as a toolset with the ML tools in python could open up lots of interesting research capabilities for the students as well as have it be applied to real problems.