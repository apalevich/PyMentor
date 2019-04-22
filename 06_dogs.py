#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercise with classes and objects.

We create class Dog so we can use create objects-dogs:

>>> bob = Dog('Bob')
>>> print(bob.name)
Bob

Using arguments we can give it not only name but date of birth (as an list) and example of voice:

>>> snatch = Dog('Snatch', [2017, 4, 12], 'Wuf wuf')
>>> print(snatch.birth_date)
[2017, 4, 12]

You can use object methods as well by adding 'get_' before:
>>> print(snatch.get_voice())
Wuf wuf

One more thing: ability to create puppies by summarizing dogs:

>>> puppy = bob + snatch
>>> print(puppy.get_birth_date())
1971-04-26 00:00:00

"""

from datetime import datetime
from datetime import timedelta


class Dog:

    def __init__(self, name='Имя', birth_date = [1970, 1, 1], voice='Голос'):

        self.name = name
        self.voice = voice
        self.birth_date = birth_date

    def __add__(self, other):

        birth_date = self.birth_date
        if self.birth_date > other.birth_date:
            birth_date = other.birth_date
        voice = '{voice1} {voice2}'.format(voice1=self.voice, voice2=other.voice)
        name = 'Щенок от собак {} и {}'.format(self.name, other.name)
        return Dog(name, birth_date, voice)

    def get_voice(self):
        return self.voice

    def get_name(self):
        return self.name

    def get_birth_date(self):

        if 'Щенок от собак' in self.name:
            return datetime(*self.birth_date) + timedelta(days=480)
        else:
            return datetime(*self.birth_date)

boy_dog = Dog('Бобик', [2017, 1, 1], 'тяф-тяф')
girl_dog = Dog('Тяпа', [2016, 1, 2], 'гав-гав')
puppy = boy_dog + girl_dog

if __name__ == '__main__':

    # Test cases from docstrings
    import doctest
    doctest.testmod()
