#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for li in my_list:
            if (c < x):
                print("{}".format(li), end="")
                c += 1
        print()

    except:
        print("Failed")

    return c
