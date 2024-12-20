import random

score = 0
correct_answers = []

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": {
        "options": ["12", "8", "11", "15"],
        "correct": "12"
    },
    "What is the capital of Texas?": {
        "options": ["Houston", "Austin", "Dallas", "San Antonio"],
        "correct": "Austin"
    }
}

# Randomize the order of the questions
question_list = list(QUESTIONS.items())
random.shuffle(question_list)

# Loop through each randomized question
question_num = 1
for question, details in question_list:
    print(f"\n{question_num}. {question}")
    
    # Randomize the answer options for the current question
    options = details["options"][:]
    random.shuffle(options)
    
    # Show the shuffled answer options
    for option in options:
        print(f"  - {option}")
    
    # Loop until the correct answer
    while True:
        answer = input("Your answer: ")
        
        if answer == details["correct"]:
            print("Correct!")
            score += 1
            correct_answers.append(question)
            break
        else:
            print("Incorrect, please try again.")
    
    question_num += 1

# Final score and correct answers show
print(f"\nYour final score is {score}/{len(QUESTIONS)}")

print("\nYou answered these questions correctly:")
for correct_question in correct_answers:
    print(f" - {correct_question}")