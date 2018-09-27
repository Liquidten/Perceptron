#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:58:23 2018

@author: sameepshah
"""
#local module
import perceptron
import generate_Data

from matplotlib.pylab import plot,norm
import matplotlib.pyplot as plt

""" Linear DATA set generation (function generateData) """
trainset = generate_Data.generateData(100) # train set generation
testset = generate_Data.generateData(30) # test set generation
p = perceptron.Perceptron() # use a short



for x in testset:
    r = p.response(x)
    if r != x[2]: # if the response is not correct
        print ('not hit.')
    if r == 1:
        plot(x[0], x[1], 'xb')
    else:
        plot(x[0], x[1], 'or')

# plot of the separation line. 
# The centor of line is the coordinate origin
# So the length of line is 2
# The separation line is orthogonal to w
n = norm(p.w) # aka the length of p.w vector
ww = p.w / n # a unit vector
ww1 = [ww[1], -ww[0]]
ww2 = [-ww[1], ww[0]]
plot([ww1[0], ww2[0]], [ww1[1], ww2[1]], '--k')
plt.show()