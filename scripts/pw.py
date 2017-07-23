''' 
note:  uses SystemRandom

examples:
> python pw.py dg 10
0790550936
> python pw.py all
Qx3yZtZCfzSyCA*zsEdapnk0VERhT4
> python pw.py
ymgueebennqkgdzmtcprrefvttctpv
> python pw.py 50
ftpxcbwimexjwnezcetjibekzeqfnmufhlguilsxplystkagsh
>
''' 

import sys, string

dg = string.digits 
lt = string.letters
lc = string.lowercase
uc = string.uppercase
all = lt + dg + '$#&*_'
D = {'dg':dg, 'lt':lt, 'lc':lc,
     'uc':uc, 'all':all}

N = 30
aL = list()
for arg in sys.argv[1:]:
    try:
        N = int(arg)
    except:
        aL.append(arg)

cL = list()
if len(aL) == 0:
    cL = lc
else:
    for arg in aL:
        try:
            cL += D[arg]
        except:
            pass

# ----------------------------

from random import SystemRandom
f = SystemRandom().randrange

iL = [f(len(cL)) for i in range(N)]
L = [cL[j] for j in iL]
print ''.join(L)


