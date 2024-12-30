import pymysql
from dotenv import load_dotenv
from os import getenv

# load_dotenv()
DB_HOST = "localhost"#getenv('DB_HOST')
DB_USER = "root"#getenv('DB_USER')
DB_NAME = "flaskcrud"#getenv('DB_NAME')
DB_PASSWORD = "root"#getenv('DB_PASSWORD') 

def get_db_con():
    con =pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )

    query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"

    cursor = con.cursor()
    cursor.execute(query=query)
    cursor.execute(f"USE {DB_NAME}")
    con.commit()
    return con


if __name__ == "__main__":
    get_db_con()
