def add_info(arg):
    with open('database.txt', 'a', encoding='utf-8') as file:
        file.write(arg)


def search_info(arg):
    with open('database.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        res = []
        count = 1
        for i in range(len(lst)):
            if arg in lst[i]:
                res.append(lst[i])
                print(f'{count}. {lst[i]}')
                count += 1
        return res

def delete_contact(arg):
    with open('database.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        res_1 = lst.copy()
        for i in range(len(lst)):
            if arg in lst[i]:
                res_1.remove(lst[i])

    with open('database.txt', 'w', encoding='utf-8') as file:
        file.writelines(res_1)
        
# def make_changes(x,y):
#     with open('database.txt', 'r', encoding='utf-8') as file:
#         lst = file.readlines()
#         res = []
#         print(lst)
#         for i in range(len(lst)):
#             a = lst[i].split()
#             if 'x' in a:
#                 a.pop(i)
#                 a.insert(i, 'y')
#     with open('database.txt', 'w', encoding='utf-8') as file:
#         file.writelines(a)


def book_view():
    with open('database.txt', 'r', encoding='utf-8') as file:
        return file.read()
    

