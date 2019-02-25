#! /usr/bin/env python
# coding: utf-8
# exer_5.py
# 2019-02-26

# canvas 100x100 draw two polygons of three sides each one, each polygon should have two vertices matching two contiguous canvas corners and one vertex matching the canvas centre

canvas = 100
center = (canvas/2, canvas/2)

newPage(canvas, canvas)
polygon((0, 0), center, (0, canvas))
polygon((canvas, 0), center, (canvas, canvas))