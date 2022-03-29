import psycopg2
from psycopg2 import Error

    # Connect to an existing database
mydb = psycopg2.connect(user="cynzshhfetztxo",
                                  password="a7cf3ab8563977c70b95acbb339573d5af88b9c831dd7bc1d7db764f46a7af08",
                                  host="ec2-52-3-60-53.compute-1.amazonaws.com",
                                  port="5432",
                                  database="dd97uhqd2of83n")

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