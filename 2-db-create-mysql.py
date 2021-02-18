import mysql.connector


# connecting to databases in MYSQL

myconnect = mysql.connector.connect (
    host = "localhost" ,
    user = '',  # add mysql user name
    password = '', #add mysql user password
)

mycursor = myconnect.cursor()
print("connected")
# mycursor.execute("CREATE DATABASE mydb1 ")  #excuted successfully - mydb1 is now in mysql

mycursor.execute("SHOW DATABASES")

# printing db names

for db in mycursor :
    print(db)
    
    
#check if database exist or not by trying to connect with 

# myconnect = mysql.connector.connect (
#     host = "localhost" ,
#     user = 'root', 
#     password = 'root',
#     database="cars"  #ERROR : Unknown database 'cars'
# )
