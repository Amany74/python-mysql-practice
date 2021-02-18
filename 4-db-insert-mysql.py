import mysql.connector

myconnect = mysql.connector.connect(
    host = "localhost" ,
        user = '',  # add mysql user name
    password = '', #add mysql user password
    database ="mydb1"
)


mycursor = myconnect.cursor()
sql = "INSERT INTO movies(name , plot) VALUES(%s,%s)"
data = ("now you see me" , "adventrous moview")
data = ("spider man" , "adventurous moview")
data = ("snowden" , "adventurous moview")
mycursor.execute(sql , data)
print("data iserted successfully")

# the print statment executed successfully but nothing appeared 
# we didn't commit the changes

#commit
myconnect.commit()
print("commited")

# we can insert a list of data instead of one by one insertion

newdata = [
    ("Extraction" , "action") ,
    ("the dark tower" , "action") ,
    ("aquaman" , "fantasy")
]

mycursor.executemany(sql , newdata)
print(mycursor.rowcount)
#last inserted element id
print(mycursor.lastrowid) #id returned if we have column id with autoincrement in our database

myconnect.commit()
