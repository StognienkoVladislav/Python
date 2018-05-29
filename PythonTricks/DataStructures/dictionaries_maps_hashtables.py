import collections
from collections import defaultdict, ChainMap
from types import MappingProxyType


# Dict
phonebook = {
    'bob': 7387,
    'alice': 3719,
    'jack': 7052,
}

squares = {x: x * x for x in range(6)}
print(phonebook['alice'])
print(squares)

# collections.OrderedDict

d = collections.OrderedDict(one=1, two=2, three=3)
print(d)

d['four'] = 4
print(d)
print(d.keys())

# collections.defaultdict
dd = defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')
print(dd['dogs'])


# ChainMap
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)
print(chain)

# MappingProxyType
writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

# The proxy is read-only
print(read_only['one'])
# read_only['one'] = 23
writable['one'] = 42
print(read_only)
