"""
The class of a user with trial period is given. Every user has a 30 days in demo-mode.
We have to write the function that returns how many days remain. Timer starts now.

>>> user = ChatUser(dt.date.today())

>>> user.trial
datetime.timedelta(days=30)

>>> user.created
datetime.date(2019, 5, 27)

>>> user.trial_days_left()
26

If trial is expired the function returns 0.
"""

import datetime as dt

class ChatUser:
    def __init__(self, created):
        self.created = created
        self.trial = dt.timedelta(days = 30)

    def trial_days_left(self):
        self.end = self.created + self.trial

        if self.end.day <= 0:
            return 0
        else:
            return self.end.day

if __name__ == '__main__':

    # Test cases from docstrings
    import doctest
    doctest.testmod()
