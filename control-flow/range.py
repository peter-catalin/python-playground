################################################################
# Range examples
################################################################
print("Range 0 to 4 incrementing by 1")
for i in range(5):
    print(i)
print("\n")

print("Range 0 to 10 incrementing by 2")
for i in range(0, 11, 2):
    print(i)
print("\n")

# What happens if in one of the we go above the stop parameter?
# A step of 3 will generate: 0, 3, 6, 9, 12, 15 ...
# The stop is 12 non inclusive, therefore I should not be included.
print("Does the stop parameter include the last element?")
for i in range(0, 12, 3):
    print(i)
if (i == 9):
    print('Your assumption is correct!\n')
else:
    print('You were wrong\n')

################################################################
# Looping over lists
################################################################

# Basic loop
names = ['Mark', 'Lisa', 'Filip', 'Ana']
for name in names:
    print('Hello', name)
print('\n')

print('Looping over indexes with range(len(x)')
for index in range(len(names)):
    print(f'At index {index} we have name {names[index]}')
print('\n')

print('Looping over indexes with enumerate(x)')
for index, value in enumerate(names):
    print(f'At index {index} we have name {value}')
print('\n')