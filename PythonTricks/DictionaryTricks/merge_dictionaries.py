

xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}


zs = {}
zs.update(xs)
zs.update(ys)

zs = dict(xs, **ys)
zs_2 = {**xs, **ys}

