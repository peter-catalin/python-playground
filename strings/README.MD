# Strings

- Can be enclosed in single or double quotes.
- When working with the interactive intepreter, you need to use `print()` if you want escaped characters to be processed.
- If you don't want escaped characters to be interpreted you can use a raw string by prefixing the string with `r`. For example: `r'C:\some\name'`
- Strings in Python are inmutable.
- There is no char type in Python, a char is a string of lenght 1.
- Strings can be sliced using this syntax `word[start:end_not_included]`

## Multiline strings

Multiline strings can be created using triple quotes. For example:

```python
"""
This
is a
multiline
string.
"""

'''
This is also a
multiline string
'''

# This is a multiline string in which the first end-of-line character is not included
# End of line characters can be excluded using \ at the end of the line.
'''\
This is also a
multiline string
'''
```

## Concatenation

1. Can be done in several ways. By using `+` to "glue" strings together.
2. By using `*` to repeat the string several times.
3. By putting two string literals together.

```python
'Py' 'thon'
```
