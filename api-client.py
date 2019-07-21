import requests

res = requests.post('http://localhost:5000/api/v1/words',json= {"letters": "red"})

if res.ok:
    print (res.json())