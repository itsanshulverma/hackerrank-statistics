#!/bin/python3


# Weighted Mean
# https://www.hackerrank.com/challenges/s10-weighted-mean/problem


# Author: Anshul Verma

def w_mean(N, W):
	_sum = 0
	for i in range(len(N)):
		_sum = _sum + N[i]*W[i]
	return _sum/sum(W)
	
if __name__ == '__main__':  
	
	N = []
	W = []
	X = int(input())
	
	lst = input().strip().split()
	for i in range(X):
		N.append(int(lst[i]))
		
	lst = input().strip().split()
	for i in range(X):
		W.append(int(lst[i]))
           
	result = w_mean(N, W)
	
	print(round(result, 1))

