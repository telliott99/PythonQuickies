#### Variable length argument list

For the SHA project I wanted to wrap Python bit-wise operations in a named function, because I thought it might be clearer.  So I did something like this:

```
def AND(*args):
    L = list(args)
    x = L.pop(0)
    while L:
        y = L.pop(0)
        x = x & y
    return x

print AND(1,3)
print AND(1,2,3)
```

The output of the first call is `1` and the second gives `0`.

The function's argument is `*args`.  The asterisk indicates a variadic argument, which is a variable (arbitrary) number of arguments.  

`args` is a tuple, and I wanted to iterate through it by using `pop`, which requires a list.  

One could also use an index like this:

```
def AND(*args):
    L = list(args)
    x = L[0]
    if len(L) == 1:
        return x
    for y in L[1:]:
        x = x & y
    return x

print AND(1,3)
print AND(1,2,3)
```

Later I remembered the `operator` module

```
import operator

def AND(*args):
    return reduce(operator.and_, args)
```

Short and sweet, but for my project I wanted to print all the values as they are processed, which this would not allow.

#### Plus a keyword argument

I also wanted to pass an argument (`v` for `verbose`), to control diagnostic printing.  Normally I would just do:

```
def AND(x, y, v=True):
```

but 

```
def AND(*args, v=True):
```

is a SyntaxError.  So, playing around with 

```
def AND(*args, **kwargs):
```

which I rewrote as

```
def f(*T,**D):
    for e in T:
        print e
    print D['v']

f('a','b','c', v=True)
```

I always use `L` for list, `D` for dict, and `T` for tuple.  For that matter, `i` and `j` for index, `s` and `t` for strings, `n` for number, `N` for constant number, and `x` and `y` for variables.

```
> python script.py 
a
b
c
True
>
```

The thing that was counterintuitive to me was the switch from `v` in calling the function to `D['v']` in looking up the value in the keywords dictionary.  The keys to the dictionary are strings.

But that's how you do it.

