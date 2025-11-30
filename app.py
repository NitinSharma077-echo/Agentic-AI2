from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request
import sys
import os

# Allow importing main.py from this folder
sys.path.append(os.path.abspath("."))

from main import run_pipeline

# Make Flask load HTML from webapp/templates
app = Flask(__name__, template_folder="webapp/templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    topic = request.form.get("topic")
    hours = request.form.get("hours")

    if not topic or not hours:
        return render_template("index.html", error="Please fill all fields.")

    result = run_pipeline(topic, hours)

    return render_template("result.html", topic=topic, hours=hours, result=result)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

