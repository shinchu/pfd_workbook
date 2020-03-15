#! /usr/bin/env python
# coding: utf-8
# exer_1.py
# 2020-03-15
#
# http://www.pythonfordesigners.com/how-to-keep-doing-things-until-you-need-to/

Variable([
    dict(name='bar', ui='Slider',
         args=dict(
             value=10,
             minValue=5,
             maxValue=50
         )),
     dict(name='direction', ui='CheckBox')
], globals())

size(100, 100)

n_bars = int(width() // bar)

for i in range(n_bars):
    if i % 2 == 0:
        fill(0)
    else:
        fill(1)
    
    if direction:
        rect(0, i * bar, width(), bar)
    else:
        rect(i * bar, 0, bar, height())

