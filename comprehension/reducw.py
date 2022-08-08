import functools

lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# 2
tupl = (1, 4, 8, 18, 22)

# using reduce with initializer = 3
print(functools.reduce(lambda x, y: x + y, tupl, 3))


# 3 factorial
def mult(x, y):
    return x * y


fact = functools.reduce(mult, range(1, 4))
print('Factorial of 3: ', fact)
