years_tuple = (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989)
respondents_tuple = (17, 35, 26, 26, 25, 27, 35, 21, 19)


# Dictionary using dict() and list comprehensions
survey_data = dict(
   years = [year for year in years_tuple],
   respondents = [respondent for respondent in respondents_tuple]
)


print(survey_data)