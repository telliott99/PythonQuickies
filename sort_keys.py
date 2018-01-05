from operator import itemgetter

L = [ {'name':'fwd',  'a':1, 'b':2, 'c':3},
      {'name':'rev',  'a':3, 'b':2, 'c':1},
      {'name':'perm', 'a':2, 'b':3, 'c':1} ]
      
L2 = [[1,5,3],[4,2,6]]

def f(e):
    return e['c']

def report(L):
    print ' '.join([e['name'][0] for e in L])

report(L)
L.sort()
report(L)
L.sort(key=f,reverse=True)
report(L)
L.sort(key=lambda e: e['b'])
report(L)

print L2
L2.sort(key=itemgetter(1),)
print L2