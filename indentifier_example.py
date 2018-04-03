def perm(l):
    #  Compute the list of all permutation of l
    if len(l) <= 1:
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i+i:]
        p = perm(s)
        for x in p:
            r.append(l[i:i+1] + x)
        return r
