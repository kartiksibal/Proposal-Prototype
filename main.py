from db import Database
import time
import os
import getpass

user_name = "postgres"
user_password = "123456"
db_name = "testdb"

db3 = Database(user_name, user_password, db_name)

db3.conn_establish()

"""
print "Welcome To the world of CVE: \n"
print "We use PostgreSql as our DB, we are expecting it to be up and running in your system\n"
time.sleep(3)
os.system('clear')

print ("Let's establish a connnection to your DB! Shall we? \n")
time.sleep(2)
os.system('clear')
"""

 #= raw_input ("Please enter your PostgreSql Username: ")
##FIX ME: Store the password inside .pgpass file
 #= getpass.getpass ("\nPlease enter your PostgreSql Password: (We'll keep it secret!!) ")

#dec = raw_input("\n\nWould you like to add the data in a new DB or an existing DB? (N for new E for existing): ")


# import pdb;
# pdb.set_trace();




"""
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


"""