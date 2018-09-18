# map applies function to all the items.

# no map

# items = [1,2,3,4,5]
# squared = []
# for i in items:
#     squared.append(i**2)


# map

# items = [1,2,3,4,5]
# squared = list(map(lambda x: x**2, items))
# print(squared)


# can apply to list of functions as wellself.

# def multiply(x):
#     return x*x
# def add(x):
#     return x+x
#
# funcs = [multiply,add]
# for i in range(5):
#     value = list(map(lambda x: x(i), funcs))
#     print(value)


# using filter

# num_list = range(-5, 5)
# less_than_zero = list(filter(lambda x: x < 0, num_list))
# print(less_than_zero)


# using reduce

from functools import reduce

product = reduce(lambda x, y : x*y,[1,2,3,4])
print(product)
