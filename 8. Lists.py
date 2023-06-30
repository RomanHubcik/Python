#create an empty list
empty_list = []

#create list with values
empty_list = ["new", 1, ["nested", "list"]]

#add something to this list
empty_list.append("append")

print(f"Print nested list with appended value: {empty_list}.")

#double list
fruits = ["a", "s", "d", "f"]
vegies = ["j", "k", "l", "o"]

#two lists in variable
dirty_dozen =  [fruits, vegies]

#print from the 2nd list the 4th item
print(f"Two dimensional list string value: {dirty_dozen[1][3]}.") 

#list every item of fruits list into new line
for i in fruits:
    print(f"String from list fruits: {i}.")

