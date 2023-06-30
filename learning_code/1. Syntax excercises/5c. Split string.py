fullnames = ['Juraj Menko', 'Peter Novák', 'Ján Koleník', 'Martin Krajcer', 'Jozef Lipa', 'Rudolf Vrtík']

# stringname = ""
# for x in fullnames:
#     #print(x)
#     name_surname_list = x.split(' ') 
#     stringname += x
#     stringname += " "
#     #print(f"Load full name: {name_surname_list}.")
# #print(f"List to strings: {stringname}.")

# stringname_split = stringname.split(" ")
# #print(f"Split strings: {stringname_split}")

# itemnumber = 0
# for item in stringname_split:
#     itemnumber += 1
#     if itemnumber % 2 == 0:
#         strlen = len(item)
#         print(f"{item} has {strlen} characters.")


#OR
for fullname in fullnames:                                    # Go over each fullname
    name_surname_list = fullname.split(' ')                   # Splits each fullname into 2 parts: Firstname + Surname (space is used as separator between them)
    surname = name_surname_list[1]                            # Read last element = it is the surname
    count_characters = len(surname)                           # Calculate count of characters in surname
    print(f'{surname} has {count_characters} characters.')    # Print final result