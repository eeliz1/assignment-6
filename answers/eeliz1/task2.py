#!/usr/bin/env python
# encoding: utf-8

'''
Calculates the sum of the integers 0 to 1000 via recursion
'''
import sys
sys.setrecursionlimit(1100)

def recursion_sum(x):
    if x == 1000:
        return x
    else:
        return (x + recursion_sum(x+1))

def main():
    answer = recursion_sum(0)
    print(answer)

if __name__ ==  '__main__':
    main()