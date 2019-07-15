#!/usr/bin/env python
# coding: utf-8



import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

# # The Monty Hall Problem
# 
# In this problem, we will simulate a famous probability puzzle. You can read about the interesting story behind it (which involves Marilyn vos Savant, "the world's smartest person") [here](https://priceonomics.com/the-time-everyone-corrected-the-worlds-smartest/) (this link may also help clarify the problem, in case the description below is a little cryptic.
# In a gameshow, contestants try to guess which of 3 closed doors contains a cash prize; the two other doors have goats behind them. The probability of choosing the correct door in the first try is, of course, 1/3. 
# 
# As a twist, the host of the show occasionally opens a door after a contestant makes his or her choice. This door is always one of the two doors the contestant did not pick, and is also always one of the goat doors (note that it is always possible to do this, since there are two goat doors).
# 
# At this point, the contestant has the option of keeping his or her original choice, or swtiching to the other unopened door. The question is: is there any benefit to switching doors? The answer surprises many people who haven't heard the question before.
# 
# We will attempt to answer the puzzle by running simulations in Python. We'll do it in several parts. Your task is to fill in the code for the missing functions below (I will skip the __`[ HW ]`__ signs from now on)

# First, write a function called simulate_prizedoor. This function will simulate the location of the prize in many games -- see the detailed specification below.

# In[30]:


"""
Function
--------
simulate_prizedoor

Generate a random array of 0s, 1s, and 2s, representing
hiding a prize behind one of door 0, door 1, and door 2

Parameters
----------
nsim : int
    The number of simulations to run

Returns
-------
sims : array
    Random array of 0s, 1s, and 2s

Example
-------
>>> print simulate_prizedoor(3)
array([0, 0, 2])
"""
def simulate_prizedoor(nsim):
    sims = np.random.randint(3, size= nsim)
    return sims
print simulate_prizedoor(10)


# Next, write a function that simulates the contestant's guesses for nsim simulations. Call this function simulate_guess. 

# In[31]:


"""
Function
--------
simulate_guess

Return guesses for which door has the prize. This could
return a random guess, or always pick a fixed guess (e.g., 
door 2), etc. Any strategy goes. 

Parameters
----------
nsim : int
    The number of simulations to generate guesses for

Returns
-------
guesses : array
    An array of guesses. Each guess is a 0, 1, or 2

Example
-------
>>> print simulate_guess(5)
array([0, 0, 0, 0, 0])
"""
## your code here
def simulate_guess(nsim):
    guesses = np.random.randint(3, size= nsim)
    return guesses
print simulate_guess(10)


# Next, write a function, goat_door, to simulate randomly revealing one of the goat doors that a contestant didn't pick.

# In[32]:


"""
Function
--------
goat_door

Simulate the opening of a "goat door" that doesn't contain the prize,
and is different from the contestants guess

Parameters
----------
prizedoors : array
    The door that the prize is behind in each simulation
guesses : array
    The door that the contestant guessed in each simulation

Returns
-------
goats : array
    The goat door that is opened for each simulation. Each item is 0, 1, or 2, and is different
    from both prizedoors and guesses

Examples
--------
>>> print goat_door(np.array([0, 1, 2]), np.array([1, 1, 1]))
>>> array([2, 2, 0])
"""
# Your code here
def goat_door(guesses, prizedoors):
    goats = [np.setdiff1d([0, 1, 2], [prizedoors[i], guesses[i]])[0] for i in range(len(prizedoors))]
    return goats
guesses = np.random.randint(3, size= 10)
prizedoors = np.random.randint(3, size= 10)
print guesses
print prizedoors
print goat_door(guesses, prizedoors)


# Write a function, switch_guess, that represents the strategy of always switching a guess after the goat door is opened.

# In[33]:


"""
Function
--------
switch_guess

The strategy that always switches a guess after the goat door is opened

Parameters
----------
guesses : array
     Array of original guesses, for each simulation
goatdoors : array
     Array of revealed goat doors for each simulation

Returns
-------
The new door after switching. Should be different from both guesses and goatdoors

Examples
--------
>>> print switch_guess(np.array([0, 1, 2]), np.array([1, 2, 1]))
>>> array([2, 0, 0])
"""
## Your code here
def switch_guess(guesses, goatdoors):
    return [np.setdiff1d([0, 1, 2], [guesses[i], goatdoors[i]])[0] for i in range(len(guesses))]
    
guesses = np.random.randint(3, size= 10)
goatdoors = np.random.randint(3, size= 10)
print guesses
print goatdoors
print switch_guess(guesses, goatdoors)


# Last function: write a win_percentage function that takes an array of guesses and prizedoors, and returns the percent of correct guesses

# In[34]:


"""
Function
--------
win_percentage

Calculate the percent of times that a simulation of guesses is correct

Parameters
-----------
guesses : array
    Guesses for each simulation
prizedoors : array
    Location of prize for each simulation

Returns
--------
percentage : number between 0 and 100
    The win percentage

Examples
---------
>>> print win_percentage(np.array([0, 1, 2]), np.array([0, 0, 0]))
33.333
"""
## Your code here
def win_percentage(guesses, prizedoors):
    count = 0
    for i in range(len(guesses)):
        if guesses[i] == prizedoors[i]:
            count += 1
    return 100.0 * count / float(len(guesses))


guesses = np.random.randint(3, size = 10)
prizedoors = np.random.randint(3, size = 10)
print guesses
print prizedoors
print win_percentage(guesses, prizedoors)


# Now, put it together. Simulate 10000 games where contestant keeps his original guess, and 10000 games where the contestant switches his door after a goat door is revealed. Compute the percentage of time the contestant wins under either strategy. Is one strategy better than the other?

# In[35]:


## Your code here
def simulate_prizedoor(nsim):
    sims = np.random.randint(3, size = nsim)
    return sims

def simulate_guess(nsim):
    guesses = np.random.randint(3, size = nsim)
    return guesses

def goat_door(guesses, prizedoors):
    goats = [np.setdiff1d([0, 1, 2], [prizedoors[i], guesses[i]])[0] for i in range(len(prizedoors))]
    return goats

def switch_guess(guesses, goatdoors):
    return [np.setdiff1d([0, 1, 2], [guesses[i], goatdoors[i]])[0] for i in range(len(guesses))]

def win_percentage(guesses, prizedoors):
    count = 0
    for i in range(len(guesses)):
        if guesses[i] == prizedoors[i]:
            count += 1
    return 100.0 * count / float(len(guesses))

nsim = 1000

prizedoors = simulate_prizedoor(nsim)
guesses = simulate_guess(nsim)

print "Wins without switching: %f" % win_percentage(guesses, prizedoors)

prizedoors = simulate_prizedoor(nsim)
guesses = simulate_guess(nsim)
goatdoors = goat_door(guesses, prizedoors)

print "Wins with switching: %f" % win_percentage(switch_guess(guesses, goatdoors), prizedoors)


# Yes, obviously switching strategy is better than not switching.

# In[ ]:




