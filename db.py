import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kashyap2207*",
        database="tournament_db"
    )
    return conn