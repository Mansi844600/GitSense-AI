from flask import Blueprint, render_template, request, jsonify
from repo_analyzer import get_repo_data, extract_features
from scoring import calculate_score
from assistant import assistant_reply

dashboard = Blueprint("dashboard", __name__)

repo_cache = {}


@dashboard.route("/dashboard", methods=["GET", "POST"])
def show_dashboard():

    if request.method == "POST":
        username = request.form["username"]
        repo = request.form["repo"]

        data = get_repo_data(username, repo)

        if not data:
            return "Repository not found"

        features = extract_features(data)
        score = calculate_score(features)

        repo_cache["features"] = features
        repo_cache["score"] = score

        return render_template(
            "dashboard.html",
            features=features,
            score=score,
        )

    return render_template("index.html")


@dashboard.route("/assistant", methods=["POST"])
def assistant_chat():

    user_query = request.json["message"]

    features = repo_cache.get("features")
    score = repo_cache.get("score")

    reply = assistant_reply(user_query, features, score)

    return jsonify({"reply": reply})
