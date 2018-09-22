multiples = [i for i in range(30) if i%3==0]
print(multiples)

squared = []
for x in range(10):
    squared.append(x**2)
print(squared)

squared = [x**2 for x in range(10)]
print(squared)




# dict comprehensions

mcase = {'a':10, 'b':34, 'A':7,'Z':3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(),0) + mcase.get(k.upper(),0)
    for k in mcase.keys()
}

#print(mcase_frequency)

print({v: k for k,v in mcase_frequency.items()})


multiples_gen = (i for i in range(30) if i%3 ==0)
print(multiples_gen)
for x in multiples_gen:
    print(x)
