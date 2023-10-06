# связь view c db

from view import *
from db import *

def main():
    while True:
        ans = select_op()
        if ans == 1:
            human_info = get_info()
            write_info(human_info)
        if ans == 2:
            characteristic = search()
            get_search(characteristic)



main()