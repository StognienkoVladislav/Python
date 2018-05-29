
def integers():
    for i in range(1, 9):
        yield i


def squared(seq):
    for i in seq:
        yield i*i


def negated(seq):
    for i in seq:
        yield -i


chain = integers()
print(list(chain))

chain = squared(integers())
print(list(chain))

print(list(negated(squared(integers()))))
