import datetime


def print_extra_day(yr):
    extra_date = datetime.date(yr, 2, 29)
    print(extra_date.strftime('%A'))


def find_leap_year(yr):
    if (yr % 4) == 0:
        if (yr % 100) == 0:
            if (yr % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Enter a year: "))
isLeap = find_leap_year(year)

if isLeap:
    print_extra_day(year)
else:
    print("This is not a leap year")
    while not isLeap:
        year = year - 1
        isLeap = find_leap_year(year)
    print("Closest leap year: {}".format(year))
    print_extra_day(year)
