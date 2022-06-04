#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    least, most = scores[0], scores[0] # becoz scores is a list of scores, and we create two placeholders for least and most
    mincount, maxcount = 0, 0

    for i in scores:
        if i < least:
            least = i
            mincount += 1
        if i > most:
            most = i
            maxcount += 1
    return [maxcount, mincount]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
