#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    sum = 0
    r_to_i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(0, len(roman_string)):
        if i > 0 and r_to_i[roman_string[i]] > r_to_i[roman_string[i-1]]:
            sum -= r_to_i[roman_string[i-1]]
            sum += r_to_i[roman_string[i]] - r_to_i[roman_string[i-1]]
        else:
            sum += r_to_i[roman_string[i]]

    return sum
