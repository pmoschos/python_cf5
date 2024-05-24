# MySQL Database Connection and Update in Python

This script demonstrates how to connect to a MySQL database server and update a record in an existing table using Python. It includes error handling for common issues such as authentication failures and SQL execution errors.

## Script Overview 📘

The script defines functions to create a connection to a MySQL server and to update a teacher's information in the `teachers` table using the established connection. The `main()` function demonstrates these operations with specified connection parameters.

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

def update_teacher(connection, teacher):
    """
    Update a teacher's information in the teachers table.

    Parameters:
    connection: A MySQLConnection object.
    teacher (tuple): A tuple containing the teacher's firstname, lastname, age, and id.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(
            "UPDATE teachers SET firstname = %s, lastname = %s, age = %s WHERE id = %s",
            teacher
        )
        connection.commit()
        print("Teacher updated successfully")
    except Error as e:
        print(f"Error: '{e}' occurred")
        connection.rollback()
    finally:
        cursor.close()

def main():
    """
    Main function to connect to the database and update a teacher.
    """
    conn = create_connection('localhost', 'root', 'root', 'coding2024', '3306')
    if conn:
        teacher = ("Alice", "Smith", 45, 2)  # New values for firstname, lastname, and age, with id to identify the teacher
        update_teacher(conn, teacher)
        conn.close()
        print("MySQL connection is closed")

if __name__ == "__main__":
    main()
```

# MySQL Database Connection and Update in Python

This script demonstrates how to connect to a MySQL database server and update a record in an existing table using Python. It includes error handling for common issues such as authentication failures and SQL execution errors.

## Key Features 🌟
- **MySQL Connection**: Learn how to establish a connection to a MySQL server using Python.
- **Update Records**: Understand how to update existing records in a database using SQL queries.
- **Error Handling**: See how to handle errors gracefully when connecting to the database and executing SQL queries.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **MySQL Server**: Ensure MySQL server is installed and running
- **External Libraries**: `mysql-connector-python`

## Installation and Setup 🚀
1. Ensure Python 3.x is installed on your machine.
2. Ensure MySQL server is installed and running.
3. Install the required library with: `pip install mysql-connector-python`
4. Save the script as `update_data.py`.
5. Open a terminal or command prompt.
6. Navigate to the directory containing `update_data.py`.
7. Run the script with: `python update_data.py`.

## Usage Example 📋
Execute the script to see how to connect to a MySQL server and update a teacher's information in the `teachers` table. The script will demonstrate establishing a connection and executing a SQL query to update the record.

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Your Name - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Your Name (https://github.com/pmoschos)
</p>
