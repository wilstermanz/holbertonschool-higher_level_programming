#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""
import requests


if __name__ == "__main__":
    with requests.get('https://intranet.hbtn.io/status') as r:
        print("Body response:\n\t- type: {}\n\t- content: {}"
              .format(type(r.text), r.text))
