#!/usr/bin/python
from fractions import Fraction
from decimal import Decimal
import math

def entropy( c, pl):
	x = 0
	for item in pl:
		x += item * math.log(item)
	x *= -c
	return x

def num_seq_tip( c, n, pl ):
	x = entropy( c, pl )
	y = 2**(n*x)
	return y

def p_seq_tip( c, n, pl ):
	x = entropy( c, pl )
	y = 2** ( -1*(n*x))
	return y

pl = [0.5, 0.5]
n = 1
c = 1/math.log(2)
print entropy( c, pl )
print num_seq_tip( c, n, pl )
print p_seq_tip(c, n, pl)
