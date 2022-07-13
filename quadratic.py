import math


def findRoots(a, b, c):
    sqrt = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(sqrt))

    if sqrt > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif sqrt == 0:
        print(" real and same roots")
        print(-b / (2 * a))


    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


if __name__ == "__main__":
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    c = int(input('Enter c:'))

    if a == 0:
        print("Input correct quadratic equation")

    else:
        findRoots(a, b, c)
