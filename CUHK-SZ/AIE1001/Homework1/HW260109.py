accept_count = 0
accept_sum = 0
while True:
    x = int(input())
    if x == -1:
        break
    if x > 0:
        accept_count += 1
        accept_sum += x
print(accept_count, accept_sum)