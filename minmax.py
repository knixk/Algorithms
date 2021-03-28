#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()                                #we used the sort method on the array.
    x = sum(arr)                              #then we used the max function and min function to find the respective values.
    minval = x - max(arr) 
    maxval = x - min(arr)
    print(minval, maxval)                     #we print the result
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
