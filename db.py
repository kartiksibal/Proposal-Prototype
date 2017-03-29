import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import time
import os
import getpass

class database:

	def __init__ (self, user_name, user_password, db_name):

		self.user_name = user_name
		self.user_password = user_password
		self.db_name = db_name

	def conn_establish(self):
		"""Tries to establish connection to the DB"""
		try:
			conn = psycopg2.connect(database=db_name, user=user_name, password=user_password, host="127.0.0.1", port="5432")
			print "Connection Successfull"
			return True
		except psycopg2.DatabaseError as error: 
			print "Connection Un- Successfull!! :-(\n"
			print error

	def new_db(self):
		"""Creates a new DB to add the table in"""
		
		##Add: A check. The user shouldn't enter the name of an existing DB
		con = psycopg2.connect(database="postgres", user=user_name, password=user_password, host="127.0.0.1", port="5432")
		#Create DB can't run in a transacton block
		con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
		cur = con.cursor()
		cur.execute("CREATE DATABASE " + db_name)	
		cur.close()
		con.close()

	def create_table(self):
		"""Initialises a new table"""
		conn = None

		try:
			con = psycopg2.connect(database=db_name, user=user_name, password=user_password, host="127.0.0.1", port="5432")
			cur = con.cursor()
			cur.execute("CREATE TABLE vuln_data ( cve_id text, pkg_name text, status text)")	
			con.commit()
			con.close()
		
		except psycopg2.DatabaseError as error: 
					print error

	def first_insert(self):
		"""Scrapes data, adds to the table"""
		count = 0
		conn = None
		try:
			conn = psycopg2.connect(database=db_name, user=user_name, password=user_password, host="127.0.0.1", port="5432")
			cur = conn.cursor()

			"""
			Advice: What will be a better approach to do this?
			It is taking the list of cve id, package name and status
			and adding it into to the table 'vuln_data'
			"""
			print "Let's start scraping Ubuntu and DUMP it in our DB (evil laugh)!!!"

			from scanner import cve_id, pkg_name, vuln_status

			for entries in cve_id:
				cur.execute("INSERT into vuln_data(cve_id, pkg_name, status) VALUES (%s, %s, %s)",(cve_id[count], pkg_name[count], vuln_status[count+1]))
				count += 1
			
			"""
			Also, will it be better to add the commit statement, inside the for loop? 
			Add Autocommit, instead? Is it wise to do it? 
			What will a better approach?
			"""
			conn.commit()
			conn.close()
		
		except psycopg2.DatabaseError as error: print error
	
	def update(self):
		"""Scraper scrapes new data, updates the whole darn table (temporary solution)"""
		pass

		"""
		##FIX ME: Ineffective Solution
		
		con = psycopg2.connect(database=db_name, user=user_name, password=user_password, host="127.0.0.1", port="5432")
		cur = con.cursor()
		count = 0
		
		for entries in cve_id:
			cur.execute ("UPDATE vuln_data SET (cve_id, pkg_name, status) WHERE (%s, %s, %s)", (cve_id [count], pkg_name [count], vuln_status [count+1]))
			count += 1
		
		con.commit()
		con.close()
		"""

"""Stuff you can probably ignore"""
## Quirky sheninigans :P

print "Welcome To the world of CVE: \n"
print "We use PostgreSql as our DB, we are expecting it to be up and running in your system\n"
time.sleep(3)
os.system('clear')

print ("Let's establish a connnection to your DB! Shall we? \n")
time.sleep(2)
os.system('clear')

user_name = raw_input ("Please enter your PostgreSql Username: ")
##FIX ME: Store the password inside .pgpass file
user_password = getpass.getpass ("\nPlease enter your PostgreSql Password: (We'll keep it secret!!) ")

dec = raw_input("\n\nWould you like to add the data in a new DB or an existing DB? (N for new E for existing): ")

if dec == 'e' or dec == 'E':
	os.system('clear')
	db_name = raw_input ("\nPlease enter your EXISTING DB's name!: ")
	##Add a check to see if the DB is valid.
	db = database (user_name, user_password, db_name)

elif dec == 'N' or dec == 'n':
	os.system('clear')
	db_name = raw_input ("\nPlease enter a name for your NEW DB: ")
	db = database (user_name, user_password, db_name)
	db.new_db()

time.sleep(2)
os.system('clear')

print "Database Connection Succesfull!"
time.sleep(2)
os.system('clear')

print ("Let's create a new table to store our data in!")
db.create_table()
time.sleep(2)
os.system('clear')

print ("Table Created!!")
time.sleep(2)
os.system('clear')

db.first_insert()
time.sleep(3)
os.system('clear')

print ("Addition Complete!! We will soon be back with an option to Scan packages and even more datasets!!!\n\nCIAO!!")


