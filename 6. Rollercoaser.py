print("Welcome to the rollercoaster!")

height = int(input("What is your height? \n"))
age = int(input("How old are you? \n"))

if height >= 120:
    if age >= 18:
        print("Welcome. Ticket price is $12.")
    elif age <=12:
        print("Welcome. Ticket price is $5.")
    else:
        print("Welcome. Ticket price is $8.")

else:
    print("Go somewhere else.")

