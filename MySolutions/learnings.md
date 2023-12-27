
- Exercise 2.1: Reading data as a single string vs. reading data with f.readlines() has a huge difference in memory consumption - 10 MB vs 40 MB for an example file. 
Point to ponder: what might be the source of that extra overhead?
    - > My guess is the additional information stored in a list data structure. 

- Memory efficiency:
    - Class with `__slots__` < Tuple < Namedtuple < Class < Dict

- A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. It is often much faster than creating a new dictionary and running multiple update() calls.

- `zip(list1, list2)` Truncates to shortest input length
