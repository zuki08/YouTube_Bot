from modules.db_conn import create_conn
import modules.yt_API as yt
from dotenv import load_dotenv
import json

load_dotenv()

leConn = create_conn()

def search(query):
    cur = leConn.cursor()
    q = f"SELECT title FROM info WHERE title like '%{query}%';"
    cur.execute(q)
    res = cur.fetchall()
    if(len(res) == 0):
        data = yt.main(query)
        # data = json.loads(data)
        print(data["items"][0])
        q = f"INSERT INTO info VALUES(id, '{data['title']}', '{data['id']['videoId']}')"

def close_leConn():
    leConn.close()