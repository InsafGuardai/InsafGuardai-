from flask import Flask, render_template, request
import os

app = Flask(__name__)

INDUSTRY_KEYWORDS = {
    "legal": ["contract", "law", "compliance", "regulation"],
    "finance": ["invoice", "payment", "tax", "balance sheet"],
    "hr": ["hiring", "termination", "salary", "employee"],
    "healthcare": ["patient", "medical", "treatment", "diagnosis"],
    "education": ["exam", "student", "curriculum", "learning"],
    "cybersecurity": ["encryption", "data breach", "malware", "firewall"],
    "it": ["server", "deployment", "API", "cloud"]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    result = {}
    text = ""
    if request.form.get("text"):
        text = request.form["text"]
    elif request.files.get("file"):
        file = request.files["file"]
        text = file.read().decode("utf-8")

    for industry, keywords in INDUSTRY_KEYWORDS.items():
        result[industry] = any(word.lower() in text.lower() for word in keywords)

    return render_template("result.html", result=result, text=text)

if __name__ == "__main__":
    app.run(debug=True)
