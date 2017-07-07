Python module:  **struct**

[docs](https://docs.python.org/2/library/struct.html)

* ``B`` unsigned char (1 byte)
* ``H`` unsigned short (2 bytes)
* ``I`` unsigned integer (2 bytes)

[format docs](https://docs.python.org/2/library/struct.html#format-characters)

```python
>>> import struct
>>> struct.pack('B', 255)
'\xff'
>>> struct.pack('I', 255)
'\xff\x00\x00\x00'
>>> struct.pack('H', 255)
'\xff\x00'
>>> struct.pack('I', 255)
'\xff\x00\x00\x00'
>>> 
```

#### Endianness

Notice that the low-value byte is the first to be listed in the printout.  Our ``ff`` goes first.  

The docs [say](https://docs.python.org/2/library/struct.html#byte-order-size-and-alignment)

> By default, C types are represented in the machine’s native format and byte order

If we want something different, we can specify the byte order with ``>`` or ``<``.  The ``>`` means "big-endian" (high-value byte first).

```python
>>> struct.pack('I', 255)
'\xff\x00\x00\x00'
>>> struct.pack('<I', 255)
'\xff\x00\x00\x00'
>>> struct.pack('>I', 255)
'\x00\x00\x00\xff'
>>> 
```

By comparison, we conclude that the default on macOS is little-endian, least-significant byte first.

macOS [docs](https://developer.apple.com/library/content/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/ByteOrdering.html)

> Intel x86 processors store a two-byte integer with the least significant byte first

This changed with the switch away from Pentium some years ago

[wikipedia](https://en.wikipedia.org/wiki/Endianness) on endianness.

#### More

More complicated example from [pmotw](https://pymotw.com/2/struct/)


```python
>>> import struct
>>> values = [1, 'ab', 2.7]
>>> st = struct.Struct('I 2s f')
>>> data = st.pack(*values)
>>> data
'\x01\x00\x00\x00ab\x00\x00\xcd\xcc,@'
```
So I am not exactly sure about the float on the end, but the result is clear.  We have four bytes for the integer 1 in hex in least-endian order:

```
'\x01\x00\x00\x00'
```

followed by the two hex bytes:

```python
'\x01\x00\x00\x00ab
```

**struct** can also unpack but why bother?

From our example above:

```python
>>> st2 = struct.Struct('I 2s f')
>>> st2.unpack(data)
(1, 'ab', 2.700000047683716)
>>>
```


```python
>>> struct.unpack('>H', '\x10\x00')
(4096,)
>>> 
```

