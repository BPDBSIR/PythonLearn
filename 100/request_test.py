from requests import get

response = get("https://xiaoyes.cn")
print(response.content)

