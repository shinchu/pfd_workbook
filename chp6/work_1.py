#! /usr/bin/env python
# coding: utf-8
# work_1.py
# 2019-03-11

# Create a 200x200pt canvas. Draw a sequence of squares from top to bottom using a while loop. The square side should be adjustable through a variable. Odd squares should be light gray, even tiles should be dark gray.

Variable([
    dict(name='square', ui='Slider',
         args=dict(
             value=10,
             minValue=1,
             maxValue=200
         ))
], globals())

CANVAS = 200

newPage(CANVAS, CANVAS)

y = 0
i = 1
while y < CANVAS:
    if i % 2 == 0:
        fill(0.2)
    else:
        fill(0.8)
    rect(0, y, square, square)
    y += square
    i += 1

