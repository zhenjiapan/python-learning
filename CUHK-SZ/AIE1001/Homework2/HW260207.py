def swap_positions(numbers, i, j):
    # Complete this function
    x = numbers[j]
    numbers[j] = numbers[i]
    numbers[i] = x

n = int(input())
numbers = []
for text in input().split():
    numbers.append(int(text))
positions = input().split()
i = int(positions[0])
j = int(positions[1])
swap_positions(numbers, i, j)
print(numbers)
