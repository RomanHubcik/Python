#1. Sums - write a function check_sum(), which, given li, a list of integers, and num, returns whether
#any two numbers in li add up to num. There are no duplicates in li.

# from itertools import permutations

# li = [1,2,3,4,5,6,7]
# sum = 7
# #print(li[3])

# item = 0
# this_elem = 0
# next_elem = 1

# # for item in li:
# #     #print(f"{this_elem} plus {next_elem} = {this_elem+next_elem}.")
# #     if (this_elem + next_elem) == 7:
# #         print('true')
# #     else:
# #         print('false')
# #     this_elem += 1
# #     next_elem += 1

# solutions = [pair for pair in permutations(li, 2) if (pair+pair) == 6]
# print('Solutions:', solutions)

#or all combinations - nested loop ...


#2. overlap
li=[[1,5], [8,9], [3,6]]

#check if the 2nd of ith is > than 2nd of jth
for item in li:
    print(item[1])
    if item[1] <= 
