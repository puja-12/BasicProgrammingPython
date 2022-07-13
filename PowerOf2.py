import math


def isPowerOfTwo(n):
    if (n == 0):
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2

    return True


# Driver Code
if __name__ == "__main__":

    if isPowerOfTwo(31):
        print("Yes");
    else:
        print("No");

    if isPowerOfTwo(64):
        print("Yes");
    else:
        print("No");