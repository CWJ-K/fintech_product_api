import os

MYSQL_DATA_HOST = os.environ.get("MYSQL_DATA_HOST", "127.0.0.1")
MYSQL_DATA_USER = os.environ.get("MYSQL_DATA_USER", "user")
MYSQL_DATA_PASSWORD = os.environ.get("MYSQL_DATA_PASSWORD", "user")
MYSQL_DATA_PORT = int(os.environ.get("MYSQL_DATA_PORT", "3306"))
MYSQL_DATA_DATABASE = os.environ.get("MYSQL_DATA_DATABASE", "invest")

API_HOST = os.environ.get("API_HOST", "127.0.0.1")
API_PORT = int(os.environ.get("API_PORT", "8888"))

