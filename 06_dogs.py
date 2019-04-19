#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Описать в виде класса собаку (Dog).
У него должны быть следующие свойства:
имя, дата рождения, голос

Создать 2-а экземпляра класса Dog со следующими параметрами
"Бобик", 1 января 2017, 'тяв-тяв'
"Тяпа", 2 января 2016, 'гав-гав'

Добавить возможность производить щенков следующим образом

puppy = boy_dog + girl_dog

Который в результате даёт:

puppy.voice()
# т.е. должно возвратить голоса М и Ж собак
>>> 'тяв-тяв гав-гав'

puppy.name()
>>> 'Щенок от собак Бобик и Тяпа'

puppy.birth_date()
# должно возвратить дату от рождения первой собаки родителя  + 480 дней.
"""

from datetime import datetime
from datetime import timedelta

class Dog:

    def __init__(self, name, birth_date, voice):

        self.name = name
        self.voice = voice
        self.birth_date = datetime(*birth_date)

class Puppy(Dog):

    def __init__(self, male, female):

        self.dad_name = male.name
        self.dad_voice = male.voice
        self.dad_birth_date = male.birth_date

        self.mom_name = female.name
        self.mom_voice = female.voice
        self.mom_birth_date = female.birth_date

    def voice(self):
        return '{voice1} {voice2}'.format(voice1=self.dad_voice, voice2=self.mom_voice)

    def name(self):
        return 'Щенок от собак {} и {}'.format(self.dad_name, self.mom_name)

    def birth_date(self):
        elder_dog = self.dad_birth_date

        if self.dad_birth_date < self.mom_birth_date:
            elder_dog = self.mom_birth_date

        return elder_dog + timedelta(days=480)

boy_dog = Dog('Бобик', [2017, 1, 1], 'тяф-тяф')
girl_dog = Dog('Тяпа', [2016, 1, 2], 'гав-гав')
puppy = Puppy(boy_dog, girl_dog)

if __name__ == '__main__':

    print(puppy.name())
    print(puppy.voice())
    print(puppy.birth_date())