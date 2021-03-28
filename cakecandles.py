#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(ar):
    # Write your code here
    c = 0                                   #we set the count variable as c
    temp = ar[0]                            #we set the temp var as the first index of array
    for i in range(1, len(ar)):             #we loop through the array in the range of 1 to n (*note not 0)
        if ar[i] > temp:                    #if found a value greater than index 0 we set it as temp
            ar[i] = temp    
    for i in range(0, len(ar)):             #now we check traverse again to check if there is more instances of the var temp
        if ar[i] == temp:
            c += 1                          #if we find any we increment by 1
    return c                                #we return the answer as c
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
