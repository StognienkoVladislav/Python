
iterator = ('Hello' for i in range(3))
for x in iterator:
    print(x)


listcomp = ['Hello' for j in range(3)]
genexpr = ('Hello' for k in range(3))

print(listcomp, genexpr)

# Filtering Values
even_squares = (x * x for x in range(10)
                if x % 2 == 0)

for x in even_squares:
    print(x)


# In-line generator expressions
for x in ('Bom dia' for l in range(3)):
    print(x)

