#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    """import guarded"""
    req = request.Request("https://intranet.hbtn.io/status")
    with request.urlopen(req) as resp:
        resp = resp.read()
        print(f"Body response:\n"
              f"\t- type: {type(resp)}\n"
              f"\t- content: {resp}\n"
              f"\t- utf8 content: {resp.decode('utf8')}"
              )
