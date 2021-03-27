#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    # Complete this function
    positive = sum(x > 0 for x in arr)/len(arr)         #Fairly simple problem, we iterate through the arr and if x > 0 we store it in variable.  
    negative = sum(x < 0 for x in arr)/len(arr)         #then we use the sum function and divide by the arr
    zero = sum(x == 0 for x in arr)/len(arr)
    
    print(positive, negative, zero, sep="\n")           #We print the answer by using a parameter known as sep and next line
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
