#### Python 2 => 3

What's different about Python 3?  Here is a nice [summary](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html).

If you try to run code written for Python 3 with Python 2, you'll likely run into trouble.  How about updating 2 to 3?  That's what we'd like to understand.

#### print

The most obvious thing is the parentheses for a ``print`` statement.  That doesn't seem like a big deal.  It's backwards compatible to 2.

```
>>> print('a','b')
a b
>>>
```

Well, that works as it would in 2.

#### Integer division

In 3:

```
>>> 3/2 
1.5
>>> 3//2
1
>>>
```

So the default is real division and you don't have to do this anymore.  In 2:

```
>>> 3 * 1.0 / 2
>>> 
```

#### Strings and bytes

Python 2 has ``str`` and unicode.  It's a bit complicated [see here](https://docs.python.org/2/howto/unicode.html).

Python 3 strings are UTF-8.

```
>>> print('strings are now utf-8 \u03BCnico\u0394é!')
strings are now utf-8 μnicoΔé!
>>>
```

```
>>> 
>>> print('strings are now utf-8 \u03BCnico\u0394é!')
strings are now utf-8 μnicoΔé!
>>>
```

We have ``bytes``

```
>>> s = 'abc'
>>> bytes(s, encoding = 'utf8')
b'abc'
>>> [n for n in _]
[97, 98, 99]
>>> 
```



