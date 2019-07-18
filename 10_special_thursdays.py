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

def special_thursdays(year: int) -> list:
    pass

if __name__ == '__main__':

    # Test cases from docstrings
    import doctest
    doctest.testmod()
