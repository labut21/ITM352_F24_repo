score = 0
QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": {
        "options": ["12", "8", "11", "15"],
        "correct": 2
    },
    "What is the capital of Texas?": {
        "options": ["Houston", "Austin", "Dallas", "San Antonio"],
        "correct": 2
    }
}

question_num = 1
for question, details in QUESTIONS.items():
    print(f"{question_num}. {question}")
    
    for idx in range(len(details["options"])):
        print(f"  {idx + 1}. {details['options'][idx]}")
    
    answer_idx = int(input("Your answer (choose the number): "))
    if answer_idx == details["correct"]:
        score += 1
    
    question_num += 1

print(f"Your score is {score}")