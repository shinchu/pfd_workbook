#! /usr/bin/env python
# coding: utf-8
# exer_3.py
# 2020-03-15
#
# http://www.pythonfordesigners.com/how-to-make-choices/

Variable([
    dict(name='distance', ui='Slider',
         args=dict(
             value=0,
             minValue=0,
             maxValue=1
         )),
     dict(name='switch', ui='CheckBox')
], globals())


size(100, 100)

n_dots = 3
margin = 5
n_margin = n_dots + 1

d = (height() - n_margin * margin) / n_dots

for i in range(n_dots):
    x = width() / 2 - d / 2
    y = (i + 1) * margin + i * d
    if switch:
        if i % 2 == 0:
            x += distance * (width() - d) / 2
        else:
            x -= distance * (width() - d) / 2
    else:
        if i % 2 == 0:
            x -= distance * (width() - d) / 2
        else:
            x += distance * (width() - d) / 2

    oval(x, y, d, d)
