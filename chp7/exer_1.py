#! /usr/bin/env python
# coding: utf-8
# exer_1.py
# 2020-03-14
#

# Write a program able to draw a circle positioned at the center of the canvas. Its size should react to a parameter 'factor' between 0 and 1:
#  - if 0, the diameter should be a quarter of the canvas height
#  - if 1, the diameter should be three-quarters of the canvas height
#  - anything in between should smoothly interpolate
# Define also a variable 'switch' pointing to a boolean value. A True value should create a black circle on a white background, otherwise the opposite.

Variable([
    dict(name='factor', ui='Slider',
         args=dict(
             value=0,
             minValue=0,
             maxValue=1
         )),
     dict(name='switch', ui='CheckBox')
], globals())

CANVAS = 200

black = (0, 0, 0)
white = (1, 1, 1)

size(CANVAS, CANVAS)

if switch:
    background = white
    foreground = black
else:
    background = black
    foreground = white

fill(*background)
stroke(*background)
rect(0, 0, CANVAS, CANVAS)

d = CANVAS / 4 + (3 * CANVAS / 4 - CANVAS / 4) * factor
r = d / 2

fill(*foreground)
stroke(*foreground)
oval(CANVAS / 2 - r, CANVAS / 2 - r, d, d)