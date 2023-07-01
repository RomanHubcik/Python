import math

# constants
input_width = float(input("Width of wall:"))
input_height = float(input("Height of wall:"))
coverage = 5

def paint_calc(width, height, coverage):
    paint_area = width * height
    num_of_cans = (paint_area / coverage)
    print(f"You will need {num_of_cans} cans exactly, so buy {math.ceil(num_of_cans)} cans.")


paint_calc(width=input_width, height=input_height, coverage=coverage)
