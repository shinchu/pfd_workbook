#! /usr/bin/env python
# coding: utf-8
# work_1.py
# 2019-02-26
#
# Your goal is to draw a black rectangle positioned in the middle of the canvas. Its height is equal to the height of the canvas. The rectangle’s width instead changes according to a variable "factor" between 0 and 1:

# if 0, the rectangle's width is equal to 0
# if 1, the rectangle's width is equal to the canvas width

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
width = canvas * factor

newPage(canvas, canvas)
rect((canvas-width)/2, 0, width, height)