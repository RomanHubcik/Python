print((f"Insert the number one: "))
a = input()
print((f"Insert the number two: "))
b = input()

print("Choose an operation: ")
oper = input()

# TODO: test line to highlight

if oper == "+":
    c = int(a) + int(b)
    print(f"{a} + {b} = {c}.")
elif oper == "-":
    c = int(a) - int(b)
    print(f"{a} - {b} = {c}.")
elif oper == "*":
    c = int(a) * int(b)
    print(f"{a} * {b} = {c}.")
elif oper == "/":
    c = int(a) / int(b)
    print(f"{a} / {b} = {c}.")

