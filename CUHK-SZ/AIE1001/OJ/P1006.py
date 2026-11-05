n = int(input())
a = 1
b = 2
i = 0

for i in range(0,n-2):
    if i % 2 == 0:
        a += b
    if i % 2 == 1:
        b += a

    i += 1

if n % 2 == 0:
    print(b % 998244353)
if n % 2 == 1:
    print(a % 998244353)