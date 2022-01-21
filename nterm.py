import os
import sys

for genome in os.listdir(sys.argv[1]):
	print(f'{sys.argv[1]}/{genome}')
	ma = []
	with open(f'{sys.argv[1]}/{genome}') as fp:
		for line in fp.readlines():
			if not line.startswith('>'):
				ma.append(line.rstrip())
	slen = len(ma[0])
	for seq in ma: print(seq[:120])
	print()


