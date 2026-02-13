from flask import Flask, render_template, request, jsonify
from github_api import get_user_data, get_repos
from scoring import calculate_metrics, generate_score
from insights import generate_insights
from recommendations import generate_recommendations
from assistant import assistant_reply
import webbrowser
from threading import Timer

app = Flask(__name__)

stored_metrics = {}


# -------------------------------
# Auto open browser
# -------------------------------
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


# -------------------------------
# Main Route
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        username = request.form["username"].strip()

        # Validate empty input
        if not username:
            return render_template("index.html", error="Please enter a username")

        user = get_user_data(username)

        # Validate profile exists
        if not user:
            return render_template("index.html", error="GitHub user not found")

        repos = get_repos(username)

        metrics = calculate_metrics(user, repos)
        score = generate_score(metrics)

        strengths, flags = generate_insights(metrics)
        recs = generate_recommendations(metrics)

        global stored_metrics
        stored_metrics = metrics

        return render_template(
            "dashboard.html",
            user=user,
            score=score,
            metrics=metrics,
            strengths=strengths,
            flags=flags,
            recs=recs
        )

    return render_template("index.html")


# -------------------------------
# AI Assistant Route
# -------------------------------
@app.route("/assistant", methods=["POST"])
def assistant():

    question = request.json.get("question")

    if not stored_metrics:
        return jsonify({"reply": "Please analyze a profile first."})

    answer = assistant_reply(question, stored_metrics)

    return jsonify({"reply": answer})


# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)
