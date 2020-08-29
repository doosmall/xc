#!/usr/bin/env python
# encoding: utf-8

fd = open("/Users/didi/work-xc/pedigree_LZF.csv", "r")
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


def level( root ):
    if d.has_key(root):
        p1, p2 = d[root]
        if p1+p2 == 0:
            return 1
        else:
            return max(level(p1), level(p2))+1

for x in range(1, 19690):
    print x, level(x)
    
