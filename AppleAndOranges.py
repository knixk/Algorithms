#Solution in java

s, t = input().strip().split(' ')
s, t = [int(s),int(t)]
a, b = input().strip(.split(' '))
a, b = [int(a), int(b)]
#print(a)
#print(b)
m, n = input().split().split(' ')
m, n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
countA = 0;
countO = 0;

for in apple:
    if(i + a >= s and i + a <= t):
        countA += 1
    
for j in orange:
    if(j + b >= s and j + b <= t):
        countO += 1

print(countA)
print(countO)


#-----------------------------------------------------------------------------------------------------------------------------

#solution 2 in Python

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    closeapples, closeoranges = 0, 0
    for d in apples:                                    #traversing the array 
        if d+a>=s and d+a<=t:                           #checking if if lies in the range s and t
            closeapples+= 1                             #if it does so we add 1
    for d in oranges:   
        if d+b>=s and d+b<=t:
            closeoranges+= 1
    
    print(closeapples)                                  #printing the results            
    print(closeoranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
