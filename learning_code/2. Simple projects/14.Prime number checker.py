print("The prime number checker.")
checknumber = int(input("What number do you want to check?"))

dividednumbers = 0
for iter in range(1, checknumber+1): #checknumber+1, lebo posledne cislo sa nerata do cyklu
    modulo = checknumber % iter
    if modulo == 0:
        dividednumbers += 1

if dividednumbers == 2:
    print("YES, this it the prime number.")
elif checknumber == 1:
    print("YES, this it the prime number.")
else:
    print("NO, this is not the prime number.")


#OR as a function with input parameter
# def primenumcheck(checknumber):
#     dividednumber = 0
#     for iter in range(1, checknumber+1): #checknumber+1, lebo posledne cislo sa nerata do cyklu
#         modulo = checknumber % iter
#         if modulo == 0:
#             dividednumber += 1
#     if dividednumber == 2:
#         print("YES, this it the prime number.")
#     elif checknumber == 1:
#         print("YES, this it the prime number.")
#     else:
#         print("NO, this is not the prime number.")
        
# primenumcheck(checknumber=checknumber)
