#! /usr/bin/env python
# coding: utf-8
# exer_1.py
# 2019-02-22

# canvas 100x100. Draw four squares, side 20 units, each one facing a corner of the canvas

canvas = 100
square = 20

newPage(canvas, canvas)
rect(0, 0, square, square)
rect(canvas-square, 0, square, square)
rect(0, canvas-square, square, square)
rect(canvas-square, canvas-square, square, square)