import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
text = response.text

print(text.count('a'))
cnt = 0
for e in text:
    if e == 'a':
        cnt += 1
    else:
        pass
print(cnt)
