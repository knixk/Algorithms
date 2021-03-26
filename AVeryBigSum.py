#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.                
def aVeryBigSum(ar):                                      #This problem was fairly simple.
    return(sum(ar))                                       #We used the inbuilt method, called sum to add all elements, and we returned the array.
                            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
