# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# a = [int(input()) for i in range (8)]
# print(a)
# count = 0
# b = a[0]

# for i in range (8):
#     if b != a[i]:
#         i += 1
#         count += 1
# print(count)

a = [1, 1, 2, 0, -1, 3, 4, 4]
b = set(a)
print(len(b))