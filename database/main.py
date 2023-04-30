"""
CS425 Spring 2023 Final Project
Tiffany Kashima
----
Real Estate Database and Rental Application using Python, Django, and PostgreSQL
----
TO DO:
Create function for SQL in python with psycopg2
Connect to database (double check in pgadmin)
Create database and tables (PostgreSQL and Python)
Create query logic
Create REST API in Django
Build front end with VUE
Testing
Comment Code
Push to repo on github
Video Walkthrough

COMPLETED: 
"""

# Create python functions to connect to PostgreSQL database

import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Create function to create database in PostgreSQL

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# Create function to execute SQL queries (create tables and insert records, update records, delete records)

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# Create function to execute SQL queries (read database, select records, and return results)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


import pandas as pd

data = [10,20,30,40,50,60]

df = pd.DataFrame(data, columns=['Numbers'])

df

