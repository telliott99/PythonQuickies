#### Iterators

```
>>> L = list('ab')
>>> itr = iter(L)
>>> next(itr)
'a'
>>> next(itr)
'b'
>>> next(itr)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
```

The ``iter`` keyword takes an iterable (like a list) and returns an iterator, which has a method ``next`` that returns each item in the iterable in turn, until it is exhausted, and returns the exception ``StopIteration``.


```
>>> def f(s):
...     L = list(s)
...     itr = iter(L)
...     while True:
...         try:
...             print(next(itr))
...         except StopIteration:
...             break
... 
>>> f('abc')
a
b
c
>>> 
```

We can build our own iterator objects like this:

```
class Test:
    def __init__(self,i,j,down=False):
        self.flag = down
        if not down:
            self.i = i
            self.j = j
        else:
            self.i = j
            self.j = i
    
    def __iter__(self):
        return self

    def next(self):
        x = self.i
        if not self.flag: # up
            if x > self.j:
                raise StopIteration
            else:
                self.i = x + 1
        else:
            if x < self.j:
                raise StopIteration
            else:
                self.i = x - 1
        return x

a = Test(1,3,down=True)
print(a.next())
for e in a:
    print e
```

output:

```
> python test.py 
3
2
1
>
```