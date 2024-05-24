# MySQL Database Connection and Data Fetching in Python

This script demonstrates how to connect to a MySQL database server, create a database, create tables, insert data, and fetch data using Python. It includes error handling for common issues such as authentication failures and SQL execution errors.

## Script Overview 📘

The script defines functions to create a connection to a MySQL server, fetch data from a table within that database, and handle errors gracefully. The `main()` function demonstrates these operations with specified connection parameters.

### :computer: Script Code

```python
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name, port):
    """
    Create a database connection to a MySQL server.
    
    Parameters:
    host_name (str): The name of the host.
    user_name (str): The user name used to authenticate.
    user_password (str): The password used to authenticate.
    db_name (str): The name of the database.
    port (str): The port number to connect to.

    Returns:
    conn: A MySQLConnection object or None if the connection failed.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name,
            port=port
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"Error: '{e}' occurred")
    return connection

def fetch_teachers(connection):
    """
    Fetch teachers from the teachers table.

    Parameters:
    connection: A MySQLConnection object.

    Returns:
    list: A list of tuples containing the fetched records.
    """
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, firstname, lastname FROM teachers")
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error: '{e}' occurred")
        return []
    finally:
        cursor.close()

def main():
    """
    Main function to connect to the database and fetch teachers.
    """
    conn = create_connection('localhost', 'root', 'root', 'coding2024', '3306')
    if conn:
        results = fetch_teachers(conn)
        print(results)
        print(type(results))
        print()

        for result in results:
            print(f"ID: {result[0]}, Firstname: {result[1]}, Lastname: {result[2]}")
        
        conn.close()
        print("MySQL connection is closed")

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **MySQL Connection**: Learn how to establish a connection to a MySQL server using Python.
- **Database Creation**: Understand how to create a new database using SQL queries.
- **Table Creation**: Learn how to create tables within a MySQL database.
- **Data Insertion**: See how to insert data into a MySQL database table.
- **Data Fetching**: Learn how to fetch data from a MySQL database table.
- **Error Handling**: See how to handle errors gracefully when connecting to the database and executing SQL queries.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **MySQL Server**: Ensure MySQL server is installed and running
- **External Libraries**: `mysql-connector-python`

## Installation and Setup 🚀
1. Ensure Python 3.x is installed on your machine.
2. Ensure MySQL server is installed and running.
3. Install the required library with: `pip install mysql-connector-python`
4. Save the script as `retrieve_data.py`.
5. Open a terminal or command prompt.
6. Navigate to the directory containing `retrieve_data.py`.
7. Run the script with: `python retrieve_data.py`.

## Usage Example 📋
Execute the script to see how to connect to a MySQL server, create a new database, create tables, insert data, and fetch data. The script will demonstrate establishing a connection, executing SQL queries to create a database and tables, inserting data into the tables, and fetching data from the tables.

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
