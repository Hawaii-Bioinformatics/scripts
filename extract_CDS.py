import sys
from Bio import SeqIO

"""
Takes a genbank file and iterates over the features that are listed.
We check the feature type and only handle those that are of the CDS type.
We extract the protien_id, product and the translation and print them in a 
fasta format, in which the protien_id is the sequence id
"""

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print "USAGE: %s <genbank file> [output file name (defaults to stdout)]"%(sys.argv[0])
    sys.exit(0)


# default to stdout
o = sys.stdout
closeout = False
if len(sys.argv) == 3:
    o = open(sys.argv[2], "w")
    closeout = True


for entry in SeqIO.parse(sys.argv[1], "genbank"):
    # iterate the features in the genbank and pull only the CDS types.
    for feat in (e for e in entry.features if e.type == 'CDS') :
        name = feat.qualifiers['protein_id'][0]
        protseq = feat.qualifiers['translation'][0]
        description = feat.qualifiers.get('product', [""])[0]
        # print the name, sequence and description in a fasta format
        print >> o, ">%s %s\n%s"%(name, description, protseq)

if closeout:
    o.close()
