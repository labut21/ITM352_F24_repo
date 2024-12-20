score = 0
qas = [
        ("What is the airspeed of an unladen swallow in miles/hr", "12"), 
        ("What is the capital of Texas", "Austin")
]

for question_num in range(len(qas)):
    answer = input(f"{question_num}. {qas[question_num][0]}? ")
    if answer == qas[question_num][1]:
        score = score + 1

print(f"Your score is {score}")