switcher = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z'
}



def factor(n):
    i = 2
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            return n, i

def solution(A):
    letter_list = []
    a, b = factor(A[0])
    if A[1] / a == int(A[1] / a):
        letter_list.append(b)
        letter_list.append(a)
        letter_list.append(A[1] / a)
    else:
        letter_list.append(a)
        letter_list.append(b)
        letter_list.append(A[1] / b)

    for i in xrange(2, len(A)):
        c = letter_list[-1]
        letter_list.append(A[i] / c)

    letter_list2 = set(letter_list)
    letter_list2 = list(letter_list2)
    letter_list2.sort()

    ans = ''

    print letter_list
    print letter_list2

    for l in letter_list:
        idx = letter_list2.index(l)
        ans += switcher[idx]

    return ans



T = input()
for _ in xrange(T):
    N, L = map(int, raw_input().strip().split())
    lst = map(int, raw_input().strip().split())
    sol = solution(lst)
    print 'Case #{0}: {1}'.format(_+1, sol)
