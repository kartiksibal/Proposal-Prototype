import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class Database:

	def __init__ (self, user_name, user_password, db_name):

		self.user_name = user_name
		self.user_password = user_password
		self.db_name = db_name

	def conn_establish(self):
		"""Tries to establish connection to the DB"""
		try:
			conn = psycopg2.connect(database=self.db_name, user=self.user_name, password=self.user_password, host="127.0.0.1", port="5432")
			print "Connection Successfull"
		except psycopg2.DatabaseError as error: print error

	def new_db(self):
		"""Creates a new DB to add the table in"""
		##Add: A check. The user shouldn't enter the name of an existing DB
		con = None

		try:
			con = psycopg2.connect(database="postgres", user=self.user_name, password=self.user_password, host="127.0.0.1", port="5432")
			con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
			cur = con.cursor()
			cur.execute("CREATE DATABASE " + db_name)	
			cur.close()
			con.close()
		
		except psycopg2.DatabaseError as error: print error

	def create_table(self):
		"""Initialises a new table"""
		conn = None

		try:
			con = psycopg2.connect(database=self.db_name, user=self.user_name, password=self.user_password, host="127.0.0.1", port="5432")
			cur = con.cursor()
			cur.execute("CREATE TABLE vuln_data ( cve_id text, pkg_name text, status text)")	
			con.commit()
			con.close()
		
		except psycopg2.DatabaseError as error: print error

	def first_insert(self):
		"""Scrapes data, adds to the table"""
		count = 0
		conn = None
		
		try:
			conn = psycopg2.connect(database=self.db_name, user=self.user_name, password=self.user_password, host="127.0.0.1", port="5432")
			cur = conn.cursor()

			"""
			What will be a better approach to do this?
			It is taking the list of cve id, package name and status
			and adding it into to the table 'vuln_data'
			"""
			print "Scraping Data!"

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
