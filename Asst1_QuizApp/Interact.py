import json
import random

# Paths for user data and quiz questions
USER_DATA_FILE = 'user_data.json'
QUIZ_FILE = 'quiz_questions.txt'

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file) if filename.endswith('.json') else file.read().split('---')

def save_data(data, filename):
    # Stores user information
    with open(filename, 'w') as file:
        json.dump(data, file)

def parse_question(block):
    # Analyze a question from the text file
    lines = block.strip().split('\n')
    return {
        'question': lines[0],
        'options': lines[1:5],
        'answer': lines[5].strip(),
        'explanation': lines[6] # Added explanation for why the answer is correct
    }

def get_username(users):
    # Get or register a username
    while True:
        username = input("Enter your username: ").strip()
        if username:
            if username not in users:
                users[username] = {'high_score': 0}
                save_data(users, USER_DATA_FILE)
                print(f"Welcome, {username}! You've been registered.")
            else:
                print(f"Welcome back, {username}!")
            return username

def use_fifty_fifty(question):
    # Add a 50/50 feature
    # Remove two incorrect answers
    correct_answer = question['answer'].lower()
    incorrect_options = [opt for opt in question['options'] if opt[0].lower() != correct_answer]
    removed_options = random.sample(incorrect_options, 2)
    return [opt for opt in question['options'] if opt not in removed_options]

def ask_question(question, fifty_fifty_available):
    # Show a question to the user, keep track of their answer, and manage the 50/50 feature
    # Return if the answer was correct and if the 50/50 was used
    print(question['question'])
    options = question['options']
    
    if fifty_fifty_available:
        use_5050 = input("Can only be used once: Would you like to eliminate 2 of the 4 wrong answers? (y/n): ").strip().lower() == 'y'
        if use_5050:
            options = use_fifty_fifty(question)
            fifty_fifty_available = False
    
    for option in options:
        print(option)
    
    while True:
        answer = input("Your answer (a/b/c/d): ").strip().lower()
        if answer in 'abcd':
            return answer == question['answer'].lower(), fifty_fifty_available
        print("Invalid input. Please enter 'a', 'b', 'c', or 'd'.")

def run_quiz(questions, username, users):
    # Main quiz loop that shows questions, tracks scores, updates high scores, and shows explanations
    # Shares the user's score, updates their high score if needed, and displays the overall champion
    score = 0
    fifty_fifty_available = True
    
    for question in questions:
        correct, fifty_fifty_available = ask_question(question, fifty_fifty_available)
        if correct:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer was '{question['answer'].upper()}'.")
        print(f"Explanation: {question['explanation']}\n") # Show explanation after each question
    
    print(f"Quiz complete! Your score: {score}/{len(questions)}")
    
    # Update user's high score if they have beaten their prior best
    if score > users[username]['high_score']:
        users[username]['high_score'] = score
        print(f"New personal high score: {score}")
    
    # Find and display the overall champion
    champion = max(users, key=lambda u: users[u]['high_score'])
    print(f"Current champion: {champion} with a score of {users[champion]['high_score']}")
    
    # Save updated user data
    save_data(users, USER_DATA_FILE)

if __name__ == "__main__":
    users = load_data(USER_DATA_FILE)
    questions = [parse_question(block) for block in load_data(QUIZ_FILE)]
    username = get_username(users)
    run_quiz(questions, username, users)