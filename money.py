# find (distinct) integer values
# for letters so that:
'''
  S E N D
+ M O R E
--------
M O N E Y

clearly M = 1
then    1 + S = 10
        O = 0
and     S = 9
now we have only 5 values

further, since E + O = N and O = 0
there is a carry from N + R operation
and E = N - 1
'''

from itertools import permutations
L = [2,3,4,5,6,7,8]

def add(x,y,carry):
    z = x + y + carry
    if z > 9:
        return 1, z % 10
    return 0, z

def test(L):
    D,E,N,R,Y = L
    if not E == (N-1):  
        return False
    carry, result = add(D,E,0)
    if result != Y:  
        return False
    carry, result = add(N,R,carry)
    if result != E:  
        return False
    if not carry:  
        return False
    return True

P = permutations(L,5)
for p in P:
    if test(p):
        print p
        break

'''
prints:

('7', '5', '6', '8', '2')
  D    E    N    R    Y

  9 5 6 7
  1 0 8 5
  -------
1 0 6 5 2
'''
    
    

