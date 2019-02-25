#! /usr/bin/env python
# coding: utf-8
# exer_2.py
# 2019-02-26

# canvas 100x100. Draw four ovals, 20 units diameter, each one having its center point to a canvas corner

canvas = 100
d = 20
r = d / 2

newPage(canvas, canvas)
oval(0-r, 0-r, d, d)
oval(canvas-r, 0-r, d, d)
oval(0-r, canvas-r, d, d)
oval(canvas-r, canvas-r, d, d)
