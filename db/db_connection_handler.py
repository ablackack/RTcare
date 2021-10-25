import sqlite3


class DbConnectionHandler:
    @staticmethod
    def get_connection_for_digital():
        conn = sqlite3.connect('db/digital.db')
        conn.row_factory = sqlite3.Row
        return conn
