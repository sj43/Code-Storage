import math
import os
import random
import re
import sys
# Complete the closest function below.


def closest(s, queries):
    result = []
    for query in queries:
        find_this_char = s[query]
        back_and_forth = 1
        cnt = 0
        cur_pos = query
        left_side_running = True
        right_side_running = True
        while True:
            if left_side_running and right_side_running:
                back_and_forth *= -1
                cnt += 1
                cur_pos += cnt * back_and_forth
            elif left_side_running:
                cur_pos -= 1
            elif right_side_running:
                cur_pos += 1
            else:
                result.append(-1)
                break
            if cur_pos < 0:
                left_side_running = False
                cur_pos += cnt * back_and_forth * (-1)
                continue
            elif cur_pos >= len(s):
                right_side_running = False
                cur_pos += cnt * back_and_forth * (-1)
                continue
            if(s[cur_pos] == find_this_char):
                result.append(cur_pos)
                break
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
