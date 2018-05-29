
squares = [x for x in range(10)]

print(squares)

# Same
squares = []
for x in range(10):
    squares.append(x)


even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)

# Same
even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x * x)


print({x * x for x in range(-9, 10)})

print({x: x*x for x in range(5)})

