### Tricks for lists and matrices

#### Reversal

``` python
>>> s = 'abc'
>>> s[::-1]
'cba'
>>>
```

The above is best.  But one could do:

``` python
>>> s = 'abc'
>>> n = len(s)
>>> L=[None]*n
>>> for i in range(n):
...     L[n-i-1] = s[i]
... 
>>> ''.join(L)
'cba'
>>>
```

or

```
>>> s = 'abc'
>>> L =list()
>>> for i in range(len(s)-1,-1,-1):
...     L.append(s[i])
... 
>>> ''.join(L)
'cba'
>>>
```


#### transposition

``` python
>>> m = [(1,2,3),(4,5,6),(7,8,9)]
>>> zip(*m)
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>>
```

