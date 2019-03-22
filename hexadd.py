#! /usr/bin/python
import sys

if len(sys.argv) < 3:
    print "Usage: hexadd n1 n2 [n3 ..]"
    print "0x leader is optional"
    sys.exit(0)

L = sys.argv[1:]

#------------------------

x = '0x'
L2 = list()
for e in L:
    if not e[:2] == x:
        L2.append(x + e)
    else:
        L2.append(e)
L = L2[:]

#------------------------

def add(L):
    n = 0
    for e in L:
        n += int(e, base=16)
    return hex(n)
    
try:
    h = add(L)
except:
    print "Error: not hex values?"
    sys.exit(1)

#------------------------

def show(L,h):
    c = len(h) - 1
    for e in L:
        print '0x' + e[2:].rjust(c)
    print '  ' + ('-'*c).rjust(c)
    print '0x' + h[2:].rjust(c)

show(L,h)