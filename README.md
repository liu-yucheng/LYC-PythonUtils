<!---
Copyright 2022 Yucheng Liu. GNU GPL3 lincense.
GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt
First added by username: liu-yucheng
Last updated by username: liu-yucheng
--->

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
Hello  # Entered "Hello" on keyboard
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

## `rand_bool`

`lyc_pyutils.randbool.rand_bool`

Shortcut: `lyc_pyutils.rand_bool`

## `load_json`

`lyc_pyutils.jsonrw.load_json`

Shortcut: `lyc_pyutils.load_json`

## `save_json`

`lyc_pyutils.jsonrw.save_json`

Shortcut: `lyc_pyutils.save_json`

## `logstr`

`lyc_pyutils.batchlog.logstr`

Shortcut: `lyc_pyutils.logstr`

## `logln`

`lyc_pyutils.batchlog.logln`

Shortcut: `lyc_pyutils.logln`

# Miscellaneous
## Versioning

```text
The versioning of this app is based on Semantic Versioning.
You can see the complete Semantic Versioning specification from
  https://semver.org/.
Basically, the version name of this app is in the form of:
  x.y.z
  Where x, y, and z are integers that are greater than or equal to 0.
  Where x, y, and z are separated by dots.
  x stands for the major version and indicates non-compatible major changes to
    the app.
  y stands for the minor version and indicates forward compatible minor
    changes to the app.
  z stands for the patch version and indicates bug fixes and patches to the
    app.
```

## Version Tags

```text
The version tags of this repo has the form of a letter "v" followed by a
  semantic version.
Given a semantic version:
  $x.$y.$z
  Where $x, $y, and $z are the semantic major, minor, and patch versions.
The corresponding version tag would be:
  v$x.$y.$z
The version tags are on the main branch.
```

## Copyright
### Short Version

```text
Copyright (C) 2022 Yucheng Liu. GNU GPL3 license (GNU General Public License
  Version 3).
You should have and keep a copy of the above license. If not, please get it
  from https://www.gnu.org/licenses/gpl-3.0.txt.
```

### Long Version

```text
LYC-PythonUtils, LYC's personal Python utility collection.
Copyright (C) 2022 Yucheng Liu. GNU GPL3 license (GNU General Public License
  Version 3).

This program is free software: you can redistribute it and/or modify it under
  the terms of the GNU General Public License as published by the Free
  Software Foundation, either version 3 of the License, or (at your option)
  any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
  FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
  more details.

You should have received a copy of the GNU General Public License along with
  this program. If not, see:
  1. The LICENSE file in this repository.
  2. https://www.gnu.org/licenses/.
  3. https://www.gnu.org/licenses/gpl-3.0.txt.
```
