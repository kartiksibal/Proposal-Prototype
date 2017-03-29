from scanner import *
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import time
import os

class database:

	def __init__ (self, user_name, user_password, db_name):

		self.user_name = user_name
		self.user_password = user_password
		self.db_name = db_name

	def conn_establish(self):
		"""Tries to establish connection to the DB"""
		try:
			conn = psycopg2.connect(database="postgres", user=user_name, password=user_password, host="127.0.0.1", port="5432")
			print "Database Connection was successfull!!"
			return True
		except:
			##Add: Raise more detailed errors.
			print "DB Connection was un-succesfull!!"
			return False

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

	def existing_db(db_name):
		"""Add: Give the user the option to add the table into an existing DB"""
		pass

	def create_table(self):
		"""Initialises a new table"""
		con = psycopg2.connect(database=db_name, user=user_name, password=user_password, host="127.0.0.1", port="5432")
		cur = con.cursor()
		cur.execute("CREATE TABLE vuln_data ( cve_id text, pkg_name text, status text)")	
		con.commit()
		con.close()

	def first_insert(self):
		"""Scrapes data, adds to the table"""
		count = 0
		conn = psycopg2.connect(database=db_name, user=user_name, password=user_password, host="127.0.0.1", port="5432")
		cur = conn.cursor()

		"""
		Advice: What will be a better approach to do this?

		It is taking the list of cve id, package name and status
		and adding it into to the table 'vuln_data'.
		"""
		for entries in cve_id:
			cur.execute("INSERT into vuln_data(cve_id, pkg_name, status) VALUES (%s, %s, %s)", (cve_id[count], 
													  pkg_name[count], 
												       vuln_status[count+1]))
			count += 1
		"""
		Also, will it be better to add the commit statement, inside the for loop? 
		Add Autocommit, instead? Is it wise to do it? 
		What will a better approach?
		"""
		conn.commit()
		conn.close()

	def update(self):
		"""Scraper scrapes new data, updates the whole darn table (temporary solution)"""
		con = psycopg2.connect(database=db_name, user=user_name, password=user_password, host="127.0.0.1", port="5432")
		cur = con.cursor()
		count = 0
		##Add: Update selected entries, instead of the whole DB.
		for entries in cve_id:
			cur.execute ("UPDATE vuln_data SET (cve_id, pkg_name, status) WHERE (%s, %s, %s)", (cve_id [count],
													  pkg_name [count],
					                                                             vuln_status [count+1]))
			count += 1
		con.commit()
		con.close()
"""
print "Welcome To the world of CVE: \n"
print "We use PostgreSql as our DB, we are expecting it to be up and running in your system\n"
time.sleep()
os.system('clear')
print ("Let's establish a connnection to your DB! \n")
user_name = raw_input ("Please enter your PostgreSql Username: ")
##FIX ME: Store the password inside .pgpass file
user_password = raw_input ("Please enter your PostgreSql Password: ")
"""
user_name = "postgres"
user_password = "123456"
db_name = "testdb"

db = database (user_name, user_password, db_name)
#db.conn_establish ()
#db.new_db()
#db.create_table()
#db.first_insert()
db.update()

"""
##If conn_establish is false, exit, continue if true
first_choice = raw_input ("Please enter a name of the new DB you'd like to create: ")
	os.system('clear')
	db_name = raw_input ("\nPlease enter the name of your existing DB: ")
	existing_db(db_name)
"""
