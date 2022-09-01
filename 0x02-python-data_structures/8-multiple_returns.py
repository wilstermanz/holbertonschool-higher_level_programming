#!/usr/bin/python3
def multiple_returns(sentence):
    lenSen = len(sentence)
    if lenSen > 0:
        firstChar = sentence[0]
    else:
        firstChar = "None"
    return (lenSen, firstChar)
