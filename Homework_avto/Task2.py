# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5]
k = 6
# min = k - list_1[0]
# for i in range(len(list_1)):
#     if k - list_1[i] < k - list_1[0]:
#         min == k - list_1[i]        
# print(min)
    
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)