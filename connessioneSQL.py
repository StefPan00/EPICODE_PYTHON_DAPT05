import pymysql
import os
import dotenv
import sqlalchemy
import pandas as pd

dotenv.load_dotenv(override=True, dotenv_path="C:/Users/PANTANO/Desktop/Data Analyst/.env")
username = os.getenv("username")
password = os.getenv("password")
host = os.getenv("host")
dbname = os.getenv("dbname")

conn_string = "mysql+pymysql://" + username + ":" + password + "@" + host + "/" + dbname

db_engine = sqlalchemy.create_engine(conn_string)