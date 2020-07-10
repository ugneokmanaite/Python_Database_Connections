import pyodbc

# what we will need for establishing database connection
# variables established

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# specifying the ODBC driver, server name, database, etc directly
# instead of local host on provided link we CONCAT'ed the server variable

connection_string = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')
# connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = connections.cursor()
try:
    with pyodbc.connect(connectionString, timeout=20) as connection:
        print("Connection did not time out")
except:
    print("Connection Timed out")
else:
# acquire a cursor from connection to execute the codethrough
# cursor moves as you execute the code
# create a cursor from the connection
# this is part of else - if connection is ok it will go to else part
    cursor = connection.cursor()
    print(connection)
    print(cursor)

import pyodbc
# server = 'databases2.spartaglobal.academy'
# database = 'Northwind'
# username = 'SA'
# password = 'Passw0rd2018'
#
# # import pyodbc
# server = 'databases2.spartaglobal.academy'
# #databases2.spartaglobal.academy
# database = 'Northwind'
# username = 'SA'
# password = 'Passw0rd2018'
# connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = connections.cursor()
# print(connections)
# print(cursor)