### Python quickies:  containers

#### Counter

```
>>> from collections import Counter
>>> c = Counter('abracadabra')
>>> c
Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
>>> c.update('ax')
>>> c
Counter({'a': 6, 'b': 2, 'r': 2, 'c': 1, 'd': 1, 'x': 1})
>>> c.most_common()
[('a', 6), ('b', 2), ('r', 2), ('c', 1), ('d', 1), ('x', 1)]
>>> c.most_common()[0]
('a', 6)
>>>
``` 

#### defaultdict

The constructor takes a "callable"

```
>>> from collections import defaultdict
>>> D = defaultdict(list)
>>> D['a']
[]
>>> 
```

A hand-rolled Counter:

```
>>> D = defaultdict(int)
>>> for c in 'mississippi':
...     D[c] += 1
... 
>>> D
defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})
>>> L = D.items()
```

This list ``L`` is of type ``dict_items`` and cannot be sorted.

```
>>> L
dict_items([('m', 1), ('i', 4), ('s', 4), ('p', 2)])
>>>
>>> L = list(D.items())
>>> L
[('m', 1), ('i', 4), ('s', 4), ('p', 2)]
>>> L.sort()
>>> L
[('i', 4), ('m', 1), ('p', 2), ('s', 4)]
>>>
```

To use this as a Counter, we need to sort on the value.  One way is to use a lambda expression for the sort ``key``.

```
>>> L.sort(key=lambda x: x[1])
>>> L
[('m', 1), ('p', 2), ('i', 4), ('s', 4)]
```

The official way to sort on the second item of a tuple:  itemgetter.

```
>>> 
>>> from operator import itemgetter as ig
>>> L.sort(key=ig(1))
>>> 
```

The keys in this dict appear in the order in which they were added:

```
>>> D = defaultdict(int)
>>> for c in 'abcde':
...     D[c] += 1
... 
>>> list(D.items())
[('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)]
>>> 
```