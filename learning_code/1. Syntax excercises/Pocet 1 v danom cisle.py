n = 11231

cifra = str(n)
print("Cifra v jednom riadku je:", cifra)
pocjedn = 0

for i in range(0, len(cifra)):

    if cifra[i] == "1":
        pocjedn += 1
             
print("Pocet jednotiek je:", pocjedn)
