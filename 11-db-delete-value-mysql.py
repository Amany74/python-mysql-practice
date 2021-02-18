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



mycursor.execute("DELETE FROM movies WHERE name = 'NEW' ")
myconnect.commit()  # all values carrying new replaced



# delete based on user input 
sql  = "DELETE FROM movies  WHERE  name =%s "
data = ( 'aquaman' ,) #don't forget the comma
mycursor.execute(sql , data)
myconnect.commit()
print('deleted successfuly')
