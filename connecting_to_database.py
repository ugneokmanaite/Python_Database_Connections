# importing class created
from database_OOP import database_OOP

import os

# connection variables stored for privacy
server = os.environ.get('db_server')
database = os.environ.get('db_database')
username = os.environ.get('db_username')
password = os.environ.get('db_password')

# OOP
# asking for user input to know what command can be established
user_input = int(input("Please enter the number for the operation you want us to execute::"

                     "\n 1. Fetch one row \n 2. Fetch many rows \n 3. Fetch All rows \n 4. Display AVG unit price \n"))

# instance created for connection variables
data_oop = database_OOP(server, database, username, password)

# establishing connection
oop_connection = data_oop.establish_connection()

# executing SQL commands
data_oop.execute_sql('SELECT * FROM Products', oop_connection, user_input)




#Assignment:-Calculate the average unit price of all the products



