#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response
"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    """import guarded"""
    data = parse.urlencode({'email': argv[2]})
    data = data.encode()
    email = request.Request(argv[1], data)
    with request.urlopen(email) as resp:
        print(resp.read().decode('utf8'))
