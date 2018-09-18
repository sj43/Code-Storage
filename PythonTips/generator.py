
# using generator

# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# for x in fibon(100):
#     print(x)



# not using generator

# def fibon(n):
#     a = b = 1
#     result = []
#     for i in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result
#
# print(fibon(100))


# to see that generator only iterates once

# def generator_function():
#     for i in range(3):
#         yield i
#
# gen = generator_function()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter))
