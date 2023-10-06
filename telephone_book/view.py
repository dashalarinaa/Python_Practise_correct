# функции для работы с пользователем

def select_op():
    op = int(input("Выбери что хочешь сделать:\n1-Новая запись\n2-Вывод\n"))
    return op 

def get_info():
    fio = input("Введите ФИО:  ")
    tel = input("Введите номер телефона: ")
    data = fio + " " + tel
    return data  

def search():
    search_info = input('Введите фио или тел: ')
    return search_info