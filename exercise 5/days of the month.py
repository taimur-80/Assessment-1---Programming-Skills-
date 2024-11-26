def get_days_in_month(month, year):
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if 1   not in days_in_month:
        return "Invalid month"

    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

    return days_in_month[month]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

month = int(input("Enter the month number (1-12): "))
year = int(input("Enter the year: "))

days = get_days_in_month(month, year)

print(f"There are {days} days in month {month} of year {year}.")