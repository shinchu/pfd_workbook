#! /usr/bin/env python
# coding: utf-8
# work_3.py
# 2019-02-26

# Draw four triangles. Fill each triangle with a different shade of gray. Also, each triangle should have two vertices matching to contiguous canvas corners and the last vertex positioned in the middle of the canvas.

canvas = 100
acolor = 0
diff = 1/4

bottom_left = (0, 0)
top_left = (0, canvas)
top_right = (canvas, canvas)
bottom_right = (canvas, 0)
center = (canvas/2, canvas/2)

newPage(canvas, canvas)
stroke(None)
fill(acolor)
polygon(top_left, center, top_right)
fill(acolor+1*diff)
polygon(top_right, center, bottom_right)
fill(acolor+2*diff)
polygon(bottom_right, center, bottom_left)
fill(acolor+3*diff)
polygon(bottom_left, center, top_left)