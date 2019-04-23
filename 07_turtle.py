#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поместить следующий набор команд текстовый файл draw.txt

beginfill, black
circle, 20, 1, black
endfill
penup
goto, 120, 0, 1, black
pendown
beginfill, black
circle, 20, 1, black
endfill
penup
goto, 150, 40, 1,
pendown
beginfill, yellow
goto, -30, 40, 1,black
goto, -30, 70, 1,black
goto, 60, 70, 1, black
goto, 60, 100, 1, black
goto, 90, 100, 1, black
goto, 115, 70, 1, black
goto, 150, 70, 1, black
goto, 150, 40, 1, black
endfill
Каждое первое слово в новой строке этого файла соответствует методу из класса Turtle.
А после запятой идут его параметры(если есть).

Использую модуль черепашка

>>>import turtle
нужно прочитав команды из файла нарисовать движения "черепашки" на экране.
"""
