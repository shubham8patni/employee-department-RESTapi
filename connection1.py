import psycopg2
from psycopg2 import Error

    # Connect to an existing database
mydb = psycopg2.connect(user="yxotjihxsyumjh",
                                  password="f5fb53d0e77282b9c6adf88df1f1d57e0075ca32154daf7a8144a7573ee0c9ba",
                                  host="ec2-44-194-92-192.compute-1.amazonaws.com",
                                  port="5432",
                                  database="d4de2v036i6s0d")

#     # Create a cursor to perform database operations
# cursor = connection.cursor()
#     # Print PostgreSQL details
# print("PostgreSQL server information")
# print(connection.get_dsn_parameters(), "\n")
#     # Executing a SQL query
# cursor.execute("SELECT version();")
#     # Fetch result
# record = cursor.fetchone()
# print("You are connected to - ", record, "\n")

# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "ShubhamPatni8.mysql.pythonanywhere-services.com",
#     user = "ShubhamPatni8",
#     password="mysql123",
#     database = "pythonsql"
# )