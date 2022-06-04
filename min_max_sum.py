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
    arr_sort = arr.sort()
    min_sum = 0
    max_sum = 0
    
    for i in range(0, len(arr_sort)-1):
        min_sum += int(arr_sort[i])
        
    for j in range(1, len(arr_sort)):
        max_sum += int(arr_sort[j])
        
    print("{} {}".format(min_sum, max_sum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
