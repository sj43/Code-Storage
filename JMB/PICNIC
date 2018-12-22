from collections import defaultdict

def count_pairings(taken):
    cur_student = -1

    for i in xrange(n):
        if not taken[i]:
            cur_student = i
            break

    if cur_student == -1:
        return 1

    ret = 0

    for pair_with in xrange(cur_student + 1, n):
        if not taken[pair_with] and are_friends(cur_student, pair_with):
            taken[cur_student] = True
            taken[pair_with] = True
            ret += count_pairings(taken)
            taken[cur_student] = False
            taken[pair_with] = False
    return ret


def are_friends(first, second):
    return _are_friends[(first, second)]


for _ in xrange(input()):
    n, m = map(int, raw_input().strip().split())
    _are_friends = defaultdict(bool)
    friends_relationships = map(int, raw_input().strip().split())
    for i in xrange(0, 2 * m, 2):
        first_person = friends_relationships[i]
        second_person = friends_relationships[i+1]
        _are_friends[(first_person, second_person)] = True
        _are_friends[(second_person, first_person)] = True
    taken = [False] * n
    print count_pairings(taken)
        
