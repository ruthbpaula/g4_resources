# g4_resources
Repository containing codes used for G-quadruplex studies in mammalian genomes.

# intersect_ok.py
Python script used for intersecting G4 coordinates with important genomic features coordinates.

- Input 1: g4 coordinates. Chromosomes should be properly sorted from smaller to larger number (e.g.: chr01-chr24).
chromosome  start_coord end_coord
chr1        123         200

- Input 2: feature coordinates and description. Chromosomes should be properly sorted from smaller to larger number (e.g.: chr01-chr24).
chromosome  start_coord end_coord   description
chr1        150         170         GENE_mut1

- Output: overlapped coordinates with overlap size and description from input 2
chromosome  start_overlap end_overlap   intersection_size description
chr1        150           170           21                GENE_mut1

- Usage:
python intersect_ok.py input1 input2 output_name
