import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts")

postList = r.json()

print(len(postList))

print(postList[0]["title"])

for i in postList:
    print(i["title"])
# print(r.json(r))
