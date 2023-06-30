num = 5
fact = 1

for i in range(1, num):
    fact = fact*num
    num -= 1
    
print(f"Faktorial: {fact}.")
