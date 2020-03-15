#! /usr/bin/env python
# coding: utf-8
# exer_2.py
# 2020-03-15
#
# http://www.pythonfordesigners.com/how-to-keep-doing-things-until-you-need-to/

Variable([
    dict(name='density', ui='Slider',
         args=dict(
             value=10,
             minValue=5,
             maxValue=50
         ))
], globals())

size(100, 100)

n_lines = int(width() // density)
stroke(0)

for i in range(n_lines):
    line((i * density, height()), (i * density + density / 2, 0))
    line((i * density + density / 2, 0), ((i + 1) * density, height()))
