import sqlite3

def delete_table(database_file, table_name):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        # Drop the table
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        print(f"Table '{table_name}' deleted successfully.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

# Replace 'your_database.db' with the actual name of your SQLite database file
database_file = './instance/app.sqlite'

# Replace 'your_table_name' with the name of the table you want to delete
table_name = 'users'

# Call the function to delete the table
delete_table(database_file, table_name)
