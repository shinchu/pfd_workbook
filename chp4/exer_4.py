#! /usr/bin/env python
# coding: utf-8
# exer_4.py
# 2019-02-26

# canvas 100x100 draw a zig zag connected polyline starting from top left corner and ending in bottom right corner of the canvas

canvas = 100
point1 = (20, 50)
point2 = (70, 70)
point3 = (50, 20)

newPage(canvas, canvas)
stroke(0)
line((0, canvas), point1)
line(point1, point2)
line(point2, point3)
line(point3, (canvas, 0))