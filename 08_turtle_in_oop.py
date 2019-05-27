#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle
import time


class BeginFillCommand:

    def __init__(self, color):
        self.color = str(color)

    def draw(self):
        turtle.color(self.color)
        turtle.begin_fill()

class CircleCommand:

    def __init__(self, radius, extent, color):
        self.radius = float(radius)
        self.extent = float(extent)
        self.color = str(color)

    def draw(self):
        turtle.color(self.color)
        turtle.circle(self.radius, self.extent)

class EndFillCommand:

    def draw(self):
        turtle.end_fill()

class PenUpCommand:

    def draw(self):
        turtle.penup()

class GoToCommand:

    def __init__(self, x, y, width, color):
        self.x = float(x)
        self.y = float(y)
        self.width = float(width)
        self.color = str(color)

    def draw(self):
        turtle.color(self.color)
        turtle.width(self.width)
        turtle.goto(self.x, self.y)

class PenDownCommand:

    def draw(self):
        turtle.pendown()


if __name__ == '__main__':

    with open('./08_draw_commands_list.txt') as draw_file:

        for line in draw_file:

            line_list = line[:-1].split(',')
            command = line_list[0]
            args = line_list[1:]

            if command == 'beginfill':
                BeginFillCommand.draw(*args)

            if command == 'circle':
                CircleCommand.draw(*args)

            if command == 'endfill':
                EndFillCommand.draw()

            if command == 'penup':
                PenUpCommand.draw()

            if command == 'goto':
                GoToCommand.draw(*args)

            if command == 'pendown':
                PenDownCommand.draw()

        time.sleep(3)
