#list comprehension - генератор списка

#lst = [[i,j] for i in range(5) for j in range(5,10)]
#lst = [i for i in range(5) if i>2]
# lst = [i if i > 2 else 0 for i in range(5)]
# print(lst)
# lst = []
# for i in range(5):
# if i > 2:
# lst.append(i)
# else:
# lst.append(0)

#dict comprehension
# a = [[1,2],[3,4],[5,6],[7,8]]
# dct = {k:v for k,v in a}
# print(dct)

#enumerate - добавляет порядковый номер к элементу последовательности
# a = [4,5,2,1,8]
# for indx, val in enumerate(a):
# print(indx,val)

# zip - соединяет соответствующие элементы последовательности в кортеж
# a = "qwer"
# b = [5, 6, 3, 9, 7]
# c = {0: "z", 1: "x", 2: "y"}
# print(list(zip(a, b, c)))
# for a, b, c in zip(a, b, c):
# print(a, b, c)

#lambda - анонимная функция

# def summ(a,b):
# return a+b
#
# print(summ(5,6))

# summa = lambda a, b: a+b if a<10 else 0
# print(summa(11,8))

#map
# def plus(x):
# if x<5:
# return x*2
# return None
#a = [4, 3, 2, 1, 5]
#print(list(map(str, a)))
#print(list(map(plus, a)))
#print(list(map(lambda x: x*2 if x<4 else -1, a)))

#map
# def plus(x):
# if x<5:
# return x*2
# return None
# a = [4, 3, 2, 1, 5]
#print(list(map(str, a)))
# print(list(map(plus, a)))
# print(list(map(lambda x: x*2 if x<4 else -1, a)))

#filter - фильтрует список
# a = [4, 3, 2, 1, 5]
# print(list(filter(lambda x: x<4, a)))

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

values = [1, 23, 42, 'asdfg']
trasformation = lambda x:x
transformed_values = list(map(trasformation, values))
if values == transformed_values:
 print('ok')
else:
 print('fail')
