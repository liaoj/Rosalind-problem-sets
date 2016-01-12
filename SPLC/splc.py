def read_fasta(filename):
    f = open(filename, "r")
    text = f.readlines()
    index_list = []
    linked_list = []
    for i in range(len(text)):
        text[i]= text[i].strip()
        if text[i][0] =='>':
            index_list.append(i)
    # print index_list
    for n in range(len(index_list)-1):
        seq_list = text[index_list[n] + 1: index_list[n+1]]
        seq_string = "".join(seq_list)
        linked_list.append(seq_string)
    linked_list.append("".join(text[index_list[-1]+1:]))
    #print linked_list
    return linked_list
                  

def exon_str(linked_list):
    seq = linked_list[0]
    #print seq
    for line in linked_list[1:]:
            tmp = seq.find(line)
            if tmp != -1:
                seq = seq[:tmp] + seq[tmp + len(line):]
    return seq



def find_cod_str(seq):
    cod_strs= []
    i = 0
    while i <= len(seq)-3:
        if seq[i:i+3] == 'ATG':
            new_seq = seq[i:]
            j = 0
            cod_str = ""
            while j <= len(new_seq)-3:
                #print new_seq[j:j+3]
                if new_seq[j:j+3] in ("TAA", "TAG", "TGA"):
                    #print j
                    cod_str = new_seq[:j]
                    # print new_seq[:j]
                    cod_strs.append(cod_str)
                    i += j +3
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



filename = "/Users/liaozhengli/Rosalind/SPLC/rosalind_splc.txt"
seq_list =  read_fasta(filename)
exon = exon_str(seq_list)
coding_strs = find_cod_str(exon)
for elem in coding_strs:
    res = trans(elem)
print res



