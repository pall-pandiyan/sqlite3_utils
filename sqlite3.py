import os
import sqlite3

from . import config


class SqLite3:
    """
    Contains functionalites for sqlite3.

    Developer: Pall Pandiyan.S
    """

    def __init__(self, db_name:str|None=None, connect:bool=True) -> None:
        """
        Initialize the db connection and cursor object using the given db_name.
        The database path is defined in the config module as DB_DIR.

        Developer: Pall Pandiyan.S
        """
        if db_name:
            self.db_name = db_name + ".db"
        else:
            self.db_name = "data.db"
        
        self.change_status(self.db_name + " - initiated")

        if connect:
            self.open_connection()
    

    def __str__(self) -> str:
        """
        Representation string containing the status of the connection.

        Developer: Pall Pandiyan.S
        """
        return self.status

    
    def change_status(self, status) -> None:
        """
        Change the status of the object.

        Developer: Pall Pandiyan.S
        """
        self.status = status
    

    def open_connection(self) -> None:
        """
        Connect to the current database and update the cursor.
        
        Developer: Pall Pandiyan.S
        """
        self.db_full_path = os.path.join(config.DB_DIR, self.db_name)
        self.conn = sqlite3.connect(self.db_full_path)
        self.cur = self.conn.cursor()
        self.change_status(self.db_name + " - ready")
    

    def close_conection(self) -> None:
        """
        Close the connection with the current database.
        
        Developer: Pall Pandiyan.S
        """
        self.conn.close()
        self.change_status(self.db_name + " - closed")
    

    def change_db(self, db_name:str) -> None:
        """
        Change the objects database name.

        Developer: Pall Pandiyan.S
        """
        self.close_conection()
        self.db_name = db_name
        self.open_connection()
    

    def execute_statement(self, query:str) -> None:
        """
        Execute the SQL statement provided as the argument.
        Since it is a statement nothing returned.

        Developer: Pall Pandiyan.S
        """
        self.cur.execute(query)
    

    def fetch_all(self, query:str) -> list:
        """
        Execute the SQL query provided as the argument.
        And return all the results.

        Developer: Pall Pandiyan.S
        """
        result = self.cur.execute(query)
        return result.fetchall()
    

    def fetch_one(self, query:str) -> list:
        """
        Execute the SQL query provided as the argument.
        And return the first result.

        Developer: Pall Pandiyan.S
        """
        result = self.cur.execute(query)
        return result.fetchone()
    

    def fetch_many(self, query:str) -> list:
        """
        Execute the SQL query provided as the argument.
        And return the results.

        Developer: Pall Pandiyan.S
        """
        result = self.cur.execute(query)
        return result.fetchmany()
    

    def delete_table(self, table_name) -> None:
        """
        Delete the given table.

        Developer: Pall Pandiyan.S
        """
        query = "DROP TABLE IF EXISTS " + table_name + ";"
        self.execute_statement(query=query)
    
    
    def select(self, table_name:str, cols:str|list|None=None) -> None:
        """
        Select query.

        Developer: Pall Pandiyan.S
        """
        if cols:
            cols = cols.join(',')
        else:
            cols = "*"
        query = "SELECT " + cols + " FROM " + table_name + ";"
        self.execute_statement(query=query)
