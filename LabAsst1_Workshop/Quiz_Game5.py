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

question_num = 1
for question, details in QUESTIONS.items():
    print(f"\n{question_num}. {question}")
    
    for option in details["options"]:
        print(f"  - {option}")
    
    # Loop until the correct answer
    while True:
        answer = input("Your answer: ").strip()
        
        if answer == details["correct"]:
            print("Correct!")
            score += 1
            correct_answers.append(question)  # Track correct answers
            break  # Leave loop after the correct answer
        else:
            print("Incorrect, please try again.")
    
    question_num += 1

print(f"\nYour final score is {score}/{len(QUESTIONS)}")

print("\nYou answered these questions correctly:")
for correct_question in correct_answers:
    print(f" - {correct_question}")