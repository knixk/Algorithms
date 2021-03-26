#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    sum = 0                                               #initialized the sum variable
    for i in ar:                                          #looping through the array ar
        sum += i                                          #we increment the current position of i
    return sum                                            #then we return the sum and hacker rank outputs the result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
