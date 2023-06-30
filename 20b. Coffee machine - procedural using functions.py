coffee_resources = { 
    "espresso": {"Water": 50, "Milk": 0, "Coffee": 18},
    "latte": {"Water": 200, "Milk": 150, "Coffee": 24},
    "cappucino": {"Water": 250, "Milk": 100, "Coffee": 24},
    }

coffee_price = {
    "espresso": 1.50,
    "latte": 2.50,
    "cappucino": 3.00
    }

machine_resources = {"Water": 300, "Milk": 200, "Coffee": 100}
print(f"Access: {machine_resources}.")

def resources_report(machine_resources):
    print(f"Water: {machine_resources['Water']} ml")
    print(f"Milk: {machine_resources['Milk']} ml")
    print(f"Coffe: {machine_resources['Coffee']} ml")

profit = 0
def is_money_sufficient():
    selected_coffe_price = coffee_price[offer]
    print(f"The selected coffee price is: ${selected_coffe_price}.")
    penny_value = int(input("How many pennies? ")) * 0.01
    nickel_value = int(input("How many nickels? ")) * 0.05
    dime_value = int(input("How many dimes? ")) * 0.10
    quarter_value = int(input("How many quarters? ")) * 0.25
    total_money = penny_value + nickel_value + dime_value + quarter_value
    if total_money > coffee_price[offer]:
        print(f"Money handled ok. Here is ${total_money-selected_coffe_price} in change")
        global profit
        profit += selected_coffe_price
        return True
    else:
        print("Sorry, thats not enough money")
        global continue_offer
        continue_offer = False
        return False

continue_offer = True
def is_machine_resources_sufficient():
    selected_coffee = coffee_resources[offer]
    for item in selected_coffee: 
        if machine_resources[item] < selected_coffee[item]:
            global continue_offer
            continue_offer = False
            print(f"There is not enough resources. Continue offer status is: {continue_offer}.") 
            return False
        else:
            machine_resources[item] -= selected_coffee[item]
            return True
    print(f"Updated machine resources: {machine_resources}.")
    return offer

while continue_offer:
    print(f"Continue offer status: {continue_offer}.")
    offer = input("What coffee do you want? Choose Espresso, Latte or Cappucino: ")
    if offer == "report":
        print(f"Machine resources: {machine_resources}.")
        offer = input("What coffee do you want? Choose Espresso, Latte or Cappucino: ")
    elif offer == "profit":
        print(f"Profit: {profit}.")
    if is_machine_resources_sufficient():
        print("Machine resources is sufficient.")  
        if is_money_sufficient():
            print(f"Enjoy your {offer}!")  