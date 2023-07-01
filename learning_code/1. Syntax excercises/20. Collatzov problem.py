n=47

#def collatz(n):
while n != 1:
    print(n,",", end = '')
    if n % 2 == 0:
        n = n / 2
    else:
        n = n*3 + 1