def nthHarmonic(N):
    # H1 = 1
    harmonic = 1.00

    for i in range(2, N + 1):
        harmonic += 1 / i

    return harmonic


# Driver code
if __name__ == "__main__":
    N = 8
    print(round(nthHarmonic(N), 5))