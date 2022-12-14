#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    """import guarded"""
    with request.urlopen(argv[1]) as resp:
        resp = dict(resp.info())
        print(resp['X-Request-Id'])
