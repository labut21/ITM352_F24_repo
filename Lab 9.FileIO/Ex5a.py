import json

quiz_data = {
     "What is Pau Hana": [
          "A type of fish",
          "The end of the workday",
          "A Hawaiian chant",
          "A luau fish"
     ],
     "What is the Hawaiian word for responsibility or privilege": [
          "Kuleana",
          "Mana",
          "Pono",
          "Aina"
     ],
     "What is the term for a native Hawaiian story or legend": [
          "Mele",
          "Mo'olelo",
          "Hula",
          "Kahuna"
     ],
     "What is a Kahuna": [
          "Leader of a hula group",
          "A Hawaiian shaman or priest ",
          "A type of canoe",
          "A Hawaiian mountain"
     ],
     "What does E komo mai mean": [
          "Goodbye",
          "Welcome",
          "Come back soon",
          "Blessings"
     ]
}

quiz_data__json = json.dumps(quiz_data)

quiz_data_file = open('quiz_questions.json', 'w')
quiz_data_file.write(quiz_data__json)
quiz_data_file.close()