from view import *
from db import *

def main():
    while True:
        ans = select_op()
        if ans == 1:
            add_info(get_info())
        if ans == 2:
            delete_contact(deletion())
        if ans == 3:
            make_changes(what_change(), changing())
        if ans == 4:
            search_info(search())
        if ans == 5:
            print(book_view())
        if ans == 6:
            break

main()







# def main():
#     while True:
#         res = select_op()
#         match res:
#             case 1:
#                 add_info(get_info())
#             case 2:
#                 pass
#             case 3:
#                 pass
#             case 4:
#                 search_info(search())
#             case 5:
#                 print(book_view())
#             case 6:
#                 break


# main()