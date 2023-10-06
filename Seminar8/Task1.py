#open("papka/input.txt","r")
#"r" - чтение файла
#"w" - создание/запись в файл + уничтожение предыдущих записей
#"a" - создание/запись в файл + сохранение предыдущих записей

# file = open("input.txt", "a",encoding="utf-8")
# file.write("привет\n")#запись строки в файл
# a = ["rt\n", "34\n", "это я!\n"]
# file.writelines(a)#запись элементов списка в файл
# file.close()#закрытие файла



#with open("input.txt","r",encoding="utf-8") as file:
#lst = file.readlines()#возвращает список, каждый элемент - строка в файле
#print(lst)
#file.seek(0)#перенос курсора внутри файла на нужную позицию
#print(file.readlines())
#lst = [string.strip() for string in lst] - убираем \n символ
#print(file.read())# - возвращает содержимое файла в виде строки
# file.seek(0)
# for i in range(5):
# print(file.readline().strip())#-читает файл построчно


