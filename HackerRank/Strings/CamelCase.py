# https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    cnt = 1
    
    for i in range(0, len(s)):
        if not (ord(s[i]) >= 97 and ord(s[i]) < 123):
            cnt += 1
    
    return cnt
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
