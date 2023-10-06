# функции для работы с базой данных
def write_info(info):
    with open("data.txt","a",encoding="utf-8") as file:
        file.write(info)

def get_search(char):
    with open("data.txt","r",encoding="utf-8") as file:
        lst= file.readlines()
        res = []
        count = 1
        for i in range (len(lst)):
            if char in lst[i]:
                res.append(lst[i])
                print(f'{count} - {lst[i]}')
                count += 1
        return res
                 
