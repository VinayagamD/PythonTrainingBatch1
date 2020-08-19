import mysql.connector
config = {"user": "vinay",
            "password": 'drago',
            "host": 'localhost',
            "database": 'test_python_db'
            }

cnx = mysql.connector.connect(**config)

try:
    cursor = cnx.cursor()
    query = "INSERT INTO student (name) VALUES (%s)"
    val = ("vinay",)
    cursor.execute(query, val)
    cnx.commit()
    print(cursor.rowcount, "record inserted.")

except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
    cnx.rollback()
finally:
    cnx.close()
