from datetime import datetime

current_year = int(datetime.now().year)

age = int(input("Please enter your age"))

Birth_year = current_year - age

print("Your Birth year was " + str(Birth_year))
