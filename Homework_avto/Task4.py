# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

# def power(num, degree, res):
#     if degree == 0:
#         return res
#     return power(num, degree - 1, res * num)


# res_1 = 1
# print(power(num_1, degree_1, res_1))

# a = 3
# b = 5
# print(f(a, b))

def f(a, b):
    if b == 0:
        return 1
    return a * f(a, b-1)
    
a = 3
b = 5
print(f(a, b))
