#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0                   
    bob = 0
    for i in range(3):              #we cycle through i in range 3
        if a[i] > b[i]:             #then we compare if index of a is greater than of b
            alice += 1              #if so we add one to alice
        elif b[i] > a[i]:           #we repeat the opposite process for bob
            bob += 1        
    li = [alice, bob]               
    return li                       #we return the array as li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
