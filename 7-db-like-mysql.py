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




mycursor.execute ("SELECT * FROM movies  WHERE name like 'Extraction%'") #use %value% to filter on specific value
result = mycursor.fetchone()
# result = mycursor.fetchall()
print(result)  # values returned successfully
