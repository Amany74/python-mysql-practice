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




sql = "SELECT * FROM movies  WHERE name=%s"
data = ('Extraction',) #we added , to make it tuple 
mycursor.execute(sql,data)
result = mycursor.fetchall()
print(result)  # values returned successfully

