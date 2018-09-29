import math
import os
import random
import re
import sys
# Complete the closest function below.


def closest(s, queries):
    result = []
    for query in queries:
        ch = s[query]
        last_index = s.rfind(ch, 0, query)
        first_index = s.find(ch, query + 1)
        if last_index == -1 and first_index == -1:
            result.append(-1)
        elif last_index == -1:
            result.append(first_index)
        elif last_index == -1:
            result.append(last_index)
        else:
            result.append(last_index if abs(last_index - query) <=
                          abs(first_index - query) else first_index)
    return result



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    res = closest(s, queries)
    print(res)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
