#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 22:14:58 2018

@author: sameepshah
"""

import random



class Perceptron(object):
    """docstring for Perceptron"""
    def __init__(self):
        super(Perceptron, self).__init__()
        self.w = [random.random() * 2 - 1 for _ in range(2)] # weights
        self.learningRate = 0.1

    def response(self, x):
        """perceptron output"""
        
        y = sum([i * j for i, j in zip(self.w, x)]) 
        if y >= 0:
            return 1
        else:
            return -1

    def updateWeights(self, x, iterError):
        """
        upates the wights status, w at time t+1 is
        w(t+1) = w(t) + learningRate * (d - r) * x
        iterError is (d - r)
        """
       
        self.w = \
            [i + self.learningRate * iterError * j for i, j in zip(self.w, x)]

    def train(self, data):
        """
        trains all the vector in data.
        Every vector in data must three elements.
        the third eclemnt(x[2]) must be the label(desired output)
        """
        learned = False
        iteration = 0
        while not learned:
            globalError = 0.0
            for x in data: # for each sample
                r = self.response(x)
                if x[2] != r: # if have a wrong response
                    iterError = x[2] - r # desired response - actual response
                    self.updateWeights(x, iterError)
                    globalError += abs(iterError)
            iteration += 1
            if globalError == 0.0 or iteration >= 100: # stop criteria
                print ('iterations: %s' % iteration)
                learned = True # stop learing

