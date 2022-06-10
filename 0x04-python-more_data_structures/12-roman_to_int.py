#!/usr/bin/python3
def subtract(my_list):
    sub = 0
    max_list = max(my_list)

    for i in my_list:
        if max_list > i:
            sub += i

    return (max_list - sub)


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys = list(rom.keys())

    num = 0
    last = 0
    list_num = [0]

    for ch in roman_string:
        for key in keys:
            if ch == key:
                if rom[ch] <= last:
                    num += subtract(list_num)
                    list_num = [rom[ch]]
                else:
                    list_num.append(rom[ch])

                last = rom[ch]

    num += subtract(list_num)
    return (num)
