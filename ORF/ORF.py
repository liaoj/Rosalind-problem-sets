
        
def rev_comp(seq):
    rev_seq = seq[::-1]
    res_seq = ''
    for e in rev_seq:
        if e == "A":
            res_seq += "T"
        if e == "T":
            res_seq += "A"
        if e == "C":
            res_seq += "G"
        if e == "G":
            res_seq += "C"
    return res_seq
    
    
def find_cod_str(seq):
    cod_strs= []

    for i in range(len(seq)-3):
        if seq[i:i+3] == 'ATG':
            new_seq = seq[i:]
            j = 0
            cod_str = ""
            while j < len(new_seq)-3:
                if new_seq[j:j+3] in ("TAA", "TAG", "TGA"):
                    cod_str = new_seq[:j]
                    cod_strs.append(cod_str)
                    break
                else:
                    j += 3
    return cod_strs

def trans(codingString):
    i = 0
    aa_seq = ""

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
    
    while i <= len(codingString) - 3:
        aa_seq += codontable[codingString[i:i+3]]
        i = i + 3
    if aa_seq:
        return aa_seq

# seq = "ATGATG"
# print trans(seq)

f = open("/Users/liaozhengli/Rosalind/ORF/rosalind_orf.txt", "r")
lines = f.readlines()
# print lines
seq = ''
seqs = []
for line in lines:
    if line[0]!= ">":
        line = line.strip()
        seq += line
seqs = [seq, rev_comp(seq)]

all_cod_seq = []
for seq in seqs:
    cod_strs = find_cod_str(seq)
    all_cod_seq += cod_strs
trans_seq = [all_cod_seq[0]]
for seq in all_cod_seq:
    if seq not in trans_seq:
        trans_seq += [seq]
for seq in trans_seq:
    print trans(seq)    
    
    
    
   

    