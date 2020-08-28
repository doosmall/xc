

fd = open("/Users/didi/work-xc/pedigree_LZF(1).csv", "r")
d = {}
for line in fd:
    p1, p2 , p3 = line.lstrip().rstrip().split(',')
    try:
        p1 = int(p1)
    except :
        p1 = 0 

    try:
        p2 = int(p2)
    except :
        p2 = 0

    try:
        p3 = int(p3)
    except :
        p3 = 0

    d[p1] = (p2, p3)

#for k, v in d.items():
#    print k, v

paths = []
def dfs(frm, to, path):
    if frm == 0:
        return
    path.append(frm)
    if d.has_key(frm):
        p1, p2 = d[frm]
        #print "--> ",frm, p1, p2
        if p1 == to:
            path.append(p1)
            paths.append(list(path))
        if p2 == to:
            path.append(p2)
            paths.append(list(path))
        
        dfs(p1, to, list(path))
        dfs(p2, to, list(path))



def get_factor(p):
    p1, p2 = d[p]
    if p1 == 0 or p2 == 0:
        return 1.0
    return 0.5

for i in range(1, 19690):
    for j in range(1, 19690):
        paths = []
        dfs(i, j, [])
        pp = 0.0
        for path in paths:
            cp = 1.0
            for p in path[:-1]:
                cp = cp * get_factor(p)
            pp += cp
        if pp <= 0:
            continue
        print i,'\t', j, '\t',  pp


