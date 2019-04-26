#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as t
import time

def create_drawing():

    with open('./draw.txt', 'r') as draw_file:

        for line in draw_file:

            line_list = line[:-1].split(',')

            # Create commands and arguments
            command = line_list[0]
            if len(line_list) > 1 and line_list[1].strip().isdigit():
                x = float(line_list[1])
            if len(line_list) > 2 and line_list[2].strip().isdigit():
                y = float(line_list[2])
            if len(line_list) > 3 and line_list[3].strip().isdigit():
                width = float(line_list[3])
            if len(line_list) > 1 and line_list[-1].strip().isalpha():
                color = line_list[-1].strip()

            # catch a command and run it
            if command == 'beginfill':
                t.color(color)
                t.begin_fill()

            if command == 'circle':
                t.color(color)
                t.circle(x, y)

            if command == 'endfill':
                t.end_fill()

            if command == 'penup':
                t.penup()

            if command == 'goto':
                t.color(color)
                t.width(width)

            if command == 'pendown':
                t.pendown()

        time.sleep(3)



if __name__ == '__main__':
    create_drawing()
