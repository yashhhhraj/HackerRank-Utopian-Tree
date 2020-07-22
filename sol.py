#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return (utopianTree(n - 2) * 2) + 1
    else:
        return (utopianTree(n - 2) + 1) * 2




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        print(utopianTree(n))

        
