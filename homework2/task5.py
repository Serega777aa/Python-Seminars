from random import *

nums = []
for i in range(5):
    nums.append(randint(0, 10))
print(nums)

def mix_list(col:list):
    for i in range(len(col)):
        rand = randint(0, len(col) - 1)
        if rand >= i:
            col[i], col[rand] = col[rand], col[i]
    

mix_list(nums)
print(nums)
