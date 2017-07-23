#### Python chunks

Despite [this](https://stackoverflow.com/questions/2095637/python-arguments-for-using-itertools-to-split-a-list-into-groups) advice from StackOverflow, I still prefer to break up strings and lists into chunks by hand.

```python
>>> s = 'abcdef'
>>> n = 2
>>> R = range(0,len(s),n)
>>> R
[0, 2, 4]
>>> rL = [s[i:i+n] for i in R]
>>> rL
['ab', 'cd', 'ef']
>>>
```

#### Official way

``` python
from itertools import izip_longest

def groupby_itertools(iterable, n=3, padvalue='x'):
    "groupby_itertools('abcde', 3, 'x') --> ('a','b','c'), ('d','e','x')"
    return izip_longest(*[iter(iterable)]*n, fillvalue=padvalue)
```


