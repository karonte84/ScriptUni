#!/usr/bin/python
from fractions import Fraction
from decimal import Decimal
from math import factorial
import math

def binomial(n, k):
	if n>k:
		return factorial(n) / (factorial(k)*factorial(n-k))
	else:
		if n==k:
			return 1
		else:
			return 0

def bernoulli_prob( n, k, p ):
	return (p**k)*( (1-p) ** (n-k) )

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

def prob_seq_tip( c, n, pl ):
	x = entropy( c, pl )
	y = 2** ( -1*(n*x))
	return y

def list_1of2powk(k):
	x = []
	for n in range (1,k+1):
		x.append(Fraction(1,2**n))
	return x;
