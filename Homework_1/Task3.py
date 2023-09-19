# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

N = int(input())
count = 0
for i in range (0, N):
    temp = 2 ** count
    count += 1
    if temp >= N:
        break
    print(temp)