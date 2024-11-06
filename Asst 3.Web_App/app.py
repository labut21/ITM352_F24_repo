from flask import Flask, render_template, request, redirect, url_for, session
import json
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a secure key

# Paths for user data and quiz questions
USER_DATA_FILE = 'user_data.json'
QUIZ_FILE = 'quiz_questions.txt'

# Load data functions (same as your code)
def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file) if filename.endswith('.json') else file.read().split('---')

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def parse_question(block):
    lines = block.strip().split('\n')
    return {
        'question': lines[0],
        'options': lines[1:5],
        'answer': lines[5].strip(),
        'explanation': lines[6]
    }

# Load users and questions on app startup
users = load_data(USER_DATA_FILE)
questions = [parse_question(block) for block in load_data(QUIZ_FILE)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_quiz():
    session['score'] = 0
    session['current_question'] = 0
    session['fifty_fifty'] = True
    return redirect(url_for('quiz_question'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz_question():
    question_index = session.get('current_question', 0)
    
    # End the quiz if all questions are answered
    if question_index >= len(questions):
        return redirect(url_for('result'))
    
    question = questions[question_index]
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == question['answer'].lower():
            session['score'] += 1
        
        session['current_question'] += 1
        return redirect(url_for('quiz_question'))
    
    # Render question page
    return render_template('question.html', question=question, fifty_fifty=session['fifty_fifty'])

@app.route('/result')
def result():
    score = session.get('score', 0)
    # Update high score and find current champion
    # (similar to your `run_quiz` logic for high scores)
    # ...
    return render_template('result.html', score=score, champion='TBD')

if __name__ == "__main__":
    app.run(debug=True)