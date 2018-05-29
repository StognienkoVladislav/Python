import array


arr = ['one', 'two', 'three']
print(arr[0])
print(arr)

# Lists are mutable:
arr[1] = 'hello'
print(arr)

del arr[1]
print(arr)

# Lists can hold arbitrary data types:
arr.append(23)
print(arr)


# Tuple - immutable containers
arr = 'one', 'two', 'three'
print(arr[0])
print(arr)

# arr[1] = 'hello'
# del arr[1]

# Tuples can hold arbitrary data types:
# Adding elements creates a copy of the tuple
print(arr + (23,))

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])

arr[1] = 23.9
print(arr)

del arr[1]
arr.append(42.94)

# Arrays are "typed"
# arr[1] = 'hello'

# STR
arr = 'abcd'
# string are immutable
print(list('abcd'))


# bytes - immutable Arrays of Single Bytes
arr_b = bytes((0, 1, 2, 3))
print(arr_b)
# arr[1] = 23
# del arr[1]

