# sum of two numbers
xy = input("Type two digit number: ")
a = xy[0]
b = xy[1]
summary = 0

if str(len(xy)) >= str(3):
    print("There is more than 2 numbers!" + str(len(xy)))
else:
    summary = (int(a)+int(b))
    print("Sum of first 2 digits is: " + str(summary))
    print(f"Sum of first 2 digits is: {summary}.") # more sipmle with f string