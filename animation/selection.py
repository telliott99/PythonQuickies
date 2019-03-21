import sys, helper
    
def selection_sort(L):
    # low value starting at pos
    def low_index(start=0):
        v = min(L[start:])
        return L.index(v)
    target = sorted(L)
    i = 0
    while L != target:
        j = low_index(start=i)
        yield (i,j,L)
        # swap
        L[i],L[j] = L[j],L[i]
        i += 1

if __name__ == "__main__":
    N = int(sys.argv[1])
    L = helper.initialize(N)
    for i,j,L in selection_sort(L):
        fn = helper.barplot(L,markers=[i,j])
        helper.plt.close()
    fn = helper.barplot(L,markers=[i,j])
    print(fn)
