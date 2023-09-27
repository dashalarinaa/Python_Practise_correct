# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

n = int(input())
numbers = list(map(int, (input().split())))
numbers_new = []
numbers_new = numbers
max = -1
min = 1000

for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    if numbers[i] < min:
        min = numbers[i]
for i in range(len(numbers_new)):
    if numbers_new[i] == max:
        numbers_new[i] = min

print(numbers_new)
