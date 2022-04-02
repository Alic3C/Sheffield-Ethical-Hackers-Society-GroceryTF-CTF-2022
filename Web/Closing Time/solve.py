import requests
import re

url = "http://18.170.40.69:3000/"

sess = requests.session()

sess.get(url)

resp = sess.post(url, data={"Wine":"on", "Cheese":"on"})

print(*re.findall(r"(SESH\{.*?\})", resp.text))
