#print("Welcome to the tip calculator")
# total_bill = input("What was the total bill? \n")
# tip_amount = input("What percentage tip would you like to give? \n")
# number_of_people = input("How many people to split the bill? \n")
# tip_amount_abs = float(tip_amount) / 100
# total_tip = float(total_bill) * float((1+tip_amount_abs))
# result_pay = float(total_tip) / float(number_of_people)
# final_pay = round(result_pay, 2)
# print(f"Each person should pay {final_pay}")


#OR:


print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? \n"))
tip_amount = float(input("What percentage tip would you like to give? \n"))
number_of_people = float(input("How many people to split the bill? \n"))
print(f"Each person should pay ${round((total_bill*(1+(tip_amount/100)))/number_of_people, 2)}.")

