S = input()
K = int(input())
for i in range(K):
    if i < K-1:
        print(S, end='-')
    else:
        print(S)