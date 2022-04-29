import profile
from bson import List
from functools import reduce

from numpy import prod

def main():
    print("Test Map, Reduce and Filters")

#map
def multiple(x):
    return x * x

def add(x):
    return x + x

funcs = [multiple, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print("Map sample",list(value))  

#filter   
number_list = range(-5, 5)
def filter_fun(number_list):
    less_than_zero = list(filter(lambda x: x < 0, number_list))
    print("Filter Sample: ",less_than_zero)

filter_fun(number_list)

#reduce
product = reduce((lambda x, y: x + y), [1,2,3,4])
print("Reduce Sample:", product)

if __name__ == "__main__":
    main()
