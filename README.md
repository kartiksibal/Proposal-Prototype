# Proposal-Prototype

Scraper scrapes data from bug trackers. Stores the scraped data into a PostgreSql database using Psycopg2 as ORM and can update the data whenever the user request. 

__It scrapes the following data:__

1. CVE ID.
2. Package Name.
3. Vulnerability Status.

__Additional Features:__

1. Interactive applcation  
2. It can create a DB for you and then dump the data.
3. It can create a table and dump the data, in an already present DB.
4. As and when more data sources are added, the user will be given an option to decide the datasets that they require.

You can run it, simply by changing your directory and entering `python main.py`

__Datasets:__

1. Debian
2. Ubuntu

__To DO__:
1. Add test cases

