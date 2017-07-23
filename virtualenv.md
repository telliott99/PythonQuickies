#### Using a virtual environment

The command to remember is:

    source bin/activate

```
> cd mpl
> source bin/activate
(mpl) > pip install numpy
Collecting numpy
...
Successfully installed numpy-1.13.1
> 
```
Example

```
> cd mpl
> source bin/activate
(mpl) > python
Python 2.7.13 (default, Jul  9 2017, 16:40:37) 
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.test('full')
Running unit tests for numpy
NumPy version 1.13.1
NumPy relaxed strides checking option: True
NumPy is installed in /Users/telliott/Desktop/mpl/lib/python2.7/site-packages/numpy
Python version 2.7.13 (default, Jul  9 2017, 16:40:37) [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
nose version 1.3.7
............
```

When you're finished:

    deactivate

or just quit Terminal.

#### Obtaining virtualenv

Use `pip` 

```
> pip install virtualenv
Collecting virtualenv
  Using cached virtualenv-15.1.0-py2.py3-none-any.whl
Installing collected packages: virtualenv
Successfully installed virtualenv-15.1.0
> pip install nose
> 
```

#### Setting up a new environment

    virtualenv <new directory>

```
> pwd
/Users/telliott_admin/Desktop
> virtualenv mpl
New python executable in /Users/telliott_admin/Desktop/mpl/bin/python2.7
Also creating executable in /Users/telliott_admin/Desktop/mpl/bin/python
Installing setuptools, pip, wheel...done.
>
```


