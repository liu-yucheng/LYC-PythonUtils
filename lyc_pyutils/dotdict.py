"""Dot dictionary."""

# Copyright 2022 Yucheng Liu. GNU GPL3 license.
# GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt
# First added by username: liu-yucheng
# Last updated by username: liu-yucheng


class DotDict:
    """Dot dictionary.

    A dictionary whose items can be accessed with the "dict.key" syntax.
    Dot dictionary is recursively compatible with the Python standard library dict.
    4 trailing underscores added to all public method names to avoid key or attribute naming confusions.
    """

    # Copyright 2022 Yucheng Liu. GNU GPL3 license.
    # GNU GPL3 license copy: https://www.gnu.org/licenses/gpl-3.0.txt

    @classmethod
    def fromdict____(cls, dic):
        """Builds and gives an DotDict from a Python standard library dict.

        Args:
            dic: the dictionary

        Returns:
            result: the resulting DotDict
        """
        # print(f"fromdict____ dic: {dic}")  # Debug
        result = DotDict()
        for key in dic:
            result.setattr____(key, dic[key])
        return result

    @classmethod
    def isprotected____(cls, key):
        """Finds if a key is protected.

        Args:
            key: the key

        Returns:
            result: the result
        """
        # print(f"isprotected____ key: {key}")  # Debug
        key = str(key)
        result = key[:1] == "_"  # See whether the key is private
        result = result or len(key) >= 4 and key[:2] == "__" and key[-2:] == "__"  # See whether the key is magic
        result = result or key[-4:] == "____"  # See whether the key is DotDict reserved
        return result

    # Magic functions

    def __init__(self, *args, **kwargs):
        """Inits self with the given args and kwargs.

        Args:
            *args: the variable arguments
            **kwargs: the keyword arguments
        """
        super().__init__()
        selftype = type(self)

        # Set the inherited keys from the custom class level
        if selftype is not DotDict and issubclass(selftype, DotDict):
            classdict = type(self).__dict__
            for key in classdict:
                key = str(key)
                # print(f"__init__ classdict {key}: {classdict[key]}")  # Debug
                if not type(self).isprotected____(key):
                    value = classdict[key]
                    self.setattr____(key, value)

        # Set keys with the key names from the variable arguments
        for arg in args:
            arg = str(arg)
            # print(f"__init__ *args arg {arg}")  # Debug
            if not selftype.isprotected____(key):
                self.setattr____(arg, None)

        # Set keys with the key names and values from the keyword arguments
        for kw in kwargs:
            kw = str(kw)
            # print(f"__init__ **kwargs kw {kw}: {kwargs[kw]}")  # Debug
            if not selftype.isprotected____(key):
                self.setattr____(kw, kwargs[kw])

    def __getattr__(self, name):
        return self.getattr____(name)

    def __setattr__(self, name, value):
        return self.setattr____(name, value)

    def __str__(self):
        return self.str____()

    def __len__(self):
        return self.__dict__.__len__()

    def __iter__(self):
        return self.__dict__.__iter__()

    def __getstate__(self):
        return self.todict____()

    def __setstate__(self):
        return type(self).fromdict____(self.__dict__)

    # End of magic functions

    def getattr____(self, name):
        """Gets an attribute of self.

        Args:
            name: the name of the attribute

        Returns:
            value: the value of the attribute; or, a new DotDict object, if the attribute does not exist

        Raises:
            AttributeError: if self does not have the attribute
        """
        if name not in self.__dict__:
            raise AttributeError(f"self does not have the attribute: {name}")

        value = self.__dict__[name]
        return value

    def setattr____(self, name, value):
        """Sets an attribute of self.

        All python standard library dict values are converted to DotDict values recursively.

        Args:
            name: the name of the attribute
            value: the value of the attribute

        Returns:
            value: the value of the attribute
        """
        if isinstance(value, dict):
            value = DotDict.fromdict____(value)
        if not type(self).isprotected____(name):
            self.__dict__[name] = value
        value = self.__dict__[name]
        return value

    def getclassattr____(self, name):
        """Gets the value of the class attribute with a name.

        This will also set self.name to type(self).__dict__[name].

        Args:
            name: the name

        Returns:
            value: the value

        Raises:
            AttributeError: if type(self) does not have the attribute
        """
        classdict = type(self).__dict__

        if name not in classdict:
            raise AttributeError(f"type(self) does not have the attribute: {name}")

        value = classdict[name]
        self.setattr____(name, value)
        return value

    def setclassattr____(self, name, value):
        """Sets the class attribute with a name to a value.

        This will first set self.name to value and then set type(self).__dict__[name] to value.

        Args:
            name: the name
            value: the value

        Returns:
            value: the value
        """
        selftype = type(self)
        if isinstance(value, DotDict):
            value = value.todict____()
        if not selftype.isprotected____(name):
            self.setattr____(name, value)
            setattr(selftype, name, value)
        value = selftype.__dict__[name]
        return value

    def str____(self):
        """Finds and gives a string representation of self.

        Returns:
            result: the resulting string representation
        """
        result = ".{}"
        if len(self.__dict__) <= 0:
            return result

        result = ".{"
        for key in self.__dict__:
            result += f"{key.__str__()}: {self.__dict__[key].__str__()}, "

        result = result[:-2]  # Remove the trailing comma and space
        result += "}"

        return result

    def todict____(self):
        """Finds and gives a Python standard library dict version of self.

        All DotDict values are converted to Python standard library dict values recursively.

        Returns:
            result: the result dict
        """
        result = {}
        for key in self.__dict__:
            value = self.__dict__[key]
            if isinstance(value, DotDict):
                value = value.todict____()
            result[key] = value
        return result
