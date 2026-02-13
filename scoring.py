def calculate_metrics(user, repos):

    repo_count = len(repos)
    stars = sum(r["stargazers_count"] for r in repos)
    forks = sum(r["forks_count"] for r in repos)

    readme_count = sum(1 for r in repos if r["description"])
    readme_ratio = readme_count / repo_count if repo_count else 0

    recent_activity = sum(1 for r in repos if r["pushed_at"])

    return {
        "repo_count": repo_count,
        "stars": stars,
        "forks": forks,
        "readme_ratio": readme_ratio,
        "recent_activity": recent_activity
    }


def generate_score(metrics):

    score = (
        min(metrics["repo_count"] * 2, 20) +
        min(metrics["stars"] * 1, 20) +
        min(metrics["readme_ratio"] * 20, 20) +
        min(metrics["recent_activity"] * 2, 20) +
        min(metrics["forks"] * 1, 20)
    )

    return round(score, 2)

