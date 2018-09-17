import functools

with open('test.txt', 'r') as f:
    data = f.readlines()
num = []
for d in data:
    num.append(int(d))
avg = functools.reduce(lambda x, y: x + y, num) / len(num)
total = sum(num)
with open('result.txt', 'w') as f2:
    f2.write(str(avg) + ' ')
    f2.write(str(total))
