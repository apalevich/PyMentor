"""
Function takes a year on input and returns every 3th of thursdays for months:
* March
* June
* September
* December

The return is a list containing datetime.date() objects:

>>> special_thursdays(2019)
[datetime.date(2019, 3, 21), datetime.date(2019, 6, 20), datetime.date(2019, 9, 19), datetime.date(2019, 12, 19)]

"""

import datetime

def special_thursdays(year: int) -> list:
    # Create list with required months and one for adding days
    months = [3, 6, 9, 12]
    days_list = []

    # Check weekdays in a loop until we find Thursday
    # starting from 15st day (1st day of 3th week)
    for month in months:
        for day in range(15, 23):
            current_date = datetime.date(int(year), month, day)
            if current_date.weekday() == 3:
                days_list.append(current_date)
                break

    return days_list

if __name__ == '__main__':

    # Test cases from docstrings
    import doctest
    doctest.testmod()
