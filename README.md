<!---
Copyright 2022 Yucheng Liu. GNU LGPL3 license.
GNU LGPL3 license copy: https://www.gnu.org/licenses/lgpl-3.0.txt
GNU LGPL3 is based on GNU GPL3, GNU GPL3 copy: https://www.gnu.org/licenses/gpl-3.0.txt
First added by username: liu-yucheng
Last updated by username: liu-yucheng
--->

# LYC-PythonUtils

Personal Python utility collection library.

# Installation (Using `pip`)

- Go to the root directory of this repo.
- The requirements.txt is empty. No dependency installations required.
- Development installation: run the `pip install -e .` command.
- ~~Deployment installation: run the `pip install .` command.~~ (Temporarily unavailable.)
- You can now access the libraries by importing the `lyc_pyutils` package.

# Using The Utilities

## `DotDict`

- Full path: `lyc_pyutils.libs.dotdict.DotDict`
- Shortcut: `lyc_pyutils.DotDict`

Dot dictionary, API version 2.

**Not API-compatible with the API version 1 dot dictionary.**

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
>>> sample2 = sample.to_dict____()
>>> print(sample2)
{'attr1': 1, 'attr2': 1.1, 'attr3': True, 'attr4': 'Hello', 'attr5': {'hello': 'World'}}
>>>
```

## `TimedInput`

- Full path: `lyc_pyutils.libs.timedinput.TimedInput`
- Shortcut: `lyc_pyutils.TimedInput`

Python "native" and platform independent timed input.

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

- Full path: `lyc_pyutils.libs.functhread.FuncThread`
- Shortcut: `lyc_pyutils.FuncThread`

An extended Python standard library thread with return value(s).

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

- Full path: `lyc_pyutils.libs.randbool.rand_bool`
- Shortcut: `lyc_pyutils.rand_bool`

Random Boolean value generator.

Python interactive shell demo use case:

```python
>>> import lyc_pyutils
>>> lyc_pyutils.rand_bool()
False
>>> lyc_pyutils.rand_bool()
False
>>> lyc_pyutils.rand_bool()
False
>>> lyc_pyutils.rand_bool()
True
>>> lyc_pyutils.rand_bool()
True
>>> lyc_pyutils.rand_bool()
True
>>> lyc_pyutils.rand_bool()
True
>>> lyc_pyutils.rand_bool()
True
>>> lyc_pyutils.rand_bool()
False
>>> lyc_pyutils.rand_bool()
False
>>> lyc_pyutils.rand_bool()
False
>>> lyc_pyutils.rand_bool()
True
>>>
```

## `load_json`

- Full path: `lyc_pyutils.libs.jsonrw.load_json`
- Shortcut: `lyc_pyutils.load_json`

Loads a JSON object from a text file and returns the object.

NOTE: the returned object has inferred types.

## `save_json`

- Full path: `lyc_pyutils.libs.jsonrw.save_json`
- Shortcut: `lyc_pyutils.save_json`

Saves a JSON object to a text file.

## `load_json_str`

- Full path: `lyc_pyutils.libs.jsonrw.load_json_str`
- Shortcut: `lyc_pyutils.load_json_str`

Loads a JSON object from a string and returns the object.

NOTE: the returned object has inferred types.

Python interactive shell demo use case:

```python
>>> import lyc_pyutils
>>> cfg1 = fr"""
... {{
...     "config": "config1"
... }}
... """
>>> loaded_cfg1 = lyc_pyutils.load_json_str(cfg1)
>>> loaded_cfg1
{'config': 'config1'}
>>>
```

## `save_json_str`

- Full path: `lyc_pyutils.libs.jsonrw.save_json_str`
- Shortcut: `lyc_pyutils.save_json_str`

Saves a JSON object to a string and returns the string.

Python interactive shell demo use case:

```python
>>> import lyc_pyutils
>>> cfg1 = {"config": "config1"}
>>> lyc_pyutils.save_json_str(cfg1)
'{\n    "config": "config1"\n}'
>>>
```

## `logstr`

- Full path: `lyc_pyutils.libs.batchlog.logstr`
- Shortcut: `lyc_pyutils.logstr`

Logs a string to a list of logs.

## `logln`

- Full path: `lyc_pyutils.libs.batchlog.logln`
- Shortcut: `lyc_pyutils.logln`

Logs a line to a list of logs.

## `flushlogs`

- Full path: `lyc_pyutils.libs.batchlog.flushlogs`
- Shortcut: `lyc_pyutils.flushlogs`

Flushes each log in a list of logs.

## `load_text`

- Full path: `lyc_pyutils.libs.textrw.load_text`
- Shortcut: `lyc_pyutils.load_text`

Loads the data from a text file to a string and returns the string.

## `save_text`

- Full path: `lyc_pyutils.libs.textrw.save_text`
- Shortcut: `lyc_pyutils.save_text`

Saves a string to a text file.

## `clamp_float`

- Full path: `lyc_pyutils.clamps.clamp_float`
- Shortcut: `lyc_pyutils.clamp_float`

Clamps a number to a range and returns a float.

Python interactive shell demo use case:

```python
>>> import lyc_pyutils
>>> lyc_pyutils.clamp_float(0.5, 0.0, 1.0)
0.5
>>> lyc_pyutils.clamp_float(1.5, 0.0, 1.0)
1.0
>>> lyc_pyutils.clamp_float(-0.5, 0.0, 1.0)
0.0
>>> lyc_pyutils.clamp_float(0.5, 1.0, 0.0)
0.5
>>> lyc_pyutils.clamp_float(1.5, 1.0, 0.0)
1.0
>>> lyc_pyutils.clamp_float(-0.5, 1.0, 0.0)
0.0
>>>
```

## `clamp_int`

- Full path: `lyc_pyutils.clamps.clamp_int`
- Shortcut: `lyc_pyutils.clamp_int`

Clamps a number to a range and returns an integer.

Python interactive shell demo use case:

```python
>>> import lyc_pyutils
>>> lyc_pyutils.clamp_int(1, 0, 2)
1
>>> lyc_pyutils.clamp_int(3, 0, 2)
2
>>> lyc_pyutils.clamp_int(-1, 0, 2)
0
>>> lyc_pyutils.clamp_int(1, 2, 0)
1
>>> lyc_pyutils.clamp_int(3, 2, 0)
2
>>> lyc_pyutils.clamp_int(-1, 2, 0)
0
>>>
```

# Testing

You can test this library by running `python <this-repo>/test_all.py`.

# Python Code Style

Follows [PEP8](https://peps.python.org/pep-0008/) with the exceptions shown in the following VSCode `settings.json` code fragment.

```json
{
  ...,
  "python.formatting.provider": "autopep8",
  "python.formatting.autopep8Args": [
    "--max-line-length=119"
  ],
  "python.linting.enabled": true,
  "python.linting.pycodestyleEnabled": true,
  "python.linting.pycodestyleArgs": [
    "--max-line-length=119"
  ],
  ...
}
```

# Change In License

On 8 April 2022, LYC-PythonUtils (versions from `1.1.4` to present) changed its license from GNU GPL3 to GNU LGPL3.

The license of all previous versions of LYC-PythonUtils (versions from `0.1.0` to `1.1.3`) remains unchanged.

- LYC-PythonUtils (versions `>= 1.1.4`): GNU LGPL3
- LYC-PythonUtils (`0.1.0 <=` versions `>= 1.1.3`): GNU GPL3

The above changes take effect because they are agreed by 100%  (1/1, `>=` 100%) of the contributors (prior to 8 April 2022) to this repository.

# Miscellaneous

## Developer's Notes 📝 And Warnings ⚠️

### Notes 📝

This library is distributed under the **[GNU LGPL3 license](LICENSE).**

GNU LGPL3 is based on **[GNU GPL3](README-Assets/GNU-GPL3-License.txt).**

A subsequent work of this library is a work that satisfies **any one** of the following:

- Is a variant of any form of this library.
- Contains a part, some parts, or all parts of this library.
- Integrates a part, some parts, or all parts of this library.

A library usage notice is a prominent notice saying that this library is used and that this library and its use are covered by the GNU LGPL3 license.

All subsequent works of this library **must include a library usage notice** (as defined above).

### Warnings ⚠️

**Not including a library usage notice** (as defined above) in any subsequent work (as defined above) of this library, and distribute it to the public is **unlawful**, no matter if such work makes a profit.

Doing so may result in severe civil and criminal penalties.

I reserve the rights, funds, time, and efforts to prosecute those who violate the license of this library to the maximum extent under applicable laws.

## Versions

### Versioning

```text
The versioning of this library is based on Semantic Versioning.
You can see the complete Semantic Versioning specification from
  https://semver.org/.
Basically, the version name of this library is in the form of:
  x.y.z
  Where x, y, and z are integers that are greater than or equal to 0.
  Where x, y, and z are separated by dots.
  x stands for the major version and indicates non-compatible major changes to
    the library.
  y stands for the minor version and indicates forward compatible minor
    changes to the library.
  z stands for the patch version and indicates bug fixes and patches to the
    library.
```

### Version Tags

```text
The version tags of this repository has the form of a letter "v" followed by a
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
Copyright (C) 2022 Yucheng Liu. GNU LGPL3 license (GNU Lesser General Public
  License Version 3).
You should have and keep a copy of the above license. If not, please get it
  from https://www.gnu.org/licenses/lgpl-3.0.txt.
GNU LGPL3 is based on GNU GPL3, and you can find the GNU GPL3 copy at
  https://www.gnu.org/licenses/gpl-3.0.txt
```

### Long Version

```text
LYC-PythonUtils, LYC's personal Python utility library.
Copyright (C) 2022 Yucheng Liu. GNU LGPL3 license (GNU Lesser General Public
  License Version 3).

This program is free software: you can redistribute it and/or modify it under
  the terms of the GNU Lesser General Public License as published by the Free
  Software Foundation, either version 3 of the License, or (at your option)
  any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
  FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License
  for more details.

You should have received a copy of the GNU Lesser General Public License along
  with this program. If not, see:
  1. The LICENSE file in this repository.
  2. https://www.gnu.org/licenses/#LGPL.
  3. https://www.gnu.org/licenses/lgpl-3.0.txt.

GNU Lesser General Public License Version 3 is based on the GNU General Public
  License Version 3. You can find a copy of the GNU General Public License
  Version 3 at:
  1. The README-Assets/GNU-GPL3-License.txt file in this repository.
  2. https://www.gnu.org/licenses/#GPL.
  3. https://www.gnu.org/licenses/gpl-3.0.txt.
```
