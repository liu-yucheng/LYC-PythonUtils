# LYC-PythonUtils

My personal Python utilities.

# Installing Using `pip`

- Go to the root directory of this repo.
- The requirements.txt is empty. No dependency installations required.
- Development installation: run the `pip install -e .` command.
- Deployment installation: run the `pip install .` command.
- You can now access the libraries by importing the `lyc_pyutils` package.

# Using The Utilities

## `DotDict `

`lyc_pyutils.dotdict.DotDict`

Shortcut: `lyc_pyutils.DotDict`

Python interactive shell demo use case:

```python
>>> from lyc_pyutils import dotdict
>>> DotDict = dotdict.DotDict
>>>
>>> sample = DotDict()
>>> print(sample)
.{}
>>>
>>> sample.attr1 = 1
>>> sample.attr2 = 1.1
>>> sample.attr3 = True
>>> sample.attr4 = "Hello"
>>> print(sample)
.{attr1: 1, attr2: 1.1, attr3: True, attr4: Hello}
>>> print(sample.attr4)
Hello
>>>
>>> sample.attr5 = {"hello": "World"}
>>> print(sample)
.{attr1: 1, attr2: 1.1, attr3: True, attr4: Hello, attr5: .{hello: World}}
>>> print(sample.attr5.hello)
World
>>>
>>> sample2 = sample.todict____()
>>> print(sample2)
{'attr1': 1, 'attr2': 1.1, 'attr3': True, 'attr4': 'Hello', 'attr5': {'hello': 'World'}}
>>>
```

## `TimedInput`

`lyc_pyutils.timedinput.TimedInput`

Shortcut: `lyc_pyutils.TimedInput`

Python interactive shell demo use case:

```python
>>> from lyc_pyutils import timedinput
>>> TimedInput = timedinput.TimedInput
>>>
>>> sample = TimedInput()
>>> sample2 = sample.take(timeout=10)
Hello                                   # Entered "Hello" on keyboard
>>> print(sample2)
Hello
>>> sample3 = sample.take(timeout=10)
                                        # Entered nothing, waited for timeout
>>> print(sample3)
None
>>> print(sample3 is None)
True
>>>
```


## `FuncThread`

`lyc_pyutils.functhread.FuncThread`

Shortcut: `lyc_pyutils.FuncThread`

Python interactive shell demo use case:

```python
>>> import lyc_pyutils
>>> def func():
...   return "Hello world!"
...
>>> thread = lyc_pyutils.FuncThread(target=func, args=[])
>>> thread.start()
>>> thread.join(timeout=None)
'Hello world!'
>>>
```
