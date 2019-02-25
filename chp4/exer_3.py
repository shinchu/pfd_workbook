#! /usr/bin/env python
# coding: utf-8
# exer_3.py
# 2019-02-26

# canvas 100x100 draw two lines connecting two non-contiguous canvas corners

canvas = 100

newPage(canvas, canvas)

stroke(0)
line((0, 0), (canvas, canvas))
line((0, canvas), (canvas, 0))
