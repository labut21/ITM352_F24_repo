from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def quiz():
    # Load questions from the JSON file
    with open('questions.json') as f:
        questions = json.load(f)

    # No need to randomize options or calculate correct answers; JSON already specifies `correct`
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)