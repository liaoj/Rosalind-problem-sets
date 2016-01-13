def lexf(s, n):
    s_list = s.split(" ")
    res = []
    if n == 1:
        res = s_list
    else:
        for i in range(len(lexf(s, n-1))):
            for j in range(len(s_list)):
                res.append(lexf(s, n-1)[i] + s_list[j])
    return res

        
    
s = "S Y F J"
for elem in lexf(s,4):
    print elem