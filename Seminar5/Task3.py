# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

n = int(input())

def prime_number(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


if prime_number(n):
    print('yes')
else:
    print('no')