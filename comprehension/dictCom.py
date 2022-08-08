square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num * num
print(square_dict)

# using dict comprehensions.
square_dict = {num: num * num for num in range(1, 11)}
print(square_dict)

# If Conditional Dictionary Comprehension
dict = {'pooja': 38, 'rahul': 48, 'jeck': 57, 'john': 33}

even_dict = {k: v for (k, v) in dict.items() if v % 2 == 0}
print(even_dict)

# Multiple if Conditional Dictionary Comprehension
dict = {'pooja': 38, 'rahul': 48, 'jeck': 57, 'john': 33}

new_dict = {k: v for (k, v) in dict.items() if v % 2 != 0 if v < 40}
print(new_dict)

# if -else Conditional Dictionary Comprehension
dict = {'pooja': 38, 'rahul': 48, 'jeck': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
              for (k, v) in dict.items()}
print(new_dict_1)
