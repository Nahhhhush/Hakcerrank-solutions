#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    length = len(arr)
    min_sum = 0
    max_sum = 0
    j = length-1 
    arr.sort()
    
    for i in range(length-1):
        min_sum += arr[i]
        
        max_sum += arr[j]
        j -= 1
    print(min_sum ,max_sum)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
