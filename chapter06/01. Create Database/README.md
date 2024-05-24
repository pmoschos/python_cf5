# MySQL Database Connection and Creation in Python

This script demonstrates how to connect to a MySQL database server and create a new database using Python. It includes error handling for common issues such as authentication failures and SQL execution errors.

## Script Overview 📘

The script defines functions to create a connection to a MySQL server and to create a new database using the established connection. The `main()` function demonstrates these operations with specified connection parameters.

### :computer: Script Code

```python
import mysql.connector
from mysql.connector import Error

# pip install mysql-connector-python

def create_connection(host_name, user_name, user_password):
    """
    Create a database connection to a MySQL server.
    
    Parameters:
    host_name (str): The name of the host.
    user_name (str): The user name used to authenticate.
    user_password (str): The password used to authenticate.

    Returns:
    conn: A MySQLConnection object or None if the connection failed.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"Error: '{e}' occurred")
    return connection

def create_database(connection, query):
    """
    Create a database using the provided connection and query.

    Parameters:
    connection: A MySQLConnection object.
    query (str): The SQL query to create a database.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"Error: '{e}' occurred")
    finally:
        cursor.close()

def main():
    """
    Main function to create a database.
    """
    conn = create_connection('localhost', 'root', 'root')
    if conn:
        create_database_query = "CREATE DATABASE coding2024"
        create_database(conn, create_database_query)
        conn.close()
        print("MySQL connection is closed")

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **MySQL Connection**: Learn how to establish a connection to a MySQL server using Python.
- **Database Creation**: Understand how to create a new database using SQL queries.
- **Error Handling**: See how to handle errors gracefully when connecting to the database and executing SQL queries.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **MySQL Server**: Ensure MySQL server is installed and running
- **External Libraries**: `mysql-connector-python`

## Installation and Setup 🚀
1. Ensure Python 3.x is installed on your machine.
2. Ensure MySQL server is installed and running.
3. Install the required library with: `pip install mysql-connector-python`
4. Save the script as `create_db.py`.
5. Open a terminal or command prompt.
6. Navigate to the directory containing `create_db.py`.
7. Run the script with: `python create_db.py`.

## Usage Example 📋
Execute the script to see how to connect to a MySQL server and create a new database. The script will demonstrate establishing a connection and executing a SQL query to create a database.

📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
