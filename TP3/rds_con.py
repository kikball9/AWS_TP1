import mysql.connector

connection = mysql.connector.connect(
    host="mysql-1-group16.cpkkieyem23g.us-east-1.rds.amazonaws.com",
    user="admin",
    password="isen2025",
    database="cloud"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM presta;")
# connection.commit()

for row in cursor.fetchall():
    print(row)

connection.close()
