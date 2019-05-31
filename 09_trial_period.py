"""
The class of a user with trial period is given. Every user has a 30 days in demo-mode.
We have to write the function that returns how many days remain. Timer starts now.

Create new user as the class object. User's name, surname and username are required:

>>> user = ChatUser("Thomas", "Anderson", "Neo", dt.date.today())

By default new user is active and has trial period:

>>> user.trial_lenght
datetime.timedelta(days=30)

You can check whether user has been created and whether his trial ends:

>>> user.created
datetime.date(2019, 5, 27)

>>> user.trial_ends_date
datetime.date(2019, 6, 26)

Function count_trial_days_left() is designed to check how many trial days left.
If there is no days left the account is disabling and the function returns 0:

>>> user.count_trial_days_left()
30

Another function called send_trial_ends_reminder() has to send message to user a reminder
before 1, 2 and 3 days before the trial is expired:

>>> send_trial_ends_reminder()
# TODO: complete function

# TODO: complete doc

"""

import datetime as dt

class ChatUser:
    def __init__(self, name, surname, username, created):
        self.name = name
        self.surname = surname
        sefl.username = username
        self.created = created
        self.active = True

        self.trial_lenght = dt.timedelta(days = 30)
        self.trial_ends_date = self.created + self.trial_lenght
        self.trial_days_left = self.trial_ends_date - dt.date.today()

        self.paid_days = 0
        self.paid_lenght = dt.timedelta(days = self.paid_days)
        self.paid_ends_date = self.trial_ends_date + self.paid_lenght
        self.paid_days_left = self.paid_ends_date - dt.date.today()

    def dasiable_unpaid_user(self):
        if self.trial_days_left.days <= 0 and self.paid_days_left.day  <= 0:
            self.active = False

    def send_trial_ends_reminder(self):
        if self.trial_days_left.days == any(range(1, 4)):
            message = "Ваш тестовый период заканчивается {}. Пожалуйста, оплатите подписку".format(self.trial_ends_date)
            pass

    def send_paid_ends_reminder(self):
        if self.paid_days_left.days == any(range(1, 4)):
            message = "Ваш оплаченный период заканчивается {}. Пожалуйста, пополните счёт".format(self.trial_ends_date)
            pass

    def count_trial_days_left(self):
        if self.trial_days_left.days <= 0:
            return 0
        else:
            return self.trial_days_left.days

    def count_paid_days_left(self):
        if self.paid_days_left.days <= 0:
            return 0
        else:
            return self.paid_days_left.days

if __name__ == '__main__':

    # Test cases from docstrings
    import doctest
    doctest.testmod()
