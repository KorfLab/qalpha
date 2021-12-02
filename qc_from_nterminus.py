#!/usr/bin/python3 

import argparse
import gzip
import json
import os
import sys

import numpy as np
from Bio.PDB import MMCIF2Dict

parser = argparse.ArgumentParser(description=''.join(
	('generate targets for poor gene quality from alphafold models')))
parser.add_argument('--pdbs', required=True, type=str,
	metavar='<path>', help='path to directory with all the models')
parser.add_argument('--window', required=True, type=int,
	metavar='<int>', help='number of residues from N-terminus to take')
parser.add_argument('--threshold', required=True, type=float,
	metavar='<float>', help='cutoff for possible hits')
parser.add_argument('--glob', required=True, type=float,
        metavar='<float>', help='cutoff for global')
arg = parser.parse_args()

for file in os.listdir(arg.pdbs):
	if 'AF-' not in file: continue
	if file.endswith('.cif.gz'):
		ids = file.split('-')
		afold_id = ids[1]
		
		cif_file = os.path.join(arg.pdbs, file)
		
		with gzip.open(cif_file, 'rt') as fp:
			cif_dic = MMCIF2Dict.MMCIF2Dict(fp)
		fp.close()
		
		if '_af_target_ref_db_details.gene' not in cif_dic: continue
		
		gene_id = cif_dic['_af_target_ref_db_details.gene'][0]
		
		 

		seq = cif_dic['_atom_site.label_comp_id']
		ind = cif_dic['_atom_site.label_seq_id']
		qas = cif_dic['_atom_site.B_iso_or_equiv']
		glob = cif_dic['_ma_qa_metric_global.metric_value']
		

		scores = dict()
		for aa, id, score in zip(seq, ind, qas):    
			if id not in scores: scores[int(id)] = (aa, float(score))
		
		n_term_scores = []
		for pos in sorted(scores):
			if pos <= arg.window:
				n_term_scores.append(scores[pos][1])
			else: break
		
		assert(len(n_term_scores) == arg.window)
		avg_score = np.mean(np.array(n_term_scores))
		data = dict()
		glob_float = float(glob[0]) #GLOBAL FILTRATION
		if glob_float > float(arg.glob): continue #less than or less than/equal to?

		if (avg_score < float(arg.threshold)): #LOCAL FILTRATION. less than or less than/equal to?
			data[afold_id] = {}
			data[afold_id]["WORMBASE:"] = gene_id
			data[afold_id]["GLOBAL SCORE:"] = glob_float
			data[afold_id]["LOCAL SCORE"] = avg_score
			print(data)

file_path = 'processing_out.txt'
sys.stdout = open(file_path, "w")
print(data)