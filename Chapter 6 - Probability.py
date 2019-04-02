# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:33:25 2019

@author: aalco
"""
import math

#probability density function for a uniform distribution
def uniform_pdf(x):
    return 1 if x>= 0 and x < 1 else 0

#Cumulative distribution function for a uniform distibution 
def uniform_cdf(x):
    "returns probability that a uniform random variable is <= x"
    if x < 0: return 0 #uniform random is never less than 0 
    elif x < 1: return x #P(X <= 0.4) = 0.4
    else: return 1 #uniform random is never more than 1

# the probability density function for a normal distribution 
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu)**2/2/sigma ** 2) / (sqrt_two_pi * sigma))

# The cumulative distribution funciton for the normal distribution
# The cumulative distribution function is non elementary due to the unintegrable inegralit has but the erf function can still allow the creation of a function in python
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu)/math.sqrt(2)/ sigma)) / 2
