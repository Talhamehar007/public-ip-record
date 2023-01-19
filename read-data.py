import sqlite3
import pandas as pd

def read_data(database_file):
    try:
        # Connect to the database
        conn = sqlite3.connect(database_file, check_same_thread=False)

        # Read data from the ip_logs table
        df = pd.read_sql_query("SELECT * FROM ip_logs", conn)

        # Close the connection
        conn.close()

        # Return the DataFrame
        return df
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    data = read_data("ip_logs.db")
    print(data)

