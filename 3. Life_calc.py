from calendar import day_abbr, week


age = input("What is your current age? ")
years_remaining = 90 - int(age) 
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365
print(f"Until 90 years remains {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks and {days_remaining} days.")

#age = 12
#print("You are " + str(age) + "years old.") - age is int and only string can be concatenated
#print(f"You are {age} years old.") - here I dont have to think about data type concat.