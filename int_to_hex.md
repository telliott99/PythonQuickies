### Converting ints <---> hex

Going forward, from ints to hex, use `hex`.

```
>>> hex(65537)
'0x10001'
>>>
```

`hex` can handle a UInt64 or even bigger.

```
>>> n
88888888888888888888888888888888888888888L
>>> hex(n)
'0x1053891488fa946a7bd9168b38e38e38e38L'
>>>
```

The default behavior is to strip off leading zeros.  My usual solution is `zfill`

```
>>> hex(1)
'0x1'
>>> 
>>> '0x' + hex(1)[2:].zfill(2)
'0x01'
>>> 
```

The suggestion often is to use a format string, but I find that complicated and hard to remember.

Going backward, from hex to ints, we can use `int(h,16)`.

```
>>> h
'0x0123456789abcdef'
>>> int(h,16)
81985529216486895
```

While the above conveniently saves us a calculation, often we want the individual bytes.

```
>>> hL = [h[i:i+2] for i in range(2,len(h),2)]
>>> hL
['01', '23', '45', '67', '89', 'ab', 'cd', 'ef']
>>> [int(x,16) for x in hL]
[1, 35, 69, 103, 137, 171, 205, 239]
>>>
```

Beware of `bytearray` (it isn't what it seems):

```
>>> h = '0xabcdef'
>>> ba = bytearray(h)
>>> ba
bytearray(b'0xabcdef')
>>> for b in ba:  print b
... 
48
120
97
98
99
100
101
102
>>>
```

The good news:  under the hood, a bytearray is an array of ints. The bad news:  feeding hex data to `bytearray` does not do what you would expect.


