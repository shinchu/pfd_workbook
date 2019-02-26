#! /usr/bin/env python
# coding: utf-8
# work_5.py
# 2019-02-26

# Draw two crosses, a dark gray "plus" shape, and a light gray "multiply" shape. The variable "factor" controls the thickness of the crosses:
# if 0, the thickness is 2pt
# if 1, the thickness is 30pt


Variable([
    dict(name='factor', ui='Slider',
         args=dict(
             value=0,
             minValue=0,
             maxValue=1
         ))
], globals())

canvas = 100
min = 2
max = 30

newPage(canvas, canvas)
strokeWidth(min + (max-min)*factor)

stroke(0.2)
line((canvas/2, 0), (canvas/2, canvas))
line((0, canvas/2), (canvas, canvas/2))

stroke(0.8)
line((0, 0), (canvas, canvas))
line((0, canvas), (canvas, 0))