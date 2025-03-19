import psycopg2
import os

def create_conn():
    conn = psycopg2.connect(f"dbname={os.getenv('db_name')} user={os.getenv('db_user')}")
    # print(os.getenv('db_user'))
    print("Successful connection")
    return conn