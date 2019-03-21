#### virtualenv update

With Python3 we have now ``venv``.

``virtualenv`` has been around for a while ([link]()).  It's installed with ``pip``.

In Python 3.4 ``pyvenv`` was added.  I know because I googled and found [this](http://masnun.com/2016/04/10/python-pyenv-pyvenv-virtualenv-whats-the-difference.html).  ``pyvenv`` (not ``pyenv``) comes with Python!  

But after my install I have "command not found."

The reason is that it's been deprecated. [docs](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/#heroku-setup)

>   The pyvenv script has been deprecated as of Python 3.6 in favor of using 

```
python3 -m venv
```
to help prevent any potential confusion as to which Python interpreter a virtual environment will be based on.
