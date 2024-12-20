import pandas as pd

# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]


#Lists of individuals' names and genders
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

age_gender = list(zip(ages,gender))
name_age_gender = dict(zip(names, age_gender))

# Convert dictionary to DataFrame
name_age_gender_df = pd.DataFrame(name_age_gender)

print(name_age_gender_df)