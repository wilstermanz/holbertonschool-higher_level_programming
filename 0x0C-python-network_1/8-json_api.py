#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""
import requests
from sys import argv


def main(q=""):
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data={'q': q})
    try:
        dict = req.json()
        id = dict.get('id')
        name = dict.get('name')
        if len(dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception as e:
        print("Not a valid JSON")


if __name__ == "__main__":
    main(argv[1])
