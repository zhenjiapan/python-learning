def running_totals(numbers):
    # Complete this function
    res = []
    sum = 0
    for i in range(n):
        sum += numbers[i]
        res.append(sum)
    return res

n = int(input())
numbers = []
for text in input().split():
    numbers.append(int(text))
print(running_totals(numbers))
