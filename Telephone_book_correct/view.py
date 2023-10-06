def select_op():
    op = int(input('Выберите действие:\n1.Добавить контакт\n2.Удалить контакт\n'
'3.Изменить контакт\n4.Показать контакт\n5.Посмотреть все контакты\n6.Выход\n'))
    return op

def get_info():
    name = input('Введите имя:\n')
    number = input('Введите номер телефона:\n')
    data = name + ' ---> ' + number + '\n'
    return data

def search():
    return input('Введите имя или телефон:\n')

def deletion():
    return input('Введите имя или телефон, который нужно удалить: ')

def what_change():
    n1 = input ('Что заменить (Введите имя или телефон): ')
    
    return n1
def changing():
    n2 = input('На что заменить: ')
    return n2