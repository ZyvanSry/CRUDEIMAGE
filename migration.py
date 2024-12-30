from repository import get_db_con
from pymysql import MySQLError


def product():
    con = get_db_con() 
    cursor = con.cursor() 
    query = """
            CREATE TABLE products(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name varchar(100) NOT NULL,
                    description TEXT,
                    thumbnail varchar(255),
                    create_at datetime default current_timestamp
            );
        """
    try : 
        cursor.execute(query=query)
        print("tabele create successs")
    except MySQLError as error:
        print(f"the table to create is {error}")

    return con

if __name__ == "__main__":
    product()