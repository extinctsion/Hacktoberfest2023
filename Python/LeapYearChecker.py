# year to be checked
year = 1900
leap = False

# if the year is divided by 4
if year % 4 == 0:

    # if the year is century
    if year % 100 == 0:

        # if year is divided by 400
        # then it is a leap year
        if year % 400 == 0:
            leap = True
        else:
            leap = False

    # if the year is not century
    else:
        leap = True

else:
    leap = False

if leap:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
