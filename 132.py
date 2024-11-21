import requests

username = ["avielb", "dviramoyal"]
for user in username:
    url = f"https://api.github.com/users/{user}/repos"

    response = requests.get(url)
    if response.status_code == 200:
       repos = response.json()
        for repo in repos:
            if "devops" in str(repo["full_name"]).lower()
          print(f"{user} - {repo['full_name']}"