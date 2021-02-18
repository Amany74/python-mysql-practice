import mysql.connector


# connecting to databases in MYSQL

myconnect = mysql.connector.connect (
    host = "localhost" ,
        user = '',  # add mysql user name
    password = '', #add mysql user password
    database ="mydb1"
)

mycursor = myconnect.cursor()
mycursor.execute("SELECT * FROM movies")
result = mycursor.fetchall()

#retrieving data

for x in result :
    print(x)
    
    
# retrieve specific columns 
#return name column only 
mycursor.execute("SELECT name FROM movies")
result = mycursor.fetchall()
for x in result :
    print(x)




# return one row  ---- excute it alone 
mycursor.execute("SELECT name FROM movies")
result = mycursor.fetchone()
for x in result :
    print(x)


# we can return values with list by not looping on the cursor -- excute alone
# this is helpful to slice data 
mycursor.execute("SELECT name , plot FROM movies")
result2 = mycursor.fetchall()
print(result2)
