#!/usr/bin/python3
def fizzbuzz():
    flag = 0
    for i in range(1, 101):
        if flag == 1:
            print(" ", end='')
        if i % 3 == 0:
            print("Fizz", end='')
        if i % 5 == 0:
            print("Buzz", end='')
        if i % 3 != 0 and i % 5 != 0:
            print(i, end='')
        flag = 1
    print("")
