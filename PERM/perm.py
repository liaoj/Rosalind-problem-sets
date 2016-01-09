def perm(n):
    if n == 1:
        return 1
    if n > 1:
        res = n*perm(n-1)
        return res


"""
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 


"""

def permutate(ls):
    if (len(ls) == 1) :
        return [ls]
    result = []
    for i in range(len(ls)):
        elem = ls[i]
        remaining = ls[:i] + ls[i+1:]
        p = permutate(remaining)
        for e in p:
            e = [elem] + e
            result.append(e)  
    return result
n = 6
ls = []
i = 1
while 1 <= i <=n:
    ls.append(i)
    i = i +1
# print ls
res = permutate(ls)
print len(permutate(ls))
for element in res:
    for e in element:
        print e,
    print 


"""
permutate([1]) => [[1]]
permutate([1, 2]) => [[1, 2], [2, 1]]
permutate([3, 4]) => [[3, 4], [4, 3]]
permutate([1, 2, 3]) => ...
"""