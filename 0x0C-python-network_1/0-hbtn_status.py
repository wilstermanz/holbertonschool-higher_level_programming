#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request


def main():
    """Main function"""
    with request.urlopen("https://intranet.hbtn.io/status") as resp:
        print(f"Body response:\n\
                \t- type: {type(resp.peek())}\n\
                \t- content: {resp.peek()}\n\
                \t- utf8 content: {resp.peek().decode('utf-8')}")


if __name__ == "__main__":
    main()
