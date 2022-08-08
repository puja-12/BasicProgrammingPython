# Using Lambda functions inside List
letters = list(map(lambda x: x, 'human'))
print(letters)

# Conditionals in List Comprehension
# this program showing even numbers from 0 to 19
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

# Nested IF with List Comprehension
# it give output all even numbers which is divisible by 5 also
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

# if ...else With List Comprehension
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(11)]
print(obj)

# Nested Loops in List Comprehension
# Transpose of Matrix using Nested Loops

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

# Transpose of a Matrix using List Comprehension
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
transpose = [[row[i] for row in matrix] for i in range(4)]
print (transpose)