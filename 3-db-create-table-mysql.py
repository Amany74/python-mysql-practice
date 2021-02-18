import mysql.connector


# connecting to databases in MYSQL

myconnect = mysql.connector.connect (
    host = "localhost" ,
    user = '',  # add mysql user name
    password = '', #add mysql user password
    database ="mydb1",
)

mycursor = myconnect.cursor()
print("connected")
 mycursor.execute("CREATE TABLE movies (name VARCHAR(100) , plot VARCHAR(500) )")

 print("table created successfully")





