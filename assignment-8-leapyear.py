while True:
    year = int(input("Please enter a 4-digit year to check for a leap year:"))

    leap_year = year%4==0 and (year%100!=0 or year%400==0)
    
    if leap_year:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")