import mysql.connector

config = {"user": "vinay",
          "password": 'drago',
          "host": 'localhost',
          "database": 'test_python_db'
          }

# cnx = mysql.connector.connect(**config)
# cursor = cnx.cursor()
# query = """SELECT * FROM student"""
# cursor.execute(query)
# for id, name in cursor:
#     print("id: ", id, ", name: ", name, sep="\t")
# cnx.close()

with mysql.connector.connect(**config) as cnx:
    cursor = cnx.cursor()
    query = """SELECT * FROM student"""
    cursor.execute(query)
    for id, name in cursor:
        print("id: ", id, ", name: ", name, sep="\t")

