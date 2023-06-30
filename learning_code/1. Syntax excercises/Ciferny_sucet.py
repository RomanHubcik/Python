n = 999
cifra = 0

if n/10 >= 1:
    cifra = cifra + 1
    #print("jedna cifra", n/10)
if n/100 >= 1:
    cifra = cifra + 1
    #print("dve cifry", n/100)
if n/1000 >= 1:
    cifra = cifra + 1
    #print("tri cifry", n/1000)


print("Pocet cifier je:", cifra+1)
