# list comprehension example
list_a = [1,4,9,16,25,36,49,64,81,100]

# new_list = []
# for item in list_a:
#     if item % 2 == 0:
#         print(f"Najdena polozka: {item}")
#         new_list.append(item)
#         print(f"Novy list: {new_list}")


#OR use list comprehension
new_list_even = [item for item in list_a if item % 2 == 0]

print(f"List of even numbers: {new_list_even}.")