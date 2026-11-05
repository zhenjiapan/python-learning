def rotate_right(numbers, k):
    # Complete this function
    if n == 0:
        return []

    res = numbers.copy()
    for i in range(k % len(numbers)):
        res = res[n-1:] + res[:n-1]
    return res

n = int(input())
numbers = []
for text in input().split():
    numbers.append(int(text))
k = int(input())
print(rotate_right(numbers, k))
