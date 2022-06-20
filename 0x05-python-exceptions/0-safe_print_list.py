#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0

    for li in my_list:
        try:
            if (c < x):
                print("{}".format(li), end="")
                c += 1

        except:
            print("Failed")

    print()

    return c
