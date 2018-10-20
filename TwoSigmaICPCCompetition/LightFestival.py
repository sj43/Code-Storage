# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
st = input()
st = list(map(int, st))
cnt = 0
on = False
for element in st:
    if element != on:
        cnt += 1
        on = not on
if st[0]==1 and st[-1]==0:
    cnt-=1
if st[0]==0 and st[-1]==1:
    cnt+=1
# for i in range(len(st) - 1, -1, -1):
#     if (on and st[i] == 0) or ((not on) and st[i] == 1):
#         on = not on
#         cnt += 1

print(cnt)
