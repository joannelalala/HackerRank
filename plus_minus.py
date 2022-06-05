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
    count_plus = 0
    count_minus = 0
    count_zero = 0

    for i in range(0, len(arr)):
        if arr[i] > 0:
            count_plus += 1
        elif arr[i] == 0:
            count_zero += 1
        else:
            count_minus += 1
    print("{}\n{}\n{}".format(count_plus/n, count_minus/n, count_zero/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
