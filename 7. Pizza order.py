print("Welcome to Python Pizza deliveries!.")

size = input("What pizza size do you want? (S, M, L) \n")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
#else:
#    print("Wrong key.")
#    bill = 0
print(f"Subtotal: ${bill}. \n")

add_pepper = input("Do you want pepperoni? (Y/N) \n")
if add_pepper == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
print(f"Subtotal: ${bill}. \n")

extra_cheese = input("Do you want extra cheese? (Y/N) \n")
if extra_cheese == "Y":
    bill += 1
print(f"Subtotal: ${bill}. \n")

print(f"Total price is: {bill}")
