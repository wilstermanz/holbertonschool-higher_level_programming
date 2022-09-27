#!/usr/bin/python3
flag = 0
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            if flag == 1:
                print(", ", end="")
            print("{}{}".format(i, j), end="")
            flag = 1
print("")
