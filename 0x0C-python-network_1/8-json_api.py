#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""
import requests
from sys import argv


def main(q=""):
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        r_dict = r.json()
        if len(r_dict) == 0:
            print("No Result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    main(argv[1]) if len(argv) != 1 else main()
