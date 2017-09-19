#!/usr/bin/env python3
""" This is a program from the /r/learnpython subreddit list of python
    practice programs
    it will ask you to what digit do you want to display pi and then
    print pi to that digit """


def readpifile():
    """ Reads pi from the files pi.txt. """
    pifile = open('pi.txt', 'r')
    return pifile.read()

def getn():
    """ get the number of digits to display from the user
        if the nimber is more than one add one to it to account for
        the decimal point"""
    num = int(input("How many digits of pi do you want to display? "))
    if num > 1:
        num = num + 1
    return num

N = getn()

if N > 12120 or N < 1:
    print("Number of digits must be above 0 and below 12120.")

else:
    print(readpifile()[:N])
