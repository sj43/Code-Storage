# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


# O(N^2 * K) solution

def foo(s, k):
    cur_longest_substring = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) <= k and len(substring) > len(cur_longest_substring):
                cur_longest_substring = substring
    return cur_longest_substring


print(foo('abcba', 2))

# O(N*K) time and O(K) space solution


def bar(s, k):
    if k == 0:
        return 0
    bounds = (0, 0)
    h = {}
    max_length = 0
    for i, char in enumerate(s):

        h[char] = i
        if len(h) <= k:
            new_lower_bound = bounds[0]
        else:
            key_to_pop = min(h, key=h.get)
            new_lower_bound = h.pop(key_to_pop) + 1
            print('key_to_pop = ', key_to_pop)
            print('new_lower_bound = ', new_lower_bound)

        bounds = (new_lower_bound, bounds[1] + 1)
        print('bounds = ', bounds)
        max_length = max(max_length, bounds[1] - bounds[0])
        print(h)
        print()

    return max_length


print(bar('abcba', 2))
