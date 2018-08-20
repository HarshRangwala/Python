# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:28:21 2018

@author: Harsh
"""

import turtle
def draw_art():
    tenlines = turtle.Turtle()
    tenlines.shape("arrow")
    tenlines.color("blue")
    for i in range(1,37):
        tenlines.right(10)
        tenlines.circle(100)
draw_art()
def spiral(size: Int, angle: Int) {if (size <= 300) {forward(size)
        right(angle)
        spiral(size + 2, angle)}}
clear()
setPenColor(darkGray)
setFillColor(green)
setBackgroundH(Color(255, 0, 0), yellow)
setPenThickness(1)
setAnimationDelay(0)
spiral(0, 91)