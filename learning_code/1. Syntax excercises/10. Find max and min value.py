# find min/max value
numlist = [5, 2, 22, 9, 3, 14, 6]

maxval = 0
for item in numlist:
    if maxval < item:
        maxval = item

minval = maxval
for item in numlist:
    if minval > item:
        minval = item
print(f"The max value is: {maxval} and the min value is:{minval}.") 


