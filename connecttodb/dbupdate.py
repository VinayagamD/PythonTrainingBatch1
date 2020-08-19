import mysql.connector

config = {"user": "vinay",
          "password": 'drago',
          "host": 'localhost',
          "database": 'test_python_db'
          }

with mysql.connector.connect(**config) as cnx:
    cursor = cnx.cursor()
    query = "UPDATE student SET name = (%s) WHERE id = (%s) "
    val = ("adithya", 9)
    cursor.execute(query, val)
    cnx.commit()

with mysql.connector.connect(**config) as cnx:
    cursor = cnx.cursor()
    query = "DELETE FROM student WHERE id = (%s)"
    val = (5,)
    cursor.execute(query, val)
    cnx.commit()
