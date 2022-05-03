import math
import random

# print(help(math))

value = 4.35

print(math.floor(value))
print(math.ceil(value))
print(round(value))
print(math.pi)
print(math.e)
print(math.nan)
print(math.inf)
print()


print(random.randint(0, 100))
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lst)
random.shuffle(lst)
print(lst)
lst.sort()
print(lst)
