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


# ordering data in students by age 

mycursor.execute("SELECT * FROM student ORDER BY age  DESC") 
result = mycursor.fetchall()
print(result)  # default ascendingly



# if we want to specify limit to values returned
mycursor.execute("SELECT * FROM movies LIMIT 5 ") 
result = mycursor.fetchall()
print(result)  # default ascendingly


# if we want to specify limit to values returned with rande (for example : start from third row )
mycursor.execute("SELECT * FROM movies LIMIT 5  OFFSET 3") 
result = mycursor.fetchall()
print(result)  # default ascendingly