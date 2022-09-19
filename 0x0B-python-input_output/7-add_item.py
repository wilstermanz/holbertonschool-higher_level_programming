#!/usr/bin/python3
"""This module adds all arguments to a list, and saves this to a file"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    from sys import argv
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    save_to_json_file(my_list + argv[1:], "add_item.json")
