#### pip

Python comes with ``pip``.

[docs](http://pip-python3.readthedocs.io/en/latest/user_guide.html) for Python3.


```
> pip --version
pip 9.0.1 from /usr/local/lib/python2.7/site-packages (python 2.7)
> which pip
/usr/local/bin/pip
> pip install --upgrade pip
Requirement already up-to-date: pip in /usr/local/lib/python2.7/site-packages
>
```

We must use the version for Python3 specifically:

```
> pip3 --version
pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)
>
```

#### ``requirements.txt``

For virtual environments, once can direct ``pip`` to install a bunch of modules all at once, by putting them in a file ``requirements.txt``.

```
pip install -r requirements.txt
```

Alternatively, with a bunch of modules installed, get their names with ``freeze``, and save it to that file.

```
pip freeze > requirements.txt
```

