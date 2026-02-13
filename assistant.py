def assistant_reply(user_query, repo_features, repo_score):
    query = user_query.lower()

    if "improve" in query:
        return suggest_improvements(repo_features)

    if "score" in query:
        return f"Your repository score is {repo_score}."

    if "issues" in query:
        return f"You currently have {repo_features['issues']} open issues."

    return "I can help you analyze repo score, issues, improvements, or popularity."


def suggest_improvements(features):
    suggestions = []

    if features["issues"] > 10:
        suggestions.append("Try resolving open issues.")

    if features["stars"] < 5:
        suggestions.append("Promote your repo to gain visibility.")

    if features["forks"] < 3:
        suggestions.append("Encourage collaboration.")

    if not suggestions:
        return "Your repo looks strong. Keep maintaining consistency."

    return "Suggestions:\n" + "\n".join(suggestions)
