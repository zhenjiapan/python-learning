def interleave(left, right):
    # Complete this function
    res = []
    for i in range(max(n, m)):
        if i < len(left):
            res.append(left[i])
        if i < len(right):
            res.append(right[i])
    return res

n = int(input())
left = []
for text in input().split():
    left.append(int(text))
m = int(input())
right = []
for text in input().split():
    right.append(int(text))
print(interleave(left, right))
