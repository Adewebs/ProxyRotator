import threading
import queue
import requests

q = queue.Queue()
valid_proxy = []
with open("proxy_list.txt", "r") as f:
    check_proxiy = f.read().split("\n")
    for p in check_proxiy:
        q.put(p)


def check_proxy():
     global q
     while not q.empty():
         proxy = q.get()
         try:
             res = requests.get("http://ipinfo.io/json",
                                proxies={"http":proxy, "https":proxy})
         except:
             continue
         if res.status_code ==200:
             print(proxy)


for t in range(10):
    threading.Thread(target=check_proxy).start()