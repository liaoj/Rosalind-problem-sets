import requests

def read_fasta(filename):
    f = open(filename, "r")
    text_list = []
    for sid in f:
        sid = sid.strip()
        r = requests.get("http://www.uniprot.org/uniprot/" + sid + ".fasta")
        text = r.text
        lines = text.split("\n")
        seq = "".join(lines[1:])
        text_list.append((sid, seq))
    return text_list

# N{P}[ST]{P}  
def find_all_pattern(seq):
    res = []
    for i in range(len(seq)-3):
        if seq[i] != "N":
            continue
        if seq[i+1] == "P":
            continue
        if seq[i+2] != "S" and seq[i+2] != "T":
            continue
        if seq[i+3] == "P":
            continue
        res.append(str(i+1))
    return res

filename = "/Users/liaozhengli/Rosalind/motif/rosalind_mprt.txt"
seq_tuple = read_fasta(filename)
for sid, seq in seq_tuple:
    tmp = find_all_pattern(seq)
    if tmp:
        print sid
        print " ".join(tmp)
        

   
            
      


