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
import turtle

with open('./draw.txt', 'r') as draw_file:

    for line in draw_file:
        line_list = line.split(',')
        if len(line_list) > 1:

            if line_list[-1].isalpha():
                exec(f'turtle.color("{line_list[-1]}")')

            if beginfill in line_list[0]:
                turtle.begin_fill()
            if endfill in line_list[0]:
                turtle.end_fill()
            if circle in line_list:
                exec('turtle.circle({line_list[1]},{line_list[2]})')
            

        else:
            command = 'turtle.' + line_list[0]

        exec(command)
