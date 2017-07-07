# Wed Sep 2 jump to Thu Sep 14 (England)
# Julian -> Gregorian transition
daysIn1752 = 366 - 11

def isLeapYear(year):
    if year > 1752:
        if year % 400 == 0:  return True
        if year % 100 == 0:  return False
    return year % 4 == 0

# 0..7 -> day of week
D = {0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed',
     4: 'Thu', 5: 'Fri', 6: 'Sat' }

# build a list of the day of week for Jan 1 
# by year
#  Jan 1 Year 1 AD was Saturday
L = [False, 6] 

# build the list
for year in range(1,2500):
    lastjan1 = L[-1]
    if year == 1752:
        n = lastjan1 + daysIn1752
    else:
        if isLeapYear(year):
            n = (lastjan1 + 2)
        else:
            n = (lastjan1 + 1)
    nextjan1 = n % 7
    L.append(nextjan1)

def newYearsDay(year):
    n = L[year]
    return D[n]

# ---------------------------------------------
# part 2:  find the day of the week for any date

months = ['Jan','Feb','Mar','Apr',
          'May','Jun','Jul','Aug',
          'Sep','Oct','Nov','Dec']

sL = [31,28,31,30,31,30,
      31,31,30,31,30,31]
      
class Date:
    def __init__(self,d,m,y):
        self.date = d
        self.month = m
        self.year = y
    def __repr__(self):
        s = str(self.date).rjust(2) 
        s += ' ' + self.month + ' '
        s += str(self.year).rjust(4)
        return s

class InvalidDateError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def daysSinceJan1(date):
    count = date.date - 1
    n = months.index(date.month)
    for i in range(n):
        count += sL[i]
    if n > 1 and isLeapYear(date.year):
        count += 1
    return count

def dayFor(date):
    if date.year == 1752:
        count = handle1752(date)
    else:
        count = daysSinceJan1(date)
    count += L[date.year]
    return D[count % 7]
    
def handle1752(date):
    n = months.index(date.month)
    # if month is not Sep
    count = daysSinceJan1(date)
    if n > 8:
        count -= 11
    # by date in Sep
    if n == 8 and date.date >= 14:
        count -= 11
    if n == 8 and 2 < date.date < 14:
        raise InvalidDateError(date)
    return count
    
def test():
    dL = [Date(1,'Jan',1),
          Date(1,'Jan',1600),
          Date(1,'Jan',1700),
          Date(4,'Jul',1776), 
          Date(4,'Apr',1865),
          Date(24,'Oct',1955),
          Date(1,'Jan',2000),
          Date(14,'Sep',2016),
          Date(2,'Sep',1752), 
          Date(14,'Sep',1752),
          Date(10,'Sep',1752)]
    for date in dL:
        try:
            result = dayFor(date)
            print result, date
        except InvalidDateError as info:
            print 'invalid date', info
test()

'''
> python calendar.py 
Sat  1 Jan    1
Tue  1 Jan 1600
Mon  1 Jan 1700
Thu  4 Jul 1776
Tue  4 Apr 1865
Mon 24 Oct 1955
Sat  1 Jan 2000
Wed 14 Sep 2016
Wed  2 Sep 1752
Thu 14 Sep 1752
invalid date 10 Sep 1752
>
'''
