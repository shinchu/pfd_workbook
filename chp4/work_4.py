#! /usr/bin/env python
# coding: utf-8
# work_4.py
# 2019-02-26
#
# Draw four circles vertically aligned in the middle of a canvas. The shapes should be equally spread out. A variable "radius" controls the size of each circle. The color of each shape should be calculated according to its horizontal position in the canvas: left darker, right lighter.

Variable([
    dict(name='radius', ui='Slider',
         args=dict(
             value=1,
             minValue=1,
             maxValue=10
         )),
    dict(name='n', ui='Slider',
         args=dict(
             value=4,
             minValue=1,
             maxValue=10,
             tickMarkCount=10,
             stopOnTickMarks=True
         ))
], globals())

canvas = 100
n = int(n)
block = canvas / (n + 1)
y = (canvas - radius) / 2

newPage(canvas, canvas)

for i in range(n):
    x = (i + 1) * block - radius / 2
    fill(x / canvas)
    oval(x, y, radius, radius)
