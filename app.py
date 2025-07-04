from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['user_input']
    response = f"This input is detected as safe and useful for corporate use."
    industry = random.choice(["Legal", "Healthcare", "Finance", "IT", "Education", "HR", "Marketing"])
    return render_template('result.html', input=user_input, result=response, industry=industry)

if __name__ == '__main__':
    app.run(debug=True)
