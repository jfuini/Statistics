# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:45:42 2016

@author: John Fuini

Random sample of 144 cats have their sleep monitored.  Slept average of 16 hours/day.  Dogs sleep on average of 14 hours per day.  Is there convincing evidence that they have different sleeping averages?  Test statistic is 1.73.

Here the test statistic is given, so we need to solve for the standard deviation.

Z = (xbar - mu)/Std_err    Std_err = sigma/sqrt(n)

so

sigma = sqrt(n)(xbar - mu)/Z
"""
import numpy as np
import scipy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt

n = 144
mu = 14
xbar = 16
Z = 1.73
sigma = np.sqrt(n)*(xbar-mu)/Z
std_err = sigma/np.sqrt(n)
print(sigma, std_err)  #we didn't to grab sigma, the test statistic immediatly gives us the standard error, when we have xbar and mu.  

#so now we make a normal distribution for the sampling distributions of means for the dogs sleeping behavior, and we want to know the p value for a selected mean to be more extreme than the 16 found for the cats
xgrid = np.linspace(5,23,100)
dist = stats.norm.pdf(xgrid, mu, std_err)
plt.figure(1)
plt.plot(xgrid, dist)
plt.axvline(16)#our cat sample average
(lower, upper) = stats.norm.interval(0.95, mu, std_err)
print("The cat's sleeping mean is inside of the 95% interval")
plt.axvline(lower, color = 'r')
plt.axvline(upper, color = 'r')
plt.show()

#another way to see this is to get the CDF for the value of the cat, and see that it is lower that 0.975, which means that our two tailed p-value is too large. 

print(stats.norm.cdf(xbar, mu, std_err))
two_tailed_p = (1-stats.norm.cdf(xbar, mu, std_err))*2
print("p-value: %s" % two_tailed_p)
print("We see that our p-value is not below 0.05")
print("So we cannot conclude that cats and dogs have different sleeping patterns based on this data")


