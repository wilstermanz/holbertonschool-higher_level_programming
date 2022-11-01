#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    """import guarded"""
    with request.urlopen("https://intranet.hbtn.io/status") as resp:
        print(f"Body response:\n"
              f"\t- type: {type(resp.peek())}\n"
              f"\t- content: {resp.peek()}\n"
              f"\t- utf8 content: {resp.peek().decode('utf-8')}\n"
              )
