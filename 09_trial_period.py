"""
The class of a user with trial period is given. Every user has a 30 days in demo-mode.
We have to write the function that returns how many days remain. Timer starts now.

Create new user as the class object. User's name, surname and username are required:
>>> user = ChatUser("Thomas", "Anderson", "Neo", dt.date.today())

By default new user is active and has trial period:
>>> user.trial_lenght
datetime.timedelta(days=30)

The user has paid period either. By default it's 0
so you can just add here days the user charged following his plan:
>>> user.paid_days
0

You can check whether user has been created and whether his trial or paid period ends:
>>> user.created
datetime.date(2019, 5, 31)
>>> user.trial_ends_date
datetime.date(2019, 6, 30)
>>> user.paid_ends_date
datetime.date(2019, 6, 30)

Function count_trial_days_left() is designed to check how many trial days left.
If there is no days left the account is disabling and the function returns 0:
>>> user.count_trial_days_left()
30

count_paid_days_left() works the same way:
>>> user.count_paid_days_left()
0

Another functions called send_trial_ends_reminder() and send_paid_ends_reminder().
It has to send message to user 1, 2 and 3 days before the trial is expired:
>>> user.send_trial_ends_reminder()
>>> user.send_paid_ends_reminder()

After all, function disable_unpaid_user() is here to disable an account:
>>> user.disable_unpaid_user()

"""

import datetime as dt

class ChatUser:
    def __init__(self, name, surname, username, created):
        self.name = name
        self.surname = surname
        self.username = username
        self.created = created
        self.active = True

        self.trial_lenght = dt.timedelta(days = 30)
        self.trial_ends_date = self.created + self.trial_lenght
        self.trial_days_left = self.trial_ends_date - dt.date.today()

        self.paid_days = 0
        self.paid_lenght = dt.timedelta(days = self.paid_days)
        self.paid_ends_date = self.trial_ends_date + self.paid_lenght
        self.paid_days_left = self.paid_ends_date - dt.timedelta(days = self.count_trial_days_left()) - dt.date.today()

    def disable_unpaid_user(self):
        if self.trial_days_left.days <= 0 and self.paid_days_left.day  <= 0:
            self.active = False

    def send_trial_ends_reminder(self):
<<<<<<< HEAD
        if self.trial_days_left.days in range(1,4):
=======
        if self.trial_days_left.days == any([x for x in range(1,4)]):
>>>>>>> 423adc8ef8076b542f3497cab28a531843576b8e
            message = "Ваш тестовый период заканчивается {}. Пожалуйста, оплатите подписку".format(self.trial_ends_date)
            # TODO: complete function with email sending

    def send_paid_ends_reminder(self):
<<<<<<< HEAD
        if self.paid_days_left.days in range(1,4):
=======
        if self.paid_days_left.days == any([x for x in range(1,4)]):
>>>>>>> 423adc8ef8076b542f3497cab28a531843576b8e
            message = "Ваш оплаченный период заканчивается {}. Пожалуйста, пополните счёт".format(self.paid_ends_date)
            # TODO: complete function with email sending

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
