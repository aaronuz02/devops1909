import requests

with open("names.txt", "r") as my_file:
    names = my_file.read().splitlines()
    for name in names:
        print(name)

with requests.get("https://www.ynet.co.il/")   as response:
    response.raise_for_status()
