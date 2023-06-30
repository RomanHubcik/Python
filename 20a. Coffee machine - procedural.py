water = int(300)
milk = int(200)
coffee = int(100)
resources_sufficient = True

while resources_sufficient:
    print("What would you like? (espresso/latte/cappucino)")
    coffee_chosen = input()

    if coffee_chosen == "report":
        print(f""" Resources status:
            Water: {water} ml
            Milk: {milk} ml
            Coffee: {coffee} ml """)
        print("\nWhat would you like? (espresso/latte/cappucino)")
        coffee_chosen = input()

    if coffee_chosen == "espresso":
        price = float(1.50)

    elif coffee_chosen == "latte":
        price = float(2.50)

    elif coffee_chosen == "cappucino":
        price = float(3.00)

    inserted_pennies = 0
    inserted_nickels = 0
    inserted_dimes = 0
    inserted_quarters = 0

    print(f"The coffe price is ${price}. Please insert coins.")

    print("How many pennies? ")
    inserted_pennies = float(int(input())*0.01)

    print("How many nickels? ")
    inserted_nickels = float(int(input())*0.05)

    print("How many dimes? ")
    inserted_dimes = float(int(input())*0.10)

    print("How many quarters? ")
    inserted_quarters = float(int(input())*0.25)

    total_sum = inserted_pennies + inserted_nickels + inserted_dimes + inserted_quarters
    print(f"Total sum of inserted coins is: ${round(total_sum,2)}.")

    refund = total_sum - price
    if refund < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is {round(refund, 2)} in change. Here is your {coffee_chosen}, enjoy!")

    if coffee_chosen == "espresso":
        water = water - int(50)
        coffee = coffee - int(18)
        if water < int(50) or coffee < int(18):
            print("Not enough resources.")
            resources_sufficient = False

    elif coffee_chosen == "latte":
        water = water - int(200)
        milk = milk - int(150)
        coffee = coffee - int(24)
        if water < int(200) or milk < int(150) or coffee < int(24): 
            print("Not enough resources.")
            resources_sufficient = False

    elif coffee_chosen == "cappucino":
        water = water - int(250)
        milk = milk - int(100)
        coffee = coffee - int(24)
        if water < int(250) or milk < int(100) or coffee < int(24):
            print("Not enought resources.")
            resources_sufficient = False