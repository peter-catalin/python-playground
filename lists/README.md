# Lists

Are defined like this:

```python
squares = [1, 4, 9, 16, 25]
```

They can contain elements of different types but usually it is not the case.

They are mutable.

They can be accessed by indexed and sliced with the same syntax as the strings.

We can even assign to slices, which can be really handy. Check
out this example from the [official documentation](https://docs.python.org/3/tutorial/introduction.html#lists):

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

# replace some values
letters[2:5] = ['C', 'D', 'E']
letters

# now remove them
letters[2:5] = []
letters

# clear the list by replacing all the elements with an empty list
letters[:] = []
letters
```
