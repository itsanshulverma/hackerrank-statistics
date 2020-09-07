#!/bin/python3


# Mean, Median and Mode
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem


# Author: Anshul Verma

def mean(N):
	return sum(N)/len(N)

def median(N):
	N = sorted(N)
	if len(N)%2 == 0:
		mid = int(len(N)/2)
		return (N[mid-1]+N[mid])/2
	else:
		mid = int(len(N)+1/2)
		return N[mid-1]
	
def mode(N):
	N = sorted(N)
	counts = dict()
	for el in N:
		counts[el] = counts.get(el, 0) + 1
	maxCount = None
	mode_el = None
	for el, count in counts.items():
		if maxCount is None or count>maxCount:
			maxCount = count
			mode_el = el
	return mode_el
	
if __name__ == '__main__':  
	
	N = []
	X = int(input())
	
	lst = input().strip().split()
	
	for i in range(X):
		N.append(int(lst[i]))
           
	res_mean = mean(N)
	res_median = median(N)
	res_mode = mode(N)
	
	print(res_mean)
	print(res_median)
	print(res_mode)

