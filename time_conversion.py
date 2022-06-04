#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # because the input format is like "12:01:00PM", the first 8 digits are numbers, the rest is AM/PM
    t = s[8:]
    dn = s[:8]
    h, m, s = t.split(":") # separate hour, minute, and second with colon
    h = int(h)

    if dn == "PM":
        if h != 12: # not midnight 12 o'clock
            h += 12
        return "{}:{}:{}".format(h, m, s)
    
    else: # dn == "AM"
        if h == 12: # at noon
            h = 0
        h = "0" + str(h) # add a leading 0
        return "{}:{}:{}".format(h, m, s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
