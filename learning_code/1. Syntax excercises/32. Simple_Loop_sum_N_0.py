n = 5
sucet = 0

for i in range(0, n):
#or for i in range(n):
    sucet += i   # is the same as sucet = sucet + i
    print("Iteration number", i+1)
    print("Sum of selected number is:", sucet, "+", i+1, "=", sucet+i+1)

# 0+1+2+3+4 ==> n=5 

#  0 + 1 =  1 
#  1 + 2 =  3
#  3 + 3 =  6
#  6 + 4 = 10
# 10 + 5 = 15
#------------
# 15 + 6 = 21
# 21 + 7 = 28
# 28 + 8 = 36
# 36 + 9 = 45
# 45 +10 = 55   