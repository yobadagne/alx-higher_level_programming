#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
        elif ord(c) == 8:
            c = chr(8)
            print ("{}".format(c))
        else:
            print("{}".format(c)))
