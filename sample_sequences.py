#! /usr/bin/env python

# usage: sampling.py <file_in> <file_out> <sample_size>

import sys
from os.path import isfile
import random
from phylib import sequence_lib

try:
	import cPickle as pickle
except:
	import pickle

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i","--input",required=True,help="Input file (FASTA)")
parser.add_argument("-o","--output",required=True,help="Output file (FASTA")
parser.add_argument("-s","--samplesize",required=True,type=int,help="Sample size")

args = vars(parser.parse_args())

file_in = args["input"]
file_out = args["output"]
sample_size = args["samplesize"]

f = open(file_in,'r')
file_idx = file_in.split('.fasta')[0]+'.idx'
if not isfile(file_idx):
	sequence_lib.index_fasta(file_in,file_idx)
f_idx = open(file_idx,'rb')
seqs = pickle.load(f_idx)
f_idx.close()

seq_pointers = list(seqs.values())
samples = random.sample(seq_pointers,sample_size)

f_out = open(file_out,'w')

for s in samples:
    f.seek(s)
    seq = f.readline()
    f_out.write(seq)
    L = f.readline()
    while L[0] != '>':
        f_out.write(L.rstrip())
        L = f.readline()
        if not L:
            break
    f_out.write('\n')

f.close()
f_out.close()
