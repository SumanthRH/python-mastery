
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