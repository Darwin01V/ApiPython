import pyodbc
from src.config import Config

def get_connection():
    conn_str = (
        f"DRIVER={{Progress OpenEdge 11.7 Driver}};"
        f"HOST={Config.PROGRESS_DB_HOST};"
        f"PORT={Config.PROGRESS_DB_PORT};"
        f"DB={Config.PROGRESS_DB_NAME};"
        f"UID={Config.PROGRESS_DB_USER};"
        f"PWD={Config.PROGRESS_DB_PASSWORD};"
    )
    conn = pyodbc.connect(conn_str)
    return conn


# import mysql.connector
# from src.config import Config

# def get_connection():
#     conn = mysql.connector.connect(
#         host=Config.MYSQL_DB_HOST,
#         port=int(Config.MYSQL_DB_PORT),
#         database=Config.MYSQL_DB_NAME,
#         user=Config.MYSQL_DB_USER,
#         password=Config.MYSQL_DB_PASSWORD
#     )
#     return conn
