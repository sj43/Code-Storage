def solution(nums):

    prefix = []
    for num in nums:
        if prefix:
            prefix.append(prefix[-1] * num)
        else:
            prefix.append(num)

    suffix = []
    for num in reversed(nums):
        if suffix:
            suffix.append(suffix[-1] * num)
        else:
            suffix.append(num)
    suffix = list(reversed(suffix))

    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix[i - 1])
        else:
            result.append(prefix[i - 1] * suffix[i + 1])
    return result



ex1 = [1, 2, 3, 4, 5] # [120, 60, 40, 30, 24]
ex2 = [3, 2, 1] # [2, 3, 6]
print solution(ex1)
print solution(ex2)

