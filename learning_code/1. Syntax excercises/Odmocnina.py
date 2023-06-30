n = 25
x = 0
result = 0

for i in range(0,n):
    x = x + 1
    if x*x <= n: 
        result = x
print("Najblizsia cela mocnina cisla", n,"je:", result)