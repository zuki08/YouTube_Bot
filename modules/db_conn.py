import psycopg
import os

def create_conn():
    conn = psycopg.connect(f"dbname={os.getenv('db_name')} user={os.getenv('db_user')}")
    print("Successful connection")
    return conn