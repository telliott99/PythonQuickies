#### virtualenv

[virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to create "isolated Python environments".  The problem is that different projects may require different versions for the modules they depend on:  newer isn't always better.

A virtual environment allows a project to share the Python interpeter, but have its own installed packages.  Get it like this:

```
> python3 -m pip install virtualenv
```

And use it like [this](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

```
> mkdir my_project
> cd my_project
> python3 -m venv env
```

This makes the ``env`` directory and a couple of sub-directories in ``my_project`` and sets them up to hold the modules I need.  The next thing is to *activate* the virtual environment.

```
> source env/bin/activate
(env) >
```


So now I might install the [cryptography](https://docs.python-guide.org/scenarios/crypto/) or the [PyCrypto]() module:

```
(env) > pip install cryptography
Collecting cryptography
..
(env) > pip install pycrypto

```

And use it like so:

```
(env) > python
Python 3.7.0 (default, Jul 23 2018, 20:22:55) 
..
>>> from Crypto.Cipher import AES
>>> encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
>>> cipher_text = encryption_suite.encrypt("A really secret message. Not for prying eyes.XXX")
>>> cipher_text[:10]
b'M,\xadT\xce\xd6\x9a\xea\x1b\xb6'
>>> len(cipher_text)
48
```

The message must be padded out to a multiple of 16 characters.

When you're finished:

```
(env) > deactivate
>
```

#### venv

A stripped-down version called ``venv`` is included in Python >= 3.4.  Do

```
> python3 -m venv
```
