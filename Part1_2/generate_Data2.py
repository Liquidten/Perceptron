#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:56:40 2018

@author: sameepshah
"""
import numpy as np
import math 

def generateData2(n):
    """
    generates a 2D NON linearly separable dataset with n samples.
    
    """
    xb = (np.random.rand(n) * 2 -1) / 2 - 0.5
    #yb = (np.random.rand(n) * 2 -1) / 2 - 0.5
    #yb = math.sqrt(1 - (n*n)) 
    #yb = 1 - xb.apply(lambda i: return i^2)
    xr = (np.random.rand(n) * 2 -1) / 2 - 0.5
    squarer = lambda t: t ** 2
    root = lambda t: math.sqrt(t)
    vfunc = np.vectorize(squarer)
    vfunc2 = np.vectorize(root)
    x_ = vfunc(xb)
    y_ = 4-x_;
    yb = vfunc2(y_)
    x_ = vfunc(xr)
    y_ = 8-x_;
    yr = vfunc2(y_)
    #yr = (np.random.rand(n) * 2 -1) / 2 - 0.5
    inputs = []
    inputs.extend([[xb[i], yb[i],1] for i in range(n)])
    #print(inputs)
    inputs.extend([[xr[i], yr[i], -1] for i in range(n)])
    #print(inputs)
    return inputs