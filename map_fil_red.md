### Python map, filter and reduce

These functions are in functools.  ``map`` and ``filter`` are in the global "namespace".

#### map

``map`` applies a function to each element of a list and in Python 2 it returns a new list.

```
>>> def f(n):
...    return n**2
...
>>> m = map(f,[1,2,3])
```

In Python 3 ``m`` is a ``map object``.  You can iterate over ``m`` or convert it to a list.

```
>>> list(m)
[1, 4, 9]
```

#### filter

``filter`` applies a function that returns ``True`` or ``False`` to each element of a list and returns a list containing those elements for which the function returns ``True``.


```
>>> def optimist(n):
...     return True
... 
>>> list(filter(optimist, [1,2,3]))
[1, 2, 3]
>>>
```

#### reduce

In Python 3 we must explicitly import ``reduce``.

To use standard functions, their names must be imported from the ``operator`` module.

```
>>> from functools import reduce
>>> import operator as op
>>> reduce(op.mul, [1,2,3,4])
24
>>> reduce(op.xor, [1,2,3])
0
>>>
```

```
>>> def f(a,b):
...     return a ^ b
... 
>>> reduce(f,[1,2,3,4])
4
>>>
```


