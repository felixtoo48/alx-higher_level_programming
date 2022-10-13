#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    while counter < x:
        try:
            print("{}".format(my_list[counter]), end="")
        except IndexError:
            break
        counter = counter + 1
        print("")
        return counter
