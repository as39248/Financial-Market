import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv() 

def connect_db():

    userdb = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return userdb