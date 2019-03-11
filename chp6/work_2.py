#! /usr/bin/env python
# coding: utf-8
# work_2.py
# 2019-03-11
#
# Extend the previous exercise. Nest two while statements and draw a pattern made of squares across the entire canvas. Try to get a chessboard effect.

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

x = y = 0
i = 1

while y < CANVAS:    
    j = i
    while x < CANVAS:
        if j % 2 == 0:
            fill(0.2)
        else:
            fill(0.8)
        rect(x, y, square, square)
        x += square
        j += 1

    x = 0
    y += square
    i += 1
