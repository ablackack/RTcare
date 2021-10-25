import sqlite3

connection = sqlite3.connect('digital.db')

with open('schema_digital.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
