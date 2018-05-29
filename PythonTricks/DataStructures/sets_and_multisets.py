from collections import Counter


vowels = {'a', 'e', 'i', 'o', 'u'}
squares = {x * x for x in range(10)}

# Set

print('e' in vowels)

letters = set('alice')
print(letters.intersection(vowels))


vowels.add('x')
print(len(vowels))

# frozenset - Immutable Set
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# vowels.add('p')

d = {frozenset({1, 2, 3}): 'hello'}
print(d[frozenset({1, 2, 3})])

inventory = Counter()

loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(inventory)

more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
print(inventory)

# Unique elements
print(len(inventory))

# Total no. elements
print(sum(inventory.values()))
