'''
This script plots the difference between the integral of a particular function (defined in the f(x) function)
and the estimated integral by performing monte carlo integration.
'''


import random as rnd
import numpy as np
import matplotlib.pyplot as plt

def f(x): # Function for monte carlo integration
    return 0.5 * (x**3) - (x**2) + 1

def monte_carlo_integration(samples): # Returns estimation of the integral via monte carlo method according to the number of samples
    samplesIn=[]
    samplesOut=[]
    num_in = 0
    for k in range(samples):
        x=2*rnd.random()
        y=rnd.random()
        if f(x) > y: # Check to see if point is below curve y=f(x)
            samplesIn.append([x,y]) # point below
        else:
            samplesOut.append([x,y]) # point above
    numIn=len(samplesIn) # number of points below
    return 2*numIn/samples

actual_value = 4/3 # Actual value of integral
approximations = [] # List of the monte carlo approximations for different sample sizes
samples = np.linspace(1, 10000, num=100, endpoint=True, dtype=int)
error = []
for i in samples:
    approximation = monte_carlo_integration(i)
    y_val = abs(approximation - actual_value) # Error between monte carlo␣ approximation and actual value
    error.append(y_val)

# Plotting
plt.plot(samples, error)
plt.xlabel('Sample Size')
plt.ylabel('Error')
plt.title('Monte Carlo Error for $0.5 * x^3 - x^2 + 1$ Over Different Sample Sizes')
plt.show()

# Plotting with log scale on both axes
plt.loglog(samples, error)
plt.xlabel('Log(Sample Size)')