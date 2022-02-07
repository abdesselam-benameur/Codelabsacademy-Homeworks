import sqlite3
from sqlite3 import Error


def create_connection(db_filename):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        # add a connection for the database
        conn = sqlite3.connect(db_filename)
    except Error as e:
        print(e)

    #To-Do return the connection 
    return conn

def close_connection(conn):
    """ closes a connection to a database """
    conn.close()


def select_all(conn):
    """select all rows from our table using the conn we already created """
    cur = conn.cursor()
    # the query to retrive all data from the longley table 
    query = "SELECT * FROM longley"

    # execute the query 
    cur.execute(query)

    # fetch all rows using the cursor cur
    rows = cur.fetchall()

    return rows 


def print_rows(rows):
    """ Loop through the retrived rows of a table and print them"""
    # All of the function body is a todo task
    for row in rows:
        print(row)
