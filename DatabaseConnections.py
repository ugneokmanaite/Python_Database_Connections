import pyodbc

server = 'databases2.spartaglobal.academy'
#databases2.spartaglobal.academy
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' + database +';UID='+ username +';PWD='+ password)

# acquiring a curser
cursor = connections.cursor()
print(connections)
print(cursor)

# messy code because everything is happening in the same file
# hard to know why the code is failing - and where fixing needs to take place during testing

# cursor is executing and returning something
query_results = cursor.execute('SELECT * FROM Products')
print("Printing query_result object:", query_results)

# to fetch one row
# maintaints its state
# rows = query_results.fetchone()
# print(rows[1]) #second column of rows- columns start from 0th index
# # or use
# print(rows.ProductName) # same as print(rows[1])


# to fetch many
# can fetch as many as you want
# rows = query_results.fetchmany(30)
# # looping through the rows
# for row in rows:
#     # print(row) # for all
#     print(row.ProductID) # if we just want a certain column

# to fetch all rows
rows = query_results.fetchall()
