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
			conn = psycopg2.connect(database=self.db_name, user=self.user_name, 
														   password=self.user_password, 
														   host="127.0.0.1", 
														   port="5432")

		except psycopg2.DatabaseError as error: 
								print (error)

	def new_db(self):
		"""Creates a new DB to add the table in"""
		#Add: A check, the user shouldn't enter the name of an existing DB
		con = None

		try:
			con = psycopg2.connect(database="postgres", user=self.user_name, 
														password=self.user_password, 
														host="127.0.0.1", 
														port="5432")

			con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
			cur = con.cursor()
			cur.execute("CREATE DATABASE " + self.db_name)	
			cur.close()
			con.close()
		
		except psycopg2.DatabaseError as error: 
						print (error)

	def create_table(self):
		"""Initialises a new table"""
		con = None

		try:
			con = psycopg2.connect(database=self.db_name, user=self.user_name, 
														  password=self.user_password, 
														  host="127.0.0.1", 
														  port="5432")
			cur = con.cursor()
			cur.execute("CREATE TABLE vuln_data ( cve_id text, pkg_name text, status text)")	
			con.commit()
			con.close()
		
		except psycopg2.DatabaseError as error: 
							print (error)

	def first_insert(self):
		"""Scrapes data, adds to the table"""
		conn = None
		
		try:
			conn = psycopg2.connect(database=self.db_name, user=self.user_name, 
														   password=self.user_password, 
														   host="127.0.0.1", 
														   port="5432")
			cur = conn.cursor()
			print ("Scraping Data!")
			
			import scanner as sc
			sc.ubuntu_data()
			sc.debian_data() 
			
			for entries in range(len(sc.cve_id)):
				cur.execute("INSERT into vuln_data(cve_id, pkg_name, status) VALUES (%s, %s, %s)",(sc.cve_id[entries], 
																									sc.pkg_name[entries], 
																									sc.vuln_status[entries]))
			conn.commit()
			conn.close()
		
		except psycopg2.DatabaseError as error: 
					print (error)
	
	def update(self):
		"""Scraper scrapes new data, updates the whole darn table (temporary solution)"""
		pass

		"""
		#FIX ME: Ineffective Solution
		
		con = psycopg2.connect(database=db_name, user=user_name, password=user_password, host="127.0.0.1", port="5432")
		cur = con.cursor()
		count = 0
		
		for entries in len(cve_id):
			cur.execute ("UPDATE vuln_data SET (cve_id, pkg_name, status) WHERE (%s, %s, %s)", (cve_id [entries], pkg_name [entries], vuln_status [entries+1]))
		
		con.commit()
		con.close()
		"""
