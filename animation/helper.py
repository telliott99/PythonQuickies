import time, random
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

random.seed(int(time.time()))
count = 0

def initialize(N):
    iL = range(1,N+1)
    L = list()
    while iL:
        index = random.choice(range(len(iL)))
        L.append(iL.pop(index))
    return L   

#--------------------------------------

def do(markers):
    i,j = markers
    plt.scatter(i, -0.5,   color='b', marker='o')
    plt.scatter(i+1, -0.5, color='r', marker='o')
    plt.scatter(j, -0.5,   color='r', marker='o')
  
def barplot(L,markers=[]):
    global count
    count += 1
    plt.figure()
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.yaxis.set_major_locator(
        MaxNLocator(integer=True))

    R = range(len(L))
    plt.bar(R, L, color= 'salmon')
    if markers:
        do(markers)
    
    s = str(count)
    if len(s) == 1:
        s = '0' + s
    fn = 'tmp/' + s + '.png'
    plt.savefig(fn)
    return fn

def show(vL):
    pL = [str(i).rjust(2) for i in vL]
    #print ' '.join(pL)
    # can't do this anymore since I'm
    # capturing output in the shell

