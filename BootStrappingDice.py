# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:36:30 2016

@author: John Fuini

Here we are going to take an initial sample, compute a statistic, in this case the median, and bootstrap the sample distribution in order to create find a distribution for the statistic and hopefully a better statistic. 
"""

import numpy as np
import scipy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
import random

#initial parameters.
n = 50 #sample size
B = 1000 #number of bootstraps

def roll_dice(n):
    die_rolls = []
    for i in range(0,n):
        die_rolls.append(random.randint(1,6))
    return np.array(die_rolls) 
        
roll1 = roll_dice(n)
first_mean = np.mean(roll1)
print(first_mean)
plt.figure(1)
plt.hist(roll1, 6)
plt.show()

"""
This obviously doesn't look like all with equal probability.  

Now we're going to bootstrap based on our sample distribution.

We will do this B number of times, and grab a bunch of means and plot the distribution of all die rolls, and the distribution of means.
"""

boot_vec = np.random.choice(roll1, n*B)
boot_mtx = boot_vec.reshape([B, n])
boot_means = np.mean(boot_mtx, axis = 1)#find means for each row

plt.figure(2)
plt.hist(boot_vec,6)
plt.show()
print("Note that the bootstraped histogram is extremly similar to the original sample, as it must be, since we are sampling uniformly the original distribution")
plt.figure(3)
plt.hist(boot_means,20)
plt.axvline(np.mean(boot_means), color = 'r', linewidth = 3)
plt.show()
print("original mean: %s, Bootstrapped mean: %s, Ideal mean: %s" % (first_mean,np.mean(boot_means), 3.5))
print("This most naive form of bootstrapping seems to only give you a standard error associated with the statistic in question")