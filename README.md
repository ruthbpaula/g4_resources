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

# pqs_closest_to_gene.py
Python script used for assigning a PQS to a single splice site (SS), comparing distance (previously computed) from different splice sites and choosing the shortest distance.

- Input: PQS coordinates in the format below
strand  gene  ss_chr  ss_coord  pqs_chr pqs_coord distance
p       ABC   chr1    123       chr1    124       +1
p       ABC   chr1    103       chr1    124       +21

- Output: same format as input, but containing one line per pqs coord, based on distance
strand  gene  ss_chr  ss_coord  pqs_chr pqs_coord distance
p       ABC   chr1    123       chr1    124       +1

- Usage:
Replace arg1 with the name of the input file, and run with "python pqs_closest_to_gene.py".
