fullnames = ['Juraj Menko', 'Peter Novák', 'Ján Koleník', 'Martin Krajcer', 'Jozef Lipa', 'Rudolf Vrtík']

for fullname in fullnames:                                    # Go over each fullname
    name_surname_list = fullname.split(' ')                   # Splits each fullname into 2 parts: Firstname + Surname (space is used as separator between them)
    surname = name_surname_list[1]                            # Read last element = it is the surname always
    count_characters = len(surname)                           # Calculate count of characters in surname
    print(f'{surname} has {count_characters} characters.')    # Print final result