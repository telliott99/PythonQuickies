I installed Python 2 via Homebrew.

```
> which python
/usr/local/bin/python
> python
Python 2.7.15 (default, Jul 23 2018, 21:27:06) 
..
>>> 
```

The back arrow doesn't work

```
>>> xyz^[[D
```

Neither does up arrow

```
>>> ^[[A
```

My Python 3 install from Homebrew does work properly.

According to the [internet](https://stackoverflow.com/questions/893053/seeing-escape-characters-when-pressing-the-arrow-keys-in-python-shell)

this happens when Python doesn't have readline.

```
>>> import readline
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: dlopen(/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/readline.so, 2): Library not loaded: /usr/local/opt/readline/lib/libreadline.7.dylib
  Referenced from: /usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/readline.so
  Reason: image not found
>>>
```

Should I use pip or brew?  pip fails

https://pypi.org/project/gnureadline/

I did ``pip install gnureadline`` but python was still borked.

brew says

```
> brew install readline
Warning: readline 8.0.0 is already installed and up-to-date
To reinstall 8.0.0, run `brew reinstall readline`
>
```

Try ``brew upgrade python2``.  

I get 2.7.16 and arrows work.



