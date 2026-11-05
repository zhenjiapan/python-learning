N = int(input())
maximum = 0
a = int(input())
#(if N > 1:)其实可以删掉，因为(range(N - 1))已经自动处理N = 1
# if N > 1:
#     for i in range(N-1):
#         x = int(input())
#         b = abs(a - x)
#         a = x
#         if b > maximum:
#             maximum = b
for i in range(N-1):
    x = int(input())
    b = abs(a - x)
    a = x
    if b > maximum:
        maximum = b
print(maximum)