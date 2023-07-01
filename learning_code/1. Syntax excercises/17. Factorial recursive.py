
def factorial(num):
    """This is a recursive function to find the factorial of an integer"""

    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))


num = 5
print("The factorial of", num, "is", factorial(num))