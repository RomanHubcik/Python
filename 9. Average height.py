height_list = [165, 159, 188, 173, 168, 184, 193]
sum_value = 0
list_lenght = len(height_list)

for height in height_list:
    sum_value += height

print(f"Average height is: {(round((float(sum_value)/float(list_lenght)), 2))} cm.")
