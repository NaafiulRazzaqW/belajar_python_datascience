import sqlConnection



mycursor = sqlConnection.mydb.cursor()

city_name = input("Enter City Name:")
sql = "SELECT * FROM city WHERE name LIKE '%{0}%'"



mycursor.execute(sql.format(city_name))

data = mycursor.fetchall()

if data == []:
    print("student not found!")

for item in data:
    print(item)