#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def generateData(n):
    """
    generates a 2D linearly separable dataset with n samples.
    
    """
    xb = (np.random.rand(n) * 2 -1) / 2 - 0.5
    yb = (np.random.rand(n) * 2 -1) / 2 + 0.5
    xr = (np.random.rand(n) * 2 -1) / 2 + 0.5
    yr = (np.random.rand(n) * 2 -1) / 2 - 0.5
    inputs = []
    inputs.extend([[xb[i], yb[i], 1] for i in range(n)])
    inputs.extend([[xr[i], yr[i], -1] for i in range(n)])
    return inputs
