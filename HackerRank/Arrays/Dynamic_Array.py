# https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

    
def dynamicArray(n, queries):
    # Write your code here
    answer = []
    arr = [[] for _ in range(n)]
    last = 0
    for case, x, y in queries:
        idx = (x ^ last) % n
        if case == 1:
            arr[idx].append(y)
        elif case == 2:
            last = arr[idx][y % len(arr[idx])]
            answer.append(last)
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
