score = 0
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
    print(f"{question_num}. {question}")
    
    for option in details["options"]:
        print(f" - {option}")
    
    answer = input("Your answer: ")
    if answer == details["correct"]:
        score += 1
    
    question_num += 1

print(f"Your score is {score}")