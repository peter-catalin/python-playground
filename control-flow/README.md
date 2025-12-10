# Control flow

## If statements

```python
if x < 0:
    print('x is negative')
elif x == 0:
    print('x is zero')
else:
    print('x is positive')
```

Python does not have a switch statement, however, it has something way more powerful: structural pattern matching.

```python
match value:
    case {"type": "user", "id": uid, "name": name}:
        print(uid, name)
    case [x, y, z]:
        print("a list of 3 elements")
    case _:
        print("default")
```

## Loops

### While

```python
a = 0
while (a < 10):
    print(a)
    a += 1
```

Python does not have a do while construct like Java, C or JavaScript.

### For

As opposed to other languages, Python does not have the `for (int i = 0; i++; i < 10)` kind
of syntax. Instead, you always use `for w in something_iterable`. For example:

```python
for letter in ['a' , 'b', 'c']:
    print(letter)
```

If you need an arithmentic progression you can use the `range` function.

The range function can be called in the following three ways:

```python
# By passing only the stop argument.
range(stop)

# By passing only the start and stop arguments.
range(start, stop)

# By passing all the arguments.
range(start, stop, step)
```

Here are some examples:

```python
for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)

for i in range(2, 5, 2):
    print(i)
```

For and while loops can have an else clause in Python that only gets executed if the loop DID NOT get broken.

Here's an example:

```python
names = ['Mark', 'Lisa', 'Filip', 'Ana']
for name in names:
    if (name == 'Mike'):
        break
    print(name)
else:
    print('No Mike found')
```

### `break`, `continue`, `pass`

- `break`: breaks the whole loop.
- `continue`: skips the current iteration and goes to the next one.
- `pass`: does nothing, it is used as a placeholder. For example, you want to define a function that does nothing (for now).

