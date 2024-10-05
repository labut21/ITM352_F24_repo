import random

def get_questions():
    """Return the list of questions with options and correct answers."""
    return {
        "What is the airspeed of an unladen swallow in miles/hr?": {
            "options": ["10", "12", "14", "16"],
            "correct": "12"
        },
        "What is the capital of Texas?": {
            "options": ["Houston", "Austin", "Dallas", "San Antonio"],
            "correct": "Austin"
        }
    }

def shuffle_questions(questions):
    """Return a shuffled list of question items."""
    question_list = list(questions.items())
    random.shuffle(question_list)
    return question_list

def display_question(question_num, question, options):
    """Display the question and its options."""
    print(f"\n{question_num}. {question}")
    for option in options:
        print(f"  - {option}")

def get_user_answer():
    """Prompt the user for an answer."""
    return input("Your answer: ")

def check_answer(user_answer, correct_answer):
    """Check if the user's answer is correct."""
    return user_answer == correct_answer

def quiz():
    """Main function to run the quiz."""
    score = 0
    correct_answers = []
    questions = get_questions()
    
    # Shuffle the questions
    question_list = shuffle_questions(questions)
    
    # Manual tracking of question number
    question_num = 1
    
    # Loop through each question
    for question, details in question_list:
        # Shuffle the options for each question
        options = details["options"][:]
        random.shuffle(options)
        
        # Display the question and options
        display_question(question_num, question, options)
        
        # Loop until the correct answer is provided
        while True:
            answer = get_user_answer()
            if check_answer(answer, details["correct"]):
                print("Correct!")
                score += 1
                correct_answers.append(question)
                break
            else:
                print("Incorrect, please try again.")
        
        question_num += 1  # Increment the question number manually
    
    # Display the final score and correct answers
    print(f"\nYour final score is {score}/{len(questions)}")
    print("\nYou answered these questions correctly:")
    for correct_question in correct_answers:
        print(f" - {correct_question}")

# Run the quiz
quiz()