from db import Database
import time
import os
import getpass

clear = os.sysem('clear') # Clear screen 
sleep = time.sleep(3) # Add delay

print "Welcome To the world of CVE: \n"
print "We use PostgreSql as our DB, we are expecting it to be up and running in your system\n"
sleep
clear       

print ("Let's establish a connnection to your DB! Shall we? \n")
sleep
clear       

user_name = input ("Please enter your PostgreSql Username: ")
##FIX ME: Store the password inside .pgpass file
user_password = getpass.getpass ("\nPlease enter your PostgreSql Password: (We'll keep it secret!!) ")

dec = input("\n\nWould you like to add the data in a new DB or an existing DB? (N for new E for existing): ")

if dec == 'e' or dec == 'E':
	os.system('clear')
	db_name = input ("\nPlease enter your EXISTING DB's name!: ")
	##Add a check to see if the DB is valid.
	db = Database (user_name, user_password, db_name)

elif dec == 'N' or dec == 'n':
	os.system('clear')
	db_name = input ("\nPlease enter a name for your NEW DB: ")
	db = Database (user_name, user_password, db_name)
	db.new_db()

sleep
clear       

db.conn_establish()
print ("Database Connection Succesfull!")
time.sleep(2)
os.system('clear')

print ("Let's create a new table to store our data in!")
db.create_table()
sleep
clear       

print ("Table Created!!")
sleep
clear       

db.first_insert()
sleep
clear       

print ("Addition Complete!! We will soon be back with an option to Scan packages and even more datasets!!!\n\nCIAO!!")