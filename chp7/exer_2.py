#! /usr/bin/env python
# coding: utf-8
# exer_2.py
# 2020-03-15
#
# http://www.pythonfordesigners.com/how-to-make-choices/

Variable([dict(name='firstLightThenDark', ui='CheckBox')], globals())

size(100, 100)
margin = 3

d = width() / 3

translate(margin, margin)

for i in range(4):
    if firstLightThenDark:
        x = width() / 5 * i
        y = height() / 5 * i
        fill(0.5 - i / 8)
        print(0.5 - i / 8)
        stroke(0)
        oval(x, y, d, d)
    else:
        x = width() / 5 * (3 - i)
        y = height() / 5 * (3 - i)
        fill(0.125 + i / 8)
        print(0.125 + i / 8)
        stroke(0)
        oval(x, y, d, d)
    

