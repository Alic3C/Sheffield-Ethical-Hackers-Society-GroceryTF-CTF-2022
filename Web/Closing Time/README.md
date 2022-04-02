# Closing Time
> 110pts

## Breifing
Oh no, the store is closing and you need to buy some supplies for your party. There are only two items left on your shopping list, and the local store Borrisons is about to close.

http://18.170.40.69:3000/

## Hint
A cheese and wine party, sounds fun....

## Solution
If only humans were robotic fast:

```python
import requests
import re

url = "http://18.170.40.69:3000/"

sess = requests.session()

sess.get(url)

resp = sess.post(url, data={"Wine":"on", "Cheese":"on"})

print(*re.findall(r"(SESH\{.*?\})", resp.text))
```

## Flag
Flag: `SESH{Ch3ESe&ndW1neP4rty_It_1s}`