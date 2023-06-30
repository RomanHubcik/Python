def greet(name, location): #parameters inside the brackets
    print(f"Hello {name}")
    print(f"How do you do {name} ?")
    print(f"Isnt weather nice here in {location}?")

greet("Angela", "Nitra") #positional arguments inside - they depend on the order of data inside brackets (name = angela etc)
greet(name = "Angela", location = "Nitra") #keyword arguments - better, no misalign with params