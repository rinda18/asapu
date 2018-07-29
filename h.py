import requests
r = requests.get("http://beeg.com").text
print(r[:3000])
