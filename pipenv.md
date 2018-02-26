#### pipenv

[python-guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

>    While pip can install Python packages, Pipenv is recommended as it’s a higher-level tool that simplifies dependency management for common use cases.

#### Usage

```
> mkdir myproject
> cd myproject
> pipenv install requests
Creating a virtualenv for this project…
⠋New python executable in /Users/telliott_admin/.local/share/virtualenvs/myproject-azAIXmGA/bin/python2.7
Also creating executable in /Users/telliott_admin/.local/share/virtualenvs/myproject-azAIXmGA/bin/python
Installing setuptools, pip, wheel...done.

Virtualenv location: /Users/telliott_admin/.local/share/virtualenvs/myproject-azAIXmGA
Creating a Pipfile for this project…
Installing requests…
Collecting requests
  Using cached requests-2.18.4-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests)
  Using cached certifi-2018.1.18-py2.py3-none-any.whl
Collecting chardet<3.1.0,>=3.0.2 (from requests)
  Using cached chardet-3.0.4-py2.py3-none-any.whl
Collecting idna<2.7,>=2.5 (from requests)
  Using cached idna-2.6-py2.py3-none-any.whl
Collecting urllib3<1.23,>=1.21.1 (from requests)
  Using cached urllib3-1.22-py2.py3-none-any.whl
Installing collected packages: certifi, chardet, idna, urllib3, requests
Successfully installed certifi-2018.1.18 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22

Adding requests to Pipfile's [packages]…
  PS: You have excellent taste! ✨ 🍰 ✨
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Updated Pipfile.lock (2f8679)!
> 
```

Here's the ``Pipfile``

```
> cat Pipfile
[[source]]

url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[dev-packages]

[packages]
requests = "*"
>
```

(removed extra spaces).

And ``Pipfile.lock``

```
{
    "_meta": {
        "hash": {
            "sha256": "a0e63f8a0d1e3df046dc19b3ffbaaedfa151afc12af5a5b960ae7393952f8679"
        },
        "host-environment-markers": {
            "implementation_name": "cpython",
            "implementation_version": "0",
            "os_name": "posix",
            "platform_machine": "x86_64",
            "platform_python_implementation": "CPython",
            "platform_release": "17.3.0",
            "platform_system": "Darwin",
            "platform_version": "Darwin Kernel Version 17.3.0: Thu Nov  9 18:09:22 PST 2017; root:xnu-4570.31.3~1/RELEASE_X86_64",
            "python_full_version": "2.7.13",
            "python_version": "2.7",
            "sys_platform": "darwin"
        },
        "pipfile-spec": 6,
        "requires": {},
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.python.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "certifi": {
            "hashes": [
                "sha256:14131608ad2fd56836d33a71ee60fa1c82bc9d2c8d98b7bdbc631fe1b3cd1296",
                "sha256:edbc3f203427eef571f79a7692bb160a2b0f7ccaa31953e99bd17e307cf63f7d"
            ],
            "version": "==2018.1.18"
        },
        "chardet": {
            "hashes": [
                "sha256:fc323ffcaeaed0e0a02bf4d117757b98aed530d9ed4531e3e15460124c106691",
                "sha256:84ab92ed1c4d4f16916e05906b6b75a6c0fb5db821cc65e70cbd64a3e2a5eaae"
            ],
            "version": "==3.0.4"
        },
        "idna": {
            "hashes": [
                "sha256:8c7309c718f94b3a625cb648ace320157ad16ff131ae0af362c9f21b80ef6ec4",
                "sha256:2c6a5de3089009e3da7c5dde64a141dbc8551d5b7f6cf4ed7c2568d0cc520a8f"
            ],
            "version": "==2.6"
        },
        "requests": {
            "hashes": [
                "sha256:6a1b267aa90cac58ac3a765d067950e7dbbf75b1da07e895d1f594193a40a38b",
                "sha256:9c443e7324ba5b85070c4a818ade28bfabedf16ea10206da1132edaa6dda237e"
            ],
            "version": "==2.18.4"
        },
        "urllib3": {
            "hashes": [
                "sha256:06330f386d6e4b195fbfc736b297f58c5a892e4440e54d294d7004e3a9bbea1b",
                "sha256:cc44da8e1145637334317feebd728bd869a35285b93cbb4cca2577da7e62db4f"
            ],
            "version": "==1.22"
        }
    },
    "develop": {}
}
```

#### Example script

```
> pwd
/Users/telliott_admin/Desktop/myproject
> touch main.py
> te main.py
```

Editing in TextEdit, add this:

```
import requests
response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))
```

and run

```
> pipenv run python main.py
Your IP is 71.204.242.36
>
```

>    Using $ pipenv run ensures that your installed packages are available to your script. It’s also possible to spawn a new shell that ensures all commands have access to your installed packages with $ pipenv shell.

#### Differences from ``pip``

One difference is that the Python executable is not in an ``env`` directory in the project but in 

```
> cd ~/.local/share/virtualenvs/
> ls
myproject-azAIXmGA
python-getting-started-mM2D4K1m
tmp-7KTiVFNJ
> cd myproject-yEdlF3rC/
```

These are pretty lightweight:

```

```

```
> ls
bin			lib
include			pip-selfcheck.json
> ls -al
total 8
drwxr-xr-x   7 telliott_admin  staff  224 Jan 20 09:16 .
drwxr-xr-x   5 telliott_admin  staff  160 Jan 20 09:16 ..
lrwxr-xr-x   1 telliott_admin  staff   79 Jan 20 09:16 .Python -> /usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/Python
drwxr-xr-x  17 telliott_admin  staff  544 Jan 20 09:16 bin
drwxr-xr-x   3 telliott_admin  staff   96 Jan 20 09:16 include
drwxr-xr-x   3 telliott_admin  staff   96 Jan 20 09:16 lib
-rw-r--r--   1 telliott_admin  staff   60 Jan 20 09:16 pip-selfcheck.json
> ls -al bin
total 128
drwxr-xr-x  17 telliott_admin  staff    544 Jan 20 09:16 .
drwxr-xr-x   7 telliott_admin  staff    224 Jan 20 09:16 ..
-rw-r--r--   1 telliott_admin  staff   2124 Jan 20 09:16 activate
-rw-r--r--   1 telliott_admin  staff   1066 Jan 20 09:16 activate.csh
-rw-r--r--   1 telliott_admin  staff   2220 Jan 20 09:16 activate.fish
-rw-r--r--   1 telliott_admin  staff   1137 Jan 20 09:16 activate_this.py
-rwxr-xr-x   1 telliott_admin  staff    288 Jan 20 09:16 chardetect
-rwxr-xr-x   1 telliott_admin  staff    297 Jan 20 09:16 easy_install
-rwxr-xr-x   1 telliott_admin  staff    297 Jan 20 09:16 easy_install-2.7
-rwxr-xr-x   1 telliott_admin  staff    269 Jan 20 09:16 pip
-rwxr-xr-x   1 telliott_admin  staff    269 Jan 20 09:16 pip2
-rwxr-xr-x   1 telliott_admin  staff    269 Jan 20 09:16 pip2.7
lrwxr-xr-x   1 telliott_admin  staff      9 Jan 20 09:16 python -> python2.7
-rwxr-xr-x   1 telliott_admin  staff   2383 Jan 20 09:16 python-config
lrwxr-xr-x   1 telliott_admin  staff      9 Jan 20 09:16 python2 -> python2.7
-rwxr-xr-x   1 telliott_admin  staff  12568 Jan 20 09:16 python2.7
-rwxr-xr-x   1 telliott_admin  staff    276 Jan 20 09:16 wheel
> 
```



#### Installation

Use ``pip`` to install ``pipenv``.

```
> pip install --user pipenv
```

A user-specific installation is recommended.  I did it system-wide.

>    If pipenv isn’t available in your shell after installation, you’ll need to add the user base‘s binary directory to your PATH.

>    On Linux and macOS you can find the user base binary directory by running python -m site --user-base and adding bin to the end. For example, this will typically print ~/.local (with ~ expanded to the absolute path to your home directory) so you’ll need to add ~/.local/bin to your PATH. You can set your PATH permanently by modifying ~/.profile.

```
> python -m site --user-base
/Users/telliott_admin/Library/Python/2.7
> 
```

So my base binary directory is that with ``bin``:

```
> ls /Users/telliott_admin/Library/Python/2.7/bin
flake8			pycodestyle
pew			pyflakes
pipenv			virtualenv-clone
>
```

My ``.local`` has only ``share``:

```
> ls ~/.local
share
> cd ~/.local/share
> ls
heroku		virtualenvs
>
```




