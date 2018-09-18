from collections import defaultdict

s = [('a', 100), ('b', 200), ('c', 300), ('a', 150), ('c', 120)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

d.items()
