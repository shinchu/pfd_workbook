#! /usr/bin/env python
# coding: utf-8
# exer_6.py
# 2019-02-26
#
# canvas 100x100 combine the circles and the squares exercises, draw the four squares below the four ovals

canvas = 100
diff = 10
rect_x = 25
rect_y = 25
d = 20

oval_x = 55
oval_y = 45

newPage(canvas, canvas)

stroke(0)
fill(1)
rect(rect_x, rect_y, d, d)
fill(0.75)
rect(rect_x+1*diff, rect_y+1*diff, d, d)
fill(0.5)
rect(rect_x+2*diff, rect_y+2*diff, d, d)
rect(rect_x+3*diff, rect_y+3*diff, d, d)

fill(0)
oval(oval_x, oval_y, d, d)
fill(0.25)
oval(oval_x-1*diff, oval_y-1*diff, d, d)
fill(0.5)
oval(oval_x-2*diff, oval_y-2*diff, d, d)
fill(0.75)
oval(oval_x-3*diff, oval_y-3*diff, d, d)