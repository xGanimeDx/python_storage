import random

def gensquares(N):
    for num in range(N):
        yield num**2

for x in gensquares(10):
    print(x)


def rand_num(low, high, n):
    for _ in range(n):
        yield random.randint(low, high)

for x in rand_num(1, 10, 12):
    print(x)


s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
