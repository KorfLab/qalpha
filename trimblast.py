
import sys

from korflib import parse_ab_blast_mformat as readblast

MIN_PCT = 40
MIN_LEN = 200


for qid, sid, qbeg, qend, sbeg, send, score, pct in readblast(sys.argv[1]):
	if qid == sid: continue
	if pct < MIN_PCT: continue
	if qend - qbeg < MIN_LEN: continue
	if send - sbeg < MIN_LEN: continue
	print(qid, sid, qbeg, qend, sbeg, send, score, pct)
