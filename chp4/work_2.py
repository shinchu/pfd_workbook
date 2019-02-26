#! /usr/bin/env python
# coding: utf-8
# work_2.py
# 2019-02-26

#Draw two rectangles, one leaning on the left side of the canvas, the other leaning on the right side. Their heights are equal to the canvas. Instead, each rectangle width is controlled by a variable "factor" between 0 and 1. When "factor":
# is 0, you see no rectangle
# is 1, you cannot see the white canvas background


Variable([
    dict(name='factor', ui='Slider',
         args=dict(
             value=0,
             minValue=0,
             maxValue=1
         ))
], globals())

canvas = 100
height = canvas
width = factor * (canvas / 2)

newPage(canvas, canvas)
rect(0, 0, width, height)
rect(canvas-width, 0, width, height)