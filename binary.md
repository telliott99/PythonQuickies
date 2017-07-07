### Functions for binary data

An excellent way to think about binary data is as a list or array of UInt8 (0..255).  

Go back and forth to ASCII with

* `ord`
* `chr`

```python
>>> s = 'cat'
>>> L = [ord(c) for c in s]
>>> L
[99, 97, 116]
>>> ''.join([chr(n) for n in range(96,96+26+1)])
'`abcdefghijklmnopqrstuvwxyz'
>>>
```

Perhaps `map` looks cleaner?


```python
>>> map(ord, '\x00\xff')
[0, 255]
>>>

```


So, one can think of ASCII as a compact byte representation in a string.  Non-printable characters are given as `\x0a` or whatever.

* `hex`
* `zfill`
* `int`

`hex` is, of course, a compact readable representation (see [here](ints-hex.md)).  The good news:  `hex` works on large ints

```python
>>> hex(sys.maxint+1)
'0x8000000000000000L'
>>>
```
The bad news: `hex` doesn't pad.  Some people prefer format strings, I use `zfill`.

```python
>>> hex(1)
'0x1'
>>> '0x' + hex(1)[2:].zfill(2)
'0x01'
>>>
```

However, it's awkward because we need to remove the `0x` first.

* `int`

```python
>>> int('ffe',16)
4094
>>> int('0xffe',16)
4094
>>>
```

`int` works on large hex numbers.

In Python, another way to represent bytes is to use a string of ASCII characters.  Non-printable characters are given as `\x0a` or whatever.

```python
>>> s = '\r\t\nabc\xff\01'
>>> s
'\r\t\nabc\xff\x01'
>>> [ord(c) for c in s]
[13, 9, 10, 97, 98, 99, 255, 1]
>>>
```

These are called [string literals](https://docs.python.org/2.7/reference/lexical_analysis.html#string-literals).

* `hexlify` 

can turn binary strings into hex:

```python
>>> from binascii import *
>>> hexlify('\r\t\nabc\xff\x01')
'0d090a616263ff01'
>>>
```

* `unhexlify`

does the reverse.

```python
>>> unhexlify('616263')
'abc'
>>> unhexlify('00ff')
'\x00\xff'
>>>
```