N = int(input())
if N <= 20:
    credit = N*2
else:
    credit = 20*2 + (N-20)*1
print(credit)