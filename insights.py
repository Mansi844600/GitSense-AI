def generate_insights(metrics):

    strengths = []
    red_flags = []

    if metrics["repo_count"] > 8:
        strengths.append("Strong project portfolio")

    if metrics["readme_ratio"] > 0.6:
        strengths.append("Good documentation practices")

    if metrics["stars"] > 20:
        strengths.append("Community engagement visible")

    if metrics["recent_activity"] < 3:
        red_flags.append("Low recent activity")

    if metrics["readme_ratio"] < 0.3:
        red_flags.append("Poor documentation")

    if metrics["repo_count"] < 3:
        red_flags.append("Very few projects")

    return strengths, red_flags
