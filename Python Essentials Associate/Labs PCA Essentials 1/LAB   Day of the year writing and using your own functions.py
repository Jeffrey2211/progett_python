def is_year_leap(year):
       return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2:
        return 29 if is_year_leap(year) else 28

    return month_lengths[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None

    days_in_current_month = days_in_month(year, month)
    if day < 1 or day > days_in_current_month:
        return None

    days_so_far = 0
    for m in range(1, month):
        days_so_far += days_in_month(year, m)
    
    days_so_far += day
    return days_so_far


print(day_of_year(2000, 12, 31))
