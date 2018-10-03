# s = input()
# n = int(input())
# for dummy_i in range(n):
#     start_index, end_index = input().split()
#     start_index = int(start_index)
#     end_index = int(end_index)
#
#     max = 0
#
#     for idx in range(len(s) - end_index):
#         if s[idx + start_index] == s[idx + end_index]:
#             max += 1
#         else:
#             break
#     print(max)
#
#     # slice1 = s[start_index:]
#     # slice2 = s[end_index:]
#     # slices_zipped = zip(slice1, slice2)
#
#     # for idx in range(len(slice2)):
#     #     if slice1[idx] == slice2[idx]:
#     #         max += 1
#     #     else:
#     #         break
#     # print(max)
a = 1
def abc(b):
    b += 1
abc(a)
print(a)
