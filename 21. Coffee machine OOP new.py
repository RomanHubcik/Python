class CoffeeResourcesClass:
    def __init__(self):
        self.coffee_resources_attrib = { 
        "espresso": {"Water": 50, "Milk": 0, "Coffee": 18},
        "latte": {"Water": 200, "Milk": 150, "Coffee": 24},
        "cappucino": {"Water": 250, "Milk": 100, "Coffee": 24},
        }

class CoffeePriceClass:
    def __init__(self):
        self.coffe_price_attrib = {
        "espresso": 1.50,
        "latte": 2.50,
        "cappucino": 3.00
        }

class MachineResourcesClass:
    def __init__(self):
        self.machine_resources_attrib = {
            "Water": 300, 
            "Milk": 200, 
            "Coffee": 100
            }

class CoffeeMachineClass:
    profit = 10
    def __init__(self):
        pass
    

    def is_money_sufficient(self):
        self.fnc_profit = 225
        #self.selected_coffe_price = CoffeePriceClass.coffe_price_attrib[offer]
        print(f"The selected coffee price is: ${selected_coffe_price}.")
        self.penny_value = int(input("How many pennies? ")) * 0.01
        self.nickel_value = int(input("How many nickels? ")) * 0.05
        self.dime_value = int(input("How many dimes? ")) * 0.10
        self.quarter_value = int(input("How many quarters? ")) * 0.25
        self.total_money = self.penny_value + self.nickel_value + self.dime_value + self.quarter_value
        if self.total_money > coffee_price[offer]:
            print(f"Money handled ok. Here is ${self.total_money.selected_coffe_price} in change")
            #global self.profit
            #profit += self.selected_coffe_price
            return True
        else:
            print("Sorry, thats not enough money")
            global continue_offer
            continue_offer = False
            return False

    def is_machine_resources_sufficient(self):
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


coffee_resources = CoffeeResourcesClass()
print(f"Coffee resources: {coffee_resources.coffee_resources_attrib}.")

coffee_price = CoffeePriceClass()
print(f"Coffe price: {coffee_price.coffe_price_attrib}.")

machine_resources = MachineResourcesClass()
machine_status = machine_resources.machine_resources_attrib
print(f"Machine resources: {machine_status}.")

coffee_machine = CoffeeMachineClass()
resources_sufficient = coffee_machine.is_machine_resources_sufficient
profit_value = coffee_machine.profit
money_sufficient = coffee_machine.is_money_sufficient



print(f"Class of cofee machine: {profit_value}.")


continue_offer = True
while continue_offer:  
    #print(f"Continue offer status: {continue_offer}.")
    offer = input("What coffee do you want? Choose Espresso, Latte or Cappucino: ")
    selected_coffe_price = CoffeePriceClass.coffe_price_attrib[offer]
    if offer == "report":
        print(f"Machine resources: {machine_status}.")
        offer = input("What coffee do you want? Choose Espresso, Latte or Cappucino: ")
    elif offer == "profit":
        print(f"Profit: {profit_value}.")
    if resources_sufficient:
        print("Machine resources is sufficient.")  
        if money_sufficient:
            print(f"Enjoy your {offer}!")  