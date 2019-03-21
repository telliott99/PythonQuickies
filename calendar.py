# strategy:  build a list of day 
# for Jan 1 by year as one of 0..6

D = {0: 'Sun', 1: 'Mon', 
     2: 'Tue', 3: 'Wed',
	 4: 'Thu', 5: 'Fri', 
	 6: 'Sat' }

def isJulianLeapYear(year):
	if year % 4 == 0:
		return True
	return False	
    	
def isLeapYear(year, transition_year = 1752):
	if year <= transition_year:
		return isJulianLeapYear(year)
	if year % 400 == 0:  return True
	if year % 100 == 0:  return False
	return isJulianLeapYear(year)

daysIn1752 = 366 - 11 # Sep 2 jumps to Sep 14
jan1year1 = 6 # Sat
L = [False, jan1year1]

N = 2500
# build the list
for y in range(1,N+1):
	jan1 = L[-1]
	if y == 1752:
		next_jan1 = jan1 + daysIn1752
	else:
		if isLeapYear(y):
		    next_jan1 = (jan1 + 2)
		else:
			next_jan1 = (jan1 + 1)
	L.append(next_jan1 % 7)

def dayForJan1(year):
	n = L[year]
	return D[n]

def test():
	pL = [1600,1700,2000]
	for y in pL:
		print dayForJan1(y)

# test()

# part 2:  get the day of the week for any date

months = ['Jan','Feb','Mar','Apr',
          'May','Jun','Jul','Aug',
          'Sep','Oct','Nov','Dec']

sL = [31,28,31,30,31,30,
      31,31,30,31,30,31]

def dayFor(date,month,year):
	count = date - 1
	n = months.index(month)
	for i in range(n):
	    count += sL[i]
	if n > 1 and isLeapYear(year):
		count += 1
	count += L[year]
	day = count % 7
	return D[day]

def dayForDateMonthYear(date,month,year):
	if year != 1752:
		return dayFor(date,month,year)
	n = months.index(month)
	# if month is not Sep
	if n < 8:
		return dayFor(date,month,year)
	if n > 8:
		return dayFor(date,month,year) - 11
	# by date in Sep
	if date <= 2:
		return dayFor(date,month,year)
	if date >= 14:
		return dayFor(date,month,year) - 11
	print "invalid date", date, month, year
	assert False
	
def test2():
	print dayForDateMonthYear(24,'Oct',1955)
	print dayForDateMonthYear(4,'Jul',1776)
	print dayForDateMonthYear(4,'Apr',1865)
	print dayForDateMonthYear(2,'Sep',1752)
	print dayForDateMonthYear(4,'Sep',1752)

test2()
