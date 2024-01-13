
# Learnings
These are some notes and comments I've taken while going through the book. Many sentences here are copied verbatim from David's slides since I found them to be great summaries for different concepts.

- Exercise 2.1: Reading data as a single string vs. reading data with f.readlines() has a huge difference in memory consumption - 10 MB vs 40 MB for an example file. 
Point to ponder: what might be the source of that extra overhead?
    - > My guess is the additional information stored in a list data structure. 

- Memory efficiency:
    - Class with `__slots__` < Tuple < Namedtuple < Class < Dict

- A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. It is often much faster than creating a new dictionary and running multiple update() calls.

- `zip(list1, list2)` Truncates to shortest input length

- Generators summarized in a line: Generators are useful in contexts where the result is an intermediate step

- You can directly pass in generators in function arguments:
    ```
    sum(x*x for x in nums)
    ```
- Generator expressions can save a LOT of memory. Key idea is that if you're dealing with map and reduce like operations on your data, you can chain operations on generator expressions and then actually materialize results one by one when you do a reduce op like sum(), max(), etc. See ex 2.3 for details - memory usage here goes from ~ 200 MB to ~ 120 KB.

- Use the `dis` library in python to peek into low level byte code. For example, use `dis.dis(f)` to get the byte code for a function `f`

- Builtin types operate according to
predefined "protocols" - the name for the special methods like `__add__` and `__len__`. Object protocols are baked into the interpreter as low-level bytecode 

- Container objects only hold references
(pointers) to their stored values. All operations involving the container internals only manipulate the pointers (not the objects)

    ![container](container.png)

- All "hashable" objects in python have a `__hash__()` and `__eq__()` method

- Assignment operations never make a copy of the value being assigned - all assignments are merely reference copies

- Immutable values can be safely shared, which can save a lot of memory (think a long list of dictionaries)

- `copy.deepcopy` is the only safe way to copy an object in python

## Classes 

- Object oriented programming is largely
concerned with the modeling of "behavior." 

- A class is a simply a set of functions that do different things on "instances"

- Classes do not define a scope. If want to operate on an instance, you always have to refer to it explicitly

- There are only three operations on an instance: 
```
obj.attr # Get an attribute
obj.attr = value # Set an attribute
del obj.attr # Delete an attribute - obj.attr no longer exists
```
- Method calls are layered onto the machinery used for simple attributes.
```
s.get_something # Looks up the method
s.get_something() # looks up and calls the method
```

- Internally, a method call `s.method()` is implemented as `s.method.__func__(s.method.__self__)`

- Class variables: can be accessed at the class level or by an instance. Can also be changed via inheritance.

- Class Method is a method that operates on the class itself. It's invoked on the class, not an instance. Example usecase is in providing alternate constructors. Most popular example of this is `AutoModel.from_pretrained` in 🤗Transformers.

- Implicit conversion of data in `__init__()` can limit flexibility and might introduce weird bugs if a user isn't paying careful attention.

## Python Encapsulation
- Python has programming conventions to indicate the intended use of something. Ex. private and public methods aren't exactly enforced like in C++.
- Attributes with a single underscore "_" are meant to act as private attributes (still accessible in instanecs and for subclasses)
- Attributes with a double underscore "__" have a special meaning - these are not accessible to subclasses. They are acessible in instance via Python's name mangling trick Ex:
```
s = MyClass()
s._MyClass__attr # to get __attr
```
- Properties in python: Useful alternative to accessor methods. Can also make sure a property is not stale/ computed when accessed. Note that a property is a _class variable_.
- Property decorators:
    - @property: to declare a property
    - @<\pname>.setter: function that's invoked with assignment ops. Needed to modify a property
    - @<\pname>.deleter: function that's invoked with deletion

- Advice on `__slots__`:  Do not use it except with classes that are simply going to serve as simple data
structures.

- Inheritance in a nutshell: Extend existing code. That's it.
    - `__init__` inheritance: you must also initialize the parents with `super().__init__()`
    - objects defined via inheritance are a special version of the parent i.e same capabilities
    - `object` is a parent of all classes in Python 3 (even if not specified)
- Objects have two string representations:
    - str(obj) - printable output
    - repr(obj) - for programmers
    - The convention for `__repr__` is to return a string that, when fed to `eval()` , will recreate the underlying object.
- Item access: `__setitem__`, `__getitem__`, `__delitem__`, `__contains__`, `__len__`

- Instances under the hood:

```
d = Date.__new__(Date, 2012, 12, 21)
d.__init__(2012, 12, 21)
```
