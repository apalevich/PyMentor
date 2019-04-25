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
"""
import turtle
import time

def create_drawing():
    with open('./draw.txt', 'r') as draw_file:

        for line in draw_file:
            line_list = line.split(',')

            for index, element in enumerate(line_list):
                if element[-1].isdigit():
                    line_list[index] = int(element)

            if len(line_list) > 1:

                if line_list[-1].isalpha():
                    exec(f'turtle.color("{line_list[-1]}")')

                if 'beginfill' in line_list[0]:
                    turtle.begin_fill()
                if 'circle' in line_list:
                    exec(f'turtle.circle({line_list[1]},{line_list[2]})')
                if 'goto' in line_list[0]:
                    turtle.pensize(int(line_list[-2]))
                    turtle.goto(line_list[1], line_list[2])

            else:
                if 'pendown' in line_list[0]:
                    turtle.pendown()
                if 'penup' in line[0]:
                    turtle.penup()
                if 'endfill' in line_list[0]:
                    turtle.end_fill()

        time.sleep(10)


if __name__ == '__main__':
    create_drawing()
