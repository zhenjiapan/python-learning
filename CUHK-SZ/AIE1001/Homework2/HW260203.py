def first_max_index(numbers):
    # Complete this function
    if n > 0:
        maximum = max(numbers)
        index = numbers.index(maximum)
        return index
    elif n == 0:
        return -1

n = int(input())
numbers = []
for text in input().split():
    numbers.append(int(text))
print(first_max_index(numbers))
