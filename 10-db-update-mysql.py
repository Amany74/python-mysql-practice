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



#Altering tables - Add new column
# mycursor.execute("ALTER TABLE movies ADD language VARCHAR(50)")
# myconnect.commit()


# alter an existing table
# mycursor.execute("ALTER TABLE movies CHANGE language  language VARCHAR(30)")

# until now we where updating the structure of the table 

# let's alter specific rows -- if we don't include where all names will be changed (be specific)
# mycursor.execute("UPDATE movies SET name = 'lol' WHERE  plot ='action'")
# myconnect.commit() #all values with plot='action' changed to lol




#user input 
sql  = "UPDATE movies SET name = %s WHERE  name =%s "
data = ('NEW' , 'snowden' )
mycursor.execute(sql , data)
myconnect.commit()


