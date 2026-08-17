import numpy as np
import statistics
# String Format
string = 'Hello, world. Welcome Naif Natheer..'
print(string.format())

# Stripping Whitespace
print(string.strip())
print(string.lstrip())
print(string.rstrip())

# Changing character case
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.swapcase())

# Searching for substrings
print(string.find('Naif'))
print(string.rfind('Naif'))
print(string.index('Naif'))
print(string.count('l'))
print(string.startswith('H'))
print(string.endswith('.'))

if 'Naif' in string:
    print(string.index('Naif'))

if 'naif' not in string:
    print('Check the name')

# Replacing substrings
print(string.replace('Naif Natheer', "It's me naif"))

# Splitting and joining
print(string.split('naif'))
print(string.rsplit('naif'))
print(string.splitlines())
print(string.join('naif'))

# Character-testing methods
print(string.isalpha())
print(string.isdigit())
print(string.isalnum())
print(string.islower())
print(string.isupper())
print(string.istitle())
print(string.isspace())

# Raw string
print(r"naif natheer")

# numpy methods
array = np.array([1, 2, 3])
print(array.sum())
print(array.mean())
print(statistics.median(array))
print(array.max())
print(array.min())
print(array.std())
