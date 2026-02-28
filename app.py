from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/survey")
def survey():
    return render_template("survey.html")

@app.route("/submit", methods=["POST"])
def submit():

    stress = int(request.form["stress"])
    sleep = int(request.form["sleep"])
    mood = int(request.form["mood"])
    motivation = int(request.form["motivation"])
    anxiety = int(request.form["anxiety"])

    total_score = stress + sleep + mood + motivation + anxiety
    percentage = round((total_score / 25) * 100)

    # Load previous data safely
    if not os.path.exists("data.json"):
        data = []
    else:
        with open("data.json", "r") as file:
            data = json.load(file)

    data.append(percentage)

    with open("data.json", "w") as file:
        json.dump(data, file)

    if percentage < 40:
        message = "You're doing well. Keep maintaining healthy habits 👍"
    elif percentage < 70:
        message = "You're experiencing moderate stress. Try relaxation."
    else:
        message = "High stress detected. Consider speaking to someone."

    return f"""
    <html>
    <head>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="card">
            <h2>Your Stress Score: {percentage}%</h2>
            <p>{message}</p>
            <br>
            <a href='/'>Go Back Home</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)