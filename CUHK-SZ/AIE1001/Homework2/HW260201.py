def clamp_values(numbers, low, high):
    # Complete this function
    res = []
    for i in range(len(numbers)):
        if numbers[i] < low:
            res.append(low)
        elif numbers[i] > high:
            res.append(high)
        else:
            res.append(numbers[i])
    return res

n = int(input())
numbers = []
for text in input().split():
    numbers.append(int(text))
bounds = input().split()
low = int(bounds[0])
high = int(bounds[1])
print(clamp_values(numbers, low, high))
