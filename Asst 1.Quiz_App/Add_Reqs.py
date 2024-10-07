def load_quiz(filename):
    """
    Loads the quiz questions from a file.
    
    :param filename: Name of the file containing quiz questions
    :return: List of quiz questions, each represented as a dictionary
    """
    quiz = []
    with open(filename, 'r') as file:
        blocks = file.read().split('---')
        for block in blocks:
            lines = block.strip().split('\n')
            if len(lines) >= 7:
                question = lines[0]
                options = lines[1:5]
                answer = lines[5].strip()
                explanation = lines[6]
                quiz.append({
                    'question': question,
                    'options': options,
                    'answer': answer,
                    'explanation': explanation
                })
    return quiz

def ask_question(question_data):
    """
    Asks a single quiz question and checks the user's response.
    
    :param question_data: Dictionary containing question, options, answer, and explanation
    :return: True if the user answered correctly, otherwise False
    """
    print(question_data['question'])
    for option in question_data['options']:
        print(option)
    
    while True:
        user_answer = input("Your answer (a/b/c/d): ").strip().lower()
        if user_answer in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Invalid input. Please enter 'a', 'b', 'c', or 'd'.")
    
    correct_option = question_data['answer'].lower()
    if user_answer == correct_option:
        print("Correct!\n")
        print(f"Explanation: {question_data['explanation']}\n")
        return True
    else:
        print(f"Incorrect! The correct answer was '{correct_option.upper()}'.\n")
        print(f"Explanation: {question_data['explanation']}\n")
        return False

def run_quiz(quiz):
    """
    Runs the entire quiz, asking each question in sequence and calculating the final score.
    
    :param quiz: List of quiz questions
    """
    score = 0
    for question in quiz:
        if ask_question(question):
            score += 1
    
    print(f"You've completed the quiz! Your final score is {score}/{len(quiz)}.")

if __name__ == "__main__":
    filename = 'quiz_questions.txt'  # Replace with correct path if needed
    quiz_data = load_quiz(filename)
    run_quiz(quiz_data)