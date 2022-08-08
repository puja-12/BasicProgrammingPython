def check_year(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0);


# Driver Code
if __name__ == "__main__":
    year = 2004
    if check_year(year):
        print("Leap Year")
    else:
        print("Not a Leap Year")