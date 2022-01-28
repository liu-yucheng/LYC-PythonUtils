"""Main package."""

# Copyright 2022 Yucheng Liu. GNU GPL3 license.
# GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng

from lyc_pyutils.libs import batchlog
from lyc_pyutils.libs import dotdict
from lyc_pyutils.libs import functhread
from lyc_pyutils.libs import jsonrw
from lyc_pyutils.libs import randbool
from lyc_pyutils.libs import textrw
from lyc_pyutils.libs import timedinput


DotDict = dotdict.DotDict

TimedInput = timedinput.TimedInput

FuncThread = functhread.FuncThread

rand_bool = randbool.rand_bool

load_json = jsonrw.load_json
save_json = jsonrw.save_json
load_json_str = jsonrw.load_json_str
save_json_str = jsonrw.save_json_str

logstr = batchlog.logstr
logln = batchlog.logln
flushlogs = batchlog.flushlogs

load_text = textrw.load_text
save_text = textrw.save_text