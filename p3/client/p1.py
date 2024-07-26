from requests import get
from time import sleep

while True:
    try:
        url = "http://127.0.0.1:8000/"
        res = get(url)
        data = res.json()
        m = data.get("m", "No message found")  
        print(m)
        print("*" * 50)
        sleep(5)
    except Exception as e:
        print("Issue:", e)


