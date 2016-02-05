#!/usr/bin/env python
# encoding: utf-8

'''
Calculates e via recursion with user input
'''

import sys
import math
sys.setrecursionlimit(1100)

##defining y as a global variable, despite advice about global variables##
y = int(input("To what factorial should e be calculated: "))

##defining recursion function to run until x counts up from 0 to y##
def recursion_e(x):
	if x == y:
		return 0
	else:
		return ((1/math.factorial(x)) + recursion_e(x+1))

##defining main function to print output from recursion_e##
def main():
	x = 0
	answer = recursion_e(x)
	print(answer)

if __name__ ==  '__main__':
    main()