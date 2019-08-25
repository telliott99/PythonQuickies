import sys
input = sys.argv[1].strip()
tL = list(input)
n = len(tL)
print ''.join(tL)

fn = '/usr/share/dict/words'
with open(fn,'r') as fh:
    data = fh.read()

L = data.strip().split('\n')
L = [w.lower() for w in L]
L = [w for w in L if len(w) == n]

#------------

for i,token in enumerate(tL):
    if token == '-':
        continue
    sL = list()
    for w in L:
        if w[i] == token:
            sL.append(w)
    L = sL[:]

for i,w in enumerate(L):
    if i and not i % 5:  print
    print w,
print


    

