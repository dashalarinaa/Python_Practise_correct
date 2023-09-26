# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
n = int(input())
m = int(input())

n_numbers = list(map(int, input().split()))
m_numbers = list(map(int, input().split()))
n_set = set(n_numbers)
m_set = set(m_numbers)

a_set = n_set.intersection(m_set)
a_set = sorted(a_set)
print(' '.join(list(map(str, a_set))))