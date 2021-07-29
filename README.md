# phypy

## Installation
To install, clone or download and decompress the zip file of this repo. Go to the `phypy` directory, then install by typing

```pip install .```

To learn the usage of any script, use the `-h` option 

```python <script_name> -h```

## Scripts for FASTA files
**sample_sequences.py**: randomly sample a subset of sequences (i.e. species) from an input FASTA file. 

E.g. to randomly sample out 10 sequences from the alignment `test_data/sequences.fasta` and output to `sampled.fasta`, run the following command:

```python sample_sequences.py -i test_data/sequences.fasta -o sampled.fasta -s 10```

**select_sequences.py**: select out the specified set of sequences. 

E.g. to sample out the 2 sequences "SB" and "SBA" from `test_data/sequences.fasta` and output to `SB_SBA.fasta`, run

```python select_sequences.py -i test_data/sequences.fasta -o SB_SBA.fasta -l "SB SBA"```

## Scripts for NEWICK files
**prune_tree.py**: prune out a set of taxa from a Newick tree. Can be used with `-v` to retain the listed taxa instead.

E.g. to prune out the two taxa "SB" and "SBA" from the tree `test_data/tree.nwk` and output to `pruned.nwk`, run 

```python prune_tree.py -i test_data/tree.nwk -o pruned.nwk -l "SB SBA"```
