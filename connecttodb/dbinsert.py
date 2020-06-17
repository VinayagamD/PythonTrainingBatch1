import mysql.connector

config = {"user": "vinay",
          "password": 'drago',
          "host": 'localhost',
          "database": 'test_python_db'
          }

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
query = "INSERT INTO student (name) VALUES (%s)"
val = ("vinay",)
cursor.execute(query, val)
cnx.commit()
print(cursor.rowcount, "record inserted.")

