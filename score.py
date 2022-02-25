#!/usr/bin/python3 

import argparse
import gzip
import json
import os
import sys
import statistics 

import numpy as np
from Bio.PDB import MMCIF2Dict

# 1) Make a good way to eliminate shit data. Threshold seems like good way to eliminate shit data. 
# 2) Find mean and standard deviation to pinpoint shit alignments 
# 3) Find Gene Sequences 
gen = []
for genome in os.listdir(sys.argv[1]):

	#print(f'{sys.argv[1]}/{genome}')
	ma = [] #poor N termini matrix
	with open(f'{sys.argv[1]}/{genome}') as fp:
		for line in fp.readlines():
			if not line.startswith('>'):
				if line.startswith('-'* int(sys.argv[2])): #setting an N-termini threshold, how to better find poor N-termini 
					ma.append(line.rstrip())
	if len(ma) > 3: #try to eliminate shit data
		gen.append(genome)

			# elif line.startswith('>'):
			# 	a = line.lstrip()
			# 	a = a[1:len(a)-2]
			# 	ma.append('gene_ID: '+ a)

	#print(ma)
#print(gen)
twodarray = []
for genome in gen:  
	with open(f'{sys.argv[1]}/{genome}') as fp:
		count = 0
		a = []
		for line in fp.readlines():
			if not line.startswith('>'):
				if line.startswith('-'): 
					for i in line:
						if i == "-":
							count = count + 1
						if i != "-":
							#print(count)
							a.append(count)
							#print(genome,count)
							#print(line)
							count = 0
							break
		#print(genome, a)
		#twodarray.append(a)
		twodarray.append(a)
print(twodarray)
meanarray = []
for i in twodarray:
	meanarray.append(statistics.mean(i))
#print(meanarray)
for i in twodarray:
	count = 0
	u = statistics.mean(i)
	sd = statistics.stdev(i)
	for j in i:
		if j >= u-sd and j <= u+sd: #within a standard deviation
			count = count + 1
	if count != 0 and (len(i)-count)/count >= 0.6: #threshold for good dashes at begin
		print(i, "good one")
	else:
		print(i, "bad one")
		

		#print(count)
		

					
					
					#ma.append(line.rstrip())
		

	#print(k)
	# for i in ma:
	# 	if 
	# print()


	# slen = len(ma[0])
	# for seq in ma: print(seq[:120])