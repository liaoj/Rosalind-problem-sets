# import sys
#
# for line in sys.stdin:
#     line = line.strip()

f = open("/Users/liaozhengli/Rosalind/MRNA/rosalind_mrna.txt", "r")
lines = f.readlines()
line = ""
for e in lines:
    line += e.strip()
line += "_"

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
        
protein_rna_dict = {}
for key, value in codontable.iteritems():
    if value not in protein_rna_dict.keys():
        protein_rna_dict[value] = 1
    else:
        protein_rna_dict[value] += 1
print protein_rna_dict

tot_num = 1
mrna_num = 0
for e in line:
    mrna_num = protein_rna_dict[e]
    tot_num *= mrna_num
    tot_num = tot_num % 1000000
print tot_num 

