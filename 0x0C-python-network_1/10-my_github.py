#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""
import requests
from sys import argv


def main():
    print(requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
                  .json()
                  .get('id')
          )


if __name__ == "__main__":
    main()
