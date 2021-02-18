import mysql.connector


# connecting to databases in MYSQL

myconnect = mysql.connector.connect (
    host = "localhost" ,
    user = '',  # add mysql user name
    password = '', #add mysql user password
)

mycursor = myconnect.cursor()
print("connected")
# mycursor.execute("SHOW DATABASES")






