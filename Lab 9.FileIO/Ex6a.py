import json

quiz_data_file = open('./quiz_questions.json', 'r')
quiz_data_json = quiz_data_file.read()
quiz_data = json.loads(quiz_data_json)

print(quiz_data["What is Pau Hana"])