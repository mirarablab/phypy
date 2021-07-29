#! /usr/bin/env python

from phylib.sequence_lib import sample_from_list
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i","--input",required=True,help="Input file (FASTA)")
parser.add_argument("-o","--output",required=True,help="Output file (FASTA")
parser.add_argument("-l","--listing",required=True,help="Selected set")

args = vars(parser.parse_args())

infile = args["input"]
outfile = args["output"]
taxalist = args["listing"].split()

print(taxalist)

sample_from_list(infile,taxalist,outfile)
