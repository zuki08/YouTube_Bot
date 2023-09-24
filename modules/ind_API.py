from modules.db_conn import create_conn
import modules.yt_API as yt
from dotenv import load_dotenv
import json

load_dotenv()

leConn = create_conn()

def search(query):
    cur = leConn.cursor()
    query = query.replace(" ", "%")
    # print(query)
    q = f"SELECT DISTINCT * FROM info WHERE Lower(title) like '%{query}%';"
    # print(q)
    cur.execute(q)
    res = cur.fetchall()
    if(len(res) == 0):
        data = yt.main(query)
        # data = json.loads(data)
        # print(data["items"][0])
        data = data['items'][0]
        # q = f"INSERT INTO info VALUES(nextval('inc'), '{data['snippet']['title']}', '{data['id']['videoId']}')"
        # cur.execute(q)
        # leConn.commit()
        return f"https://www.youtube.com/watch?v={data['id']['videoId']}"
    else:
        return f"https://www.youtube.com/watch?v={res[0][2]}"
def list():
     cur = leConn.cursor()
     q = "select * from info;"
     cur.execute(q)
     res = cur.fetchall()
     return res
def close_leConn():
    leConn.close()