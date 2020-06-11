import psycopg2
from dotenv import load_dotenv
import os

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)

print("CONNECTION", type(connection))


cursor = connection.cursor()
print("CURSOR", type(cursor))


cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()

print(result)


insertion_sql= "INSERT INTO test_table (name, data) VALUES(%s, %s)"

cursor.execute(insertion_sql, ("A Row", "null"))

connection.commit()

cursor.close()
connection.close()