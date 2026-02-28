from flask import Flask, render_template, request
import json

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

    # Load previous data
    with open("data.json", "r") as file:
        data = json.load(file)

    data.append(percentage)

    # Save updated data
    with open("data.json", "w") as file:
        json.dump(data, file)

    # Suggestion
    if percentage < 40:
        message = "You're doing well. Keep maintaining healthy habits 👍"
    elif percentage < 70:
        message = "You're experiencing moderate stress. Try relaxation or take short breaks."
    else:
        message = "Your stress level is high. Consider talking to a trusted person or professional."

    # Trend detection
    trend_warning = ""
    if len(data) >= 3 and data[-3] < data[-2] < data[-1]:
        trend_warning = "⚠️ Your stress is increasing consistently."

    return f"""
    <html>
    <head>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="card">
            <h2>Your Stress Score: {percentage}%</h2>
            <p>{message}</p>
            <p class="warning">{trend_warning}</p>

            <br>
            <a href='/dashboard'>View Dashboard</a><br><br>
            <a href='/'>Go Back Home</a>
        </div>
    </body>
    </html>
    """

@app.route("/dashboard")
def dashboard():
    with open("data.json", "r") as file:
        data = json.load(file)

    return render_template("dashboard.html", scores=data)

if __name__ == "__main__":
    app.run(debug=True)