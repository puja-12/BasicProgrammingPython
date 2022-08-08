def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
# result = map(lambda x: x + x, numbers)
print(list(result))

# 2
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

# 3
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))
# results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)

# 4
my_strings = ['a', 'b', 'c', 'd', 'e']

uppered_form = list(map(str.upper, my_strings))


print(uppered_form)


# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))