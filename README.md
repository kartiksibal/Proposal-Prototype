# Proposal-Prototype

Scraper scrapes data from Ubuntu's bug tracker. Stores the scraped data into a PostgreSql database using Psycopg2 as ORM and can update the data whenever the user wants. 

It scrapes the following data:

1. CVE Id.
2. Package Name.
3. Vulnerability Status.

You can run it, simply by changing your directory and entering `python db.py`
