import mysql.connector


# connecting to databases in MYSQL

myconnect = mysql.connector.connect (
    host = "localhost" ,
    user = '',  # add mysql user name
    password = '', #add mysql user password
    database ="mydb1"
)

mycursor = myconnect.cursor()
print("connected")

# create new table student to try where 
# mycursor.execute("CREATE TABLE student (name VARCHAR(50) , age int(10) )")

# print("table created successfully")




# insert some data
# sql = "INSERT INTO student(name , age) VALUES(%s,%s)"
# newdata = [
#     ("berry" , 25) ,
#     ("boom" , 15)
# ]
# mycursor.executemany(sql , newdata)
# myconnect.commit()
# print("done")



# return data >= 20

mycursor.execute ("SELECT * FROM student  WHERE age >= 20")
result = mycursor.fetchall()
print(result)  # values returned successfully









