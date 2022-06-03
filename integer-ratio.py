#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = len([x for x in arr if x > 0])
    negative = len([x for x in arr if x < 0])
    zero = len([x for x in arr if x == 0])
    
    print("{}\n{}\n{}".format(positive/n, negative/n, zero/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)