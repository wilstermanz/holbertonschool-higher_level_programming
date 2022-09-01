#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    list_copy = my_list.copy()

    if idx < len(my_list) and idx >= 0:
        list_copy[idx] = element

    return list_copy
