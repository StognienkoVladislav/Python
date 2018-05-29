import operator


xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

print(sorted(xs.items()))
print(sorted(xs.items(), key=lambda x: x[1]))
print(sorted(xs.items(), key =operator.itemgetter(1)))
print(sorted(xs.items(), key=lambda x: abs(x[1])))
print(sorted(xs.items(),
             key=lambda x: x[1],
             reverse=True))
