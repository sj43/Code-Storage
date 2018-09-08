import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    ans = 0
    counter = 0
    while(n > 0):
        counter += 1
        counter = counter * (n % 2)
        ans = max(counter, ans)
        n = n // 2
    print(ans)
