# Последовательность Фибоначчи/
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fib(a):

#     if a == 1 or a == 2:
#         return 1
#     return fib(a-1) + fib(a-2)
# a = int(input())
# print(fib(a))

# 0 1 1 2 3 5 8 13 21
# 0 1 2 3 4 5 6 7  8

def fib(a):

    if a == 0:
        return 0
    if a == 1:
        return 1
    return fib(a-1) + fib(a-2)
a = int(input())
print(fib(a))