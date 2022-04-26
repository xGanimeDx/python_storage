import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
# TODO: Investigate best value for variable symbol
symbol = "!@#$%^*(){}[]?"

all = lower + upper + number + symbol
# TODO: Add validation for the input
length = int(input("Enter length of the password: "))
password = "".join(random.sample(all, length))
print("Password generated: ", password)
