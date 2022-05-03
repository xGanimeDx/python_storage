import time
import timeit

def func_one(n):
    return [str(num) for num in range(n)]

start = time.time()
func_one(1000000)
end = time.time()
print(end - start)


def func_two(n):
    return list(map(str, range(n)))


start = time.time()
func_two(1000000)
end = time.time()
print(end - start)
# -----------------------------------------------------------
stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=100000))

stmt = '''
func_two(100)
'''
setup = '''
def func_two(n):
    return list(map(str, range(n)))
'''
print(timeit.timeit(stmt, setup, number=100000))