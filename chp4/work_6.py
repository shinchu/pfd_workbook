#! /usr/bin/env python
# coding: utf-8
# work_6.py
# 2019-02-26
#
# Draw a grid with three columns and three rows. The program should allow the presence of a safe space between the elements (often referred to as "gutter"). The "gutter" value should be expressed in typographical points.

Variable([
    dict(name='columns', ui='Slider',
         args=dict(
             value=3,
             minValue=1,
             maxValue=10,
             tickMarkCount=10,
             stopOnTickMarks=True
         )),
    dict(name='rows', ui='Slider',
         args=dict(
             value=3,
             minValue=1,
             maxValue=10,
             tickMarkCount=10,
             stopOnTickMarks=True
         )),
    dict(name='gutter', ui='Slider',
         args=dict(
             value=1,
             minValue=0,
             maxValue=10
         ))
], globals())

canvas = 100
columns = int(columns)
rows = int(rows)

newPage(canvas, canvas)
column_block = canvas / columns
row_block = canvas / rows

stroke(0)
strokeWidth(0.1)

for i in range(columns-1):
    x = (i + 1) * column_block
    line((x - gutter/2, 0), (x - gutter/2, canvas))
    line((x + gutter/2, 0), (x + gutter/2, canvas))

for i in range(rows-1):
    y = (i + 1) * row_block
    line((0, y - gutter/2), (canvas, y - gutter/2))
    line((0, y + gutter/2), (canvas, y + gutter/2))