print(0x3A8)
print(1.2e3)
print(1.2e-3)
print(float('-inf'))
print(~0)


class Silly:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return 'Silly' + str(self.x)


print(str(Silly(3)))

print('peAr'.capitalize())
print(list({1: 2, 3: 4}))
print(list('abc'))
print(list(enumerate(['a', 'b', 'c', 'd'])))
print(list(enumerate('abcd')))
a_list = ['a', 'b', 'c']
a_list.insert(3, 'd')
print(a_list)
a_list.insert(7, 'e')
print(a_list)
a_list.reverse()
print(a_list)

words = 'This is a test string from Andrew'.split()
print(words)

words.sort()
print(words)
words.sort(reverse=True)
print(words)
