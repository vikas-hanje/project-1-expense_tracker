import mysql.connector
import os
from dotenv import load_dotenv

def connect_DB():
    connection = mysql.connector.connect(
        host = os.getenv("DB-host"),
        user = os.getenv("DB-user"),
        password = os.getenv("DB-password"),
        database = os.getenv("DB-database")
    )
    return connection