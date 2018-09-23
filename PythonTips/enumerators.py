# from collections import namedtuple
# from enum import Enum
#
#
# class Species(Enum):
#     cat = 1
#     dog = 2
#     horse = 3
#     aardvark = 4
#     butterfly = 5
#     owl = 6
#     platypus = 7
#     dragon = 8
#     unicorn = 9
#     # The list goes on and on...
#
#     # But we don't really care about age, so we can use an alias.
#     kitten = 1
#     puppy = 2
#
#
# Animal = namedtuple('Animal', 'name age type')
# perry = Animal(name='Perry', age=31, type=Species.cat)
# drogon = Animal(name='Drogon', age=4, type=Species.dragon)
# tom = Animal(name="Tom", age=75, type=Species.cat)
# charlie = Animal(name="Charlie", age=2, type=Species.kitten)
#
# charlie.type == tom.type





some_list = ['apple','banana','grapes','pear']
for counter, value in enumerate(some_list):
    print(counter, value)



my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list,3))
print(counter_list)
