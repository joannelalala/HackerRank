#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr_sum = 0
    nmin, nmax = arr[0], arr[0]
    
    for i in arr:
        arr_sum += i
        if i < nmin:
            nmin = i
        if i > nmax:
            nmax = i
        
    print("{} {}".format(arr_sum - nmax, arr_sum - nmin))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
