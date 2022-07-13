import math


def WC(temp, windsp):
    # Calculating Wind Chill Index (Twc)
    wci = 13.12 + 0.6215 * temp - 11.37 * math.pow(windsp, 0.16) + \
          0.3965 * temp * math.pow(windsp, 0.16)
    return wci


if __name__ == "__main__":
    # Taking the Air Temperature (Ta)
    temp = 42

    # Taking the Wind Speed (v)
    windsp = 150

    print("The Wind Chill Index is", int(round(WC(temp, windsp))))