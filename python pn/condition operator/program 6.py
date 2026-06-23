year = int(input("enter a number"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print (f"{year} is a leap year.")
else:
    print (f"{year} is not a leap year.")

#4 se divisible and not 100 se divisible or 400 se divisible?