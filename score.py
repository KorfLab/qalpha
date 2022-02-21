#!/usr/bin/python3 

import argparse
import gzip
import json
import os
import sys

import numpy as np
from Bio.PDB import MMCIF2Dict

# 1) Make a good way to eliminate shit data
# 2) Find mean and standard deviation to pinpoint shit alignments 
# 3) Find Gene Sequences 

for genome in os.listdir(sys.argv[1]):
	# parser = argparse.ArgumentParser(description=''.join(('generate targets for poor gene quality from alphafold models')))
	# parser.add_argument('--threshold', required=True, type=int, metavar='<int>', help='number of residues from N-terminus to take')
	# arg = parser.parse_args()

	print(f'{sys.argv[1]}/{genome}')
	ma = [] #poor N termini matrix
	with open(f'{sys.argv[1]}/{genome}') as fp:
		for line in fp.readlines():
			if not line.startswith('>'):
				if line.startswith('-'* int(sys.argv[2])): #setting an N-termini threshold, how to better find poor N-termini
					ma.append(line.rstrip())
			elif line.startswith('>'):
				a = line.lstrip()
				a = a[1:len(a)-2]
				ma.append('gene_ID: '+ a)

	print(ma)
	#print(k)
	# for i in ma:
	# 	if 
	# print()


	# slen = len(ma[0])
	# for seq in ma: print(seq[:120])
    


