fullnames = ['Juraj Menko', 'Peter Novák', 'Ján Koleník', 'Martin Krajcer', 'Jozef Lipa', 'Rudolf Vrtík']

stringname = ""

for x in fullnames:
    #print(x)
    name_surname_list = x.split(' ') 
    stringname += x
    stringname += " "
print(f"List to strings: {stringname}.")
print(f"Namesurname {name_surname_list}.")


stringname_split = stringname.split(" ")
print(stringname_split)

itemnumber = 0

for item in stringname_split:
    itemnumber += 1
    if itemnumber % 2 == 0:
        strlen = len(item)
        print(item, strlen)