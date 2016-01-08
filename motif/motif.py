import requests

def target():
  aa_list = ["A", "R", "N", "D", "B", "C", "E", "Q", "Z", "G", "H", "I", "L", "K", "M", "F", "S", "T", "W", "Y", "V"]
  res = []
  for e in aa_list:
      for letter in aa_list:
          s_tag = ""
          t_tag = ""
          s_tag += "N"+ e + "S" + letter
          t_tag += "N"+ e + "T" + letter
          res += [s_tag, t_tag]
  return res

def find_substr(text, target):
  i = 0
  res = []
  while i < len(text):
      new_text = text[i:i+len(target)]
      if new_text == target:
          res.append(i)
      i = i + 1
  return res   

tar = target()
#print target
f = open("/Users/liaozhengli/Rosalind/motif/input.txt", "r")
ids = f.readlines()
for id in ids:
    id = id.strip()
    r = requests.get("http://www.uniprot.org/uniprot/" + id + ".fasta")
    fasta = r.text.split("\n")
    body = ""
    for line in fasta:
        line = line.strip()
        if len(line) != 0 and line[0] != ">":
            body += line
    res = []
    for t in tar:
        s = find_substr(body, t)
        if s:
            res += s
    if res != []:
        print id
        for i in sorted(res):
            print i+1,
        print
    
            
    
    
    
  
        
    
    # for line in r.text:
#         print line 
    #print r.text
