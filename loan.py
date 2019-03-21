initial_balance = 250000
interest = 4.25   # percent
monthly_rate = interest/1200.0
term = 360        # months
inflation = 3.0   # percent
monthly_inflation_rate = inflation/1200.0

def show(month,base,extra,current,total):
    print (str(month) + ' payments of').ljust(15),
    print ('%3.2f' % (base + extra)).rjust(10)
    print ('final payoff:').ljust(15),
    print ('%3.2f' % current).rjust(10)
    print ('total cost:').ljust(15),
    print('%3.2f' % total).rjust(10)
    print

def test(base,extra=0,with_inflation=True):
    month = 0
    current = initial_balance
    total = 0
    inflation_multiplier = 1.0
    
    while current - base - extra > 0:
        month += 1
        inflation_multiplier *= (1.0 / (1.0 + monthly_inflation_rate))
        interest = monthly_rate * current
        current -= base - interest + extra
        cost = base
        if with_inflation:  
            cost *= inflation_multiplier
        total += cost
        
    total += current
    show(month,base,extra,current,total)
        
base = 1229.84
for extra in [0,100]:
    print 'with inflation'
    test(base,extra)
    print 'no inflation'
    test(base,extra,with_inflation=False)
    
    
# http://inflationdata.com/inflation/inflation_rate/CurrentInflation.asp