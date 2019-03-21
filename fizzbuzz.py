def test(n):
    s = ''
    if not n % 3:  s += 'Fizz'
    if not n % 5:  s += 'Buzz'
    return s

for i in range(1,16):
    s = test(i)
    if s == '':  
        print str(i)
    else:
        print s

