# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

N = int(input())
numbers_n = []
for i in range(N):
    numbers_n.append(int(input()))
print(numbers_n)

M = int(input())
numbers_m = []
for i in range(M):
    numbers_m.append(int(input()))
print(numbers_m)

numbers_a = []
for el in numbers_n:
    if el not in numbers_m:
        numbers_a.append(el)
print(numbers_a)