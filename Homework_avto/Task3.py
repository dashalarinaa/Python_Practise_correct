# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# d = {1: 'AEIOULNSTR',
# 2: 'DG',
# 3: 'BCMP', 
# 4: 'FHVWY', 
# 5: 'K',
# 8: 'JX',
# 10: 'QZ',
# }


# d = {
# 1: 'АВЕИНОРСТ', 
# 2: 'ДКЛМПУ',
# 3: 'БГЁЬЯ', 
# 4: 'ЙЫ', 
# 5: 'ЖЗХЦЧ', 
# 8: 'ШЭЮ', 
# 10: 'ФЩЪ' }
#  print(d.lower())
# k = 'ноутбук'

# print(d)
# result = [key for letter in k for key, value in d.items() if letter in value]
# print(sum(result))


# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)


# print('Как тебя зовут?')
# name = input()
# print('Привет,', name)

# print('a', 'b', 'c', sep='', end='')

# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')

# a = 2 % 5
# print(a)

# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)

# a = 82 // 3 ** 2 % 7
# print(a)

# print("The world's a little blurry", "Or maybe it's my eyes", end='!!!', sep=' :) ')
# s = 13
# k = -5
# d = s + 2
# s = d
# k = 2 * s
# print(s + k + d)

a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)