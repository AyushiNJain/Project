# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:44:58 2020

@author: Admin
"""


#import numpy as np
#import matplotlib.pyplot as plt
import math
print("Find the resistivity of an intrinsic semiconductor with intrinsic concentration of 2.5 X 10^19 per m\u00b3. The mobilities of electrons and holes are 0.40 m\u00b2/V-s and 0.20 m\u00b2/V-s.\n")
print("Solution: Given data are:\n")
print("Intrinsic concentration (n) = 2.5 X 10^19/m\u00b3\n")
print("Mobility of electrons(\u03BCe) = 0.40 m\u00b2/V-s\n")
print("Mobility of holes(\u03BCp) = 0.20 m\u00b2/V-s\n")
print("The conductivity of an intrinsic semiconductor(\u03C3) = ne[\u03BCe + \u03BCp]\n")
print("The resistivity (\u03c1) = 1/(\u03C3) = 1/ne[\u03BCe + \u03BCp]\n")
print("=1/2.5 X 10^19 X 1.6 X 10^-19[0.40+0.20]\n")
concentration=2.5*math.pow(10,19) 
electrons=0.40 
holes=0.20  
sum=electrons+holes
e=1.6*math.pow(10,-19)
m=concentration*e
conductivity=m*sum
resistivity=1/conductivity
print("=",round(resistivity,4),"\u03A9-m.")
