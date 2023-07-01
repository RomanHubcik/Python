n = 12345

cifra = str(n)
print("Zadana cifra je:", cifra)
pocjedn = 0
backward = ''

for i in range(0, len(cifra)):
    backward += (cifra[len(cifra)-i-1:len(cifra)-i])
    
print("Cifra pospatku je: ", backward)
       

#print(cifra[4:5],cifra[3:4],cifra[2:3],cifra[1:2],cifra[0:1])


