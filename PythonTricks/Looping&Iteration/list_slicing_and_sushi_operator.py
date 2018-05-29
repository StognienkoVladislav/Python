

lst = [1, 2, 3, 4, 5]
print(lst)

# lst[start:end:step]
print(lst[1:3:1])
print(lst[1:3])
print(lst[::2])
print(lst[::-1])

original_lst = lst
lst[:] = [7, 8, 9]
print(lst, original_lst)
print(original_lst is lst)

# copy
copied_lst = lst[:]
print(copied_lst)
print(copied_lst is lst)

