def generate_recommendations(metrics):

    recs = []

    if metrics["readme_ratio"] < 0.5:
        recs.append("Add detailed README explaining project usage")

    if metrics["repo_count"] < 5:
        recs.append("Build more diverse projects")

    if metrics["recent_activity"] < 3:
        recs.append("Stay consistent with commits")

    if metrics["stars"] == 0:
        recs.append("Promote projects on LinkedIn / GitHub community")

    return recs
