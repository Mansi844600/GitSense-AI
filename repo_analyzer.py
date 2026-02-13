import requests
from config import GITHUB_API


def get_repo_data(username, repo):
    url = f"{GITHUB_API}/repos/{username}/{repo}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def extract_features(repo_data):
    features = {
        "stars": repo_data.get("stargazers_count", 0),
        "forks": repo_data.get("forks_count", 0),
        "issues": repo_data.get("open_issues_count", 0),
        "language": repo_data.get("language", "Unknown"),
        "watchers": repo_data.get("watchers_count", 0),
    }

    return features
