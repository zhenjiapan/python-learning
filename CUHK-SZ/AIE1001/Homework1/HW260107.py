L = int(input())
R = int(input())
K = int(input())
count = 0
for i in range(L, R+1):
    if i % K == 0:
        count += 1
print(count)