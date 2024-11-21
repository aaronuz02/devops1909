import requests

response = requests.get("https://www.ynet.co.il/")
if response.status_code == 200:
    print("ynet page found")
    