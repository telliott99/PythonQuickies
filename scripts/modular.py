def add_mod(i,j,p):
    if i >= p or j >= p:
        raise ValueError
    r = i + j
    if r >= p:
        r -= p
    return r

def test1():
    print add_mod(13,57,101)
    #print add_mod(102,57,101)

#test1()

def test_digits(i,j):
    left = bin(i)[2:].count('1')
    return left >= bin(j)[2:].count('1')

def multiply_mod(i,j,p):
    if test_digits(i,j):
       i,j = j,i
    n = i
    r = 0
    while j > 0:
        if j & 1:
            r = r + n
            while r >= p:
                r -= p
        # prepare for next round
        j = j >> 1  # right shift j
        n = n + n   # double n
        while n >= p:
            #print 'mul sub p'
            n -= p
    return r

def test2():
    print multiply_mod(13,19,23)
    print multiply_mod(123,456,101)

#test2()

def eea(i, j):
    assert(isinstance(i, int))
    assert(isinstance(j, int))
    (s, t, u, v) = (1, 0, 0, 1)
    while j != 0:
        (q, r) = (i // j, i % j)
        (unew, vnew) = (s, t)
        s = u - (q * s)
        t = v - (q * t)
        (i, j) = (j, r)
        (u, v) = (unew, vnew)
    (d, m, n) = (i, u, v)
    return (d, m, n)

def test3():
    print eea(7,121)                # (1, -3, 52)
    print multiply_mod(7,52,121)    # 1
    print eea(52,121)

# test3()

def exponentiate_mod(i,j,p):
    if test_digits(i,j):
       i,j = j,i
    n = i
    r = 1
    while j > 0:
        if j & 1:
            print '& sub p'
            r = multiply_mod(r,n,p)
            while r >= p:
                r -= p
        # prepare for next round
        j = j >> 1              # right shift j
        n = multiply_mod(n,n,p)   # square n
        while n >= p:
            print 'exp sub p'
            n -= p
    return r

def test4():
    print exponentiate_mod(13,57,101)
    print exponentiate_mod(2,40,101)
    print exponentiate_mod(314159265359,271828182846,2**127-1)

test4()