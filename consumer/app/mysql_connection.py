import mysql.connector


mysql_conn = mysql.connector.connect(
    host="mysql",
    user="mysql",
    password="mysql",
    database="test_17"
)
cursor = mysql_conn.cursor()

