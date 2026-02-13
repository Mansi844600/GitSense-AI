import requests

HEADERS = {
    "Accept": "application/vnd.github+json"
}

def get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    res = requests.get(url, headers=HEADERS)

    if res.status_code == 200:
        return res.json()

    return None


def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    res = requests.get(url, headers=HEADERS)

    if res.status_code == 200:
        return res.json()

    return []
