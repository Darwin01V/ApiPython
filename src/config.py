import os
from dotenv import load_dotenv
class Config:
    # Configuración para la base de datos Progress OpenEdge
    PROGRESS_DB_HOST = os.getenv('PROGRESS_DB_HOST', 'localhost')
    PROGRESS_DB_PORT = os.getenv('PROGRESS_DB_PORT', '1234')
    PROGRESS_DB_NAME = os.getenv('PROGRESS_DB_NAME', 'mydb')
    PROGRESS_DB_USER = os.getenv('PROGRESS_DB_USER', 'user')
    PROGRESS_DB_PASSWORD = os.getenv('PROGRESS_DB_PASSWORD', 'password')

    # Configuración para la base de datos MySQL
    MYSQL_DB_HOST = os.getenv('MYSQL_DB_HOST', 'localhost')
    MYSQL_DB_PORT = os.getenv('MYSQL_DB_PORT', '3306')
    MYSQL_DB_NAME = os.getenv('MYSQL_DB_NAME', 'farmacia')
    MYSQL_DB_USER = os.getenv('MYSQL_DB_USER', 'root')
    MYSQL_DB_PASSWORD = os.getenv('MYSQL_DB_PASSWORD', '') 
