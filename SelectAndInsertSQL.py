import mysql.connector
import sqlConnection 



mycursor = sqlConnection.mydb.cursor()

mycursor.execute('SELECT * FROM city')

myresult1 = mycursor.fetchone() 
myresult2 = mycursor.fetchall()
print(myresult2, "Data City")

# insert sql

sql = "INSERT INTO city (admin_id, name) VALUES ( %s, %s )"
val = (1, "Malang Raya")
mycursor.execute(sql,val)
sqlConnection.mydb.commit()


print(mycursor.rowcount, "record inserted")