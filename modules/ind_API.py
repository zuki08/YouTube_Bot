from modules.db_conn import create_conn
import modules.yt_API as yt
from dotenv import load_dotenv
import json

load_dotenv()

leConn = create_conn()
cur = leConn.cursor()
data = []
def search(query):
    query = query.replace(" ", "%")
    # print(query)
    q = f"SELECT DISTINCT * FROM info WHERE title like '%{query}%';"
    print(q)
    cur.execute(q)
    res = cur.fetchall()
    print(res)
    if(len(res) == 0):
        global data
        data = yt.main(query)
        # data = json.loads(data)
        print(data["items"][0])
        # data = data['items'][0]
        itemArr = []
        idx = 1;
        for item in data["items"]:
            itemArr.append(f"{idx}. {item["snippet"]["title"]}")
        return "\n".join(itemArr)
    else:
        return f"https://www.youtube.com/watch?v={res[0][2]}"
def choose(idx:int):
    idx = int(int(idx) - 1)
    print(data["items"][idx])
    ttl = data["items"][idx]['snippet']['title'].replace("&#39;", '\'')
    ttl = ttl.replace('&amp;', '&')
    ttl = ttl.replace('&quot;', '\"')
    q = f"INSERT INTO info VALUES(nextval('inc'), '{ttl}', '{data["items"][idx]['id']['videoId']}')"
    cur.execute(q)
    leConn.commit()
    return f"https://www.youtube.com/watch?v={data["items"][idx]['id']['videoId']}"
def select(idx:int):
    q = f"SELECT * FROM info WHERE id = {idx}";
    cur.execute(q)
    res = cur.fetchall()
    return f"https://www.youtube.com/watch?v={res[0][2]}"
def list():
     cur = leConn.cursor()
     q = "select * from info;"
     cur.execute(q)
     res = cur.fetchall()
     return res
def close_leConn():
    leConn.close()