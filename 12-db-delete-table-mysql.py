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
#table created successfuly 
# mycursor.execute("CREATE  TABLE base1 (name VARCHAR(100) )")


#deleting TABLES
mycursor.execute("DROP  TABLE base1   ")
print("deleted base1 ")
mycursor.execute("DROP TABLE  IF EXISTS base2  ") # EXCUTUES EVEN IF THERE IS NO TABLE NO ERROR
myconnect.commit()  # all values carrying new replaced



# delete based on user input 
# sql  = "DELETE FROM movies  WHERE  name =%s "
# data = ( 'aquaman' ,) #don't forget the comma
# mycursor.execute(sql , data)
# myconnect.commit()
# print('deleted successfuly')
