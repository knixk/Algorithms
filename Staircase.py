#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1, n+1):               #using the range function to iterate.
        s = "#" * i                       #We multiply a "#" everytime we iterate by i which is 1 here.
        print(s.rjust(n))                 #We use a special method in python called rjust, it gives us the functionality of adding padding and aligning it in the right.

if __name__ == '__main__':
    n = int(input())

    staircase(n)
