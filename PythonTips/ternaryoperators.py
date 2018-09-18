is_nice = True
state = 'nice' if is_nice else 'not nice'
print(state)


nice = True
personality = ('mean','nice')[nice]
print("The cat is ",personality)

condition = True
print(2 if condition else 1/0)
print((1/0,2)[condition])
