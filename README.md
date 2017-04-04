# Proposal-Prototype

Scraper scrapes data from Ubuntu's bug tracker. Stores the scraped data into a PostgreSql database using Psycopg2 as ORM and can update the data whenever the user wants. 

It scrapes the following data:

1. CVE id.
2. Package Name.
3. Vulnerability Status.

Additional Features:

1. It can create a DB for you and then dump the data.
2. It can create a table and dump the data, in an already present DB.
3. As and when more data sources are added, the user will be given an option to decide the datasets that they require.

You can run it, simply by changing your directory and entering `python main.py`
