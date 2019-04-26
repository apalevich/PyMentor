#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle
import time

class GoToDraw:
    def __init__(self, x, y, width=1, color='black'):
        self.x = float(x.strip())
        self.y = float(y.strip())
        self.width = float(width.strip())
        self.color = color

    # def draw(self, turtle):
    #     turtle.width = self.width
    #     turtle.color = self.color

    def draw(self, action):
        if self.action == 'beginfill':
            turtle.color(self.color)
            turtle.begin_fill()

        if self.action == 'circle':
            turtle.color(self.color)
            turtle.circle(self.x, self.y)

        if self.action == 'endfill':
            turtle.end_fill()

        if self.action == 'penup':
            turtle.penup()

        if self.action == 'goto':
            turtle.color(self.color)
            turtle.width(self.width)

        if self.action == 'pendown':
            turtle.pendown()

with open('./draw.txt') as draw_file:

    for line in draw_file:

        line_list = line[:-1].split(',')
        a,b,c,d,e = *line_list
        action = GoToDraw()

        action.draw(line_list[0])

    time.sleep(3)
