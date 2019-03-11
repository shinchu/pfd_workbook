#! /usr/bin/env python
# coding: utf-8
# work_3.py
# 2019-03-11

# Write a program able to draw a ruler of a specific measure unit (either PostScript points or millimeters) across the entire canvas. The ruler ticks should be of different lengths according to a given rhythm. Use a while loop. Numbers displayed along the ruler are a plus.

Variable([
    dict(name='canvas', ui='Slider',
         args=dict(
             value=100,
             minValue=100,
             maxValue=500
         )),
    dict(name='mm', ui='CheckBox')
], globals())

newPage(canvas, 50)

y = 0.5

stroke(0)
strokeWidth(1)
line((0, y), (canvas, y))

font("Input Mono", 6)
if mm:
    unit = 3.7795
    text("millimeters", (5, 50-10))
else:
    unit = 1
    text("PostScript points", (5, 50-10))


font("Input Mono Condensed", 4)
i = 0
x = 0
while x < canvas:
    if i % 10 == 0:
        line((x, y+10), (x, y)) 
        text(str(i), (x, y+15), align="center")
    elif i % 5 == 0:
        line((x, y+5), (x, y))
        if mm:
            text(str(i), (x, y+15), align="center")

    if mm:
        line((x, y+2), (x, y))
    
    i += 1
    x = unit * i

    