from utils.http import Http

base_url = "https://anda-api.williamginger.top/api/v1/"
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhbmRhIiwic3ViIjoiOTkzNTgzMmJhZGYzMTFlZTgwMTYwNDdjMTZkNGEzYjQiLCJ1c2VybmFtZSI6ImhhbyIsIm5pY2tuYW1lIjoiXHU2ZDY5Iiwicm9sZSI6InN1cGVyIiwiZXhwIjoxNzEzODQ3NTUyfQ.J1hTUHHq1akAy9TmNHZ1yDNRvBZMVrVCQ1WYLDDraLY"
}

session = Http(
    base_url=base_url,
    default_headers=headers,
).create()

res = session.get("https://www.cnblogs.com/chiyun/p/17653549.html", json={
    "page": 1,
    "size": 2
})

print(res.text)

session.close()