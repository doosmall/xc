import traceback
fd = open("/Users/didi/work-xc/pedigree_major.csv", "r")
import sys
sys.setrecursionlimit(95000)

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

fnd = 2713
fnd = 9771
paths = []
def dfs(root, path):
    if root == 0:
        return
    path.append(root)
    if d.has_key(root):
        p1, p2 = d[root]
        if p1 in path:
            path.append(p1)
            paths.append(list(path))
            #print path
            return
        if p2 in path:
            path.append(p2)
            #print path
            paths.append(list(path))
            return
        if p1 == 0 and p2 == 0:
            #paths.append(list(path))
            pass
        else:
            dfs(p1, list(path))
            dfs(p2, list(path))
    

for k, v in d.items():
    path = []
    dfs(k, path)

tmp = {}
for path in paths:
    left = path[-1]
    tmp[tuple(path[path.index(left):])] = 0

for k, _ in tmp.items():
    print k




'''
fnd = 2713
fnd = 9771
stack = []
stack.append(fnd)
while( len(stack) > 0 ):
    #print 'stack:', stack
    pp = stack.pop()
    if pp in stack:
        print "res:", pp, stack
        break

    if d.has_key(pp):
        p1, p2 = d[pp]
        print pp, d[pp]
        if p1 != 0:
            stack.append(p1)
        if p2 != 0:
            stack.append(p2)


tmp = []
fnd = 9771
def find(k):
    if d.has_key(k):
        p1, p2 = d[k]
        print k,  d[k]
        if p1 == 0:
            return
        if p2 == 0:
            return
        
        if k in tmp:
            print 'find:',k, tmp 
        
        tmp.append(p1)
        find(p1)
        tmp.pop()

        tmp.append(p2)
        find(p2)
        tmp.pop()



fnd = 9771
tmp.append(fnd)
try:
    find(fnd)
except:
    pass
exit(0)


for k, v in d.items():
    fnd = k
    tmp.append(fnd)
    try:
        find(fnd)
    except:
        print k, v
        pass
    tmp =[]

    '''