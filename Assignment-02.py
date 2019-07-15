#!/usr/bin/env python
# coding: utf-8

# The aim of this assigment is to get you familiarized the NumPy package, and have a quick introduction to the plotting packages Matplotlib and Seaborn. NumPy allows efficient, "vectorized" processing of data in Python. As in the last assignment, I will indicate the tasks you need to do as part of the homework with the shorthand __`[ HW ]`__. 
# 
# # Reading: Introduction to NumPy
# 
# - __`[ HW ]`__ Read [this "Quickstart tutorial"](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html) for NumPy. 
# 
# 
# Other pages you may want to read: [Data types](https://docs.scipy.org/doc/numpy-dev/user/basics.types.html), [Indexing](https://docs.scipy.org/doc/numpy-dev/user/basics.indexing.html), [Broadcasting](https://docs.scipy.org/doc/numpy-dev/user/basics.broadcasting.html).
# 
# In order to do some of the exercises below, you will need to dive a little deeper into NumPy. Feel free to use [NumPy reference](https://docs.scipy.org/doc/numpy-dev/reference/index.html), [Stack Overflow](http://stackoverflow.com/) (a question-answer site), or other tutorials you may find on the web. (If you do find other useful tutorials, feel free to share with others in the course chat room.)

# # Introduction to NumPy

# In[21]:


# [ HW ] execute this cell to import NumPy, Matplotlib, and Seaborn
# The line with %matplotlib is an IPython "magic" command; you can read more about 
# magics at this link: https://ipython.org/ipython-doc/3/interactive/magics.html

import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[22]:


# Here are some example commands to get our feets wet
# [ HW ] execute this cell and inspect the outputs to see 
# how slicing and indexing work (feel free to edit/experiment 
# with the code )

print "Make a 3 x 5 array (matrix) of random numbers"
x = np.random.random((3, 5))
print x
print

print "Add 1 to every element"
x = x + 1
print x
print

# Note that indexing in Python is 0-based, so it may be confusing 
# to talk about the "first row"! 
print "Get the element at column 2 of row 0" 
print x[0, 2]
print

# The colon syntax is called "slicing" the array. 
print "Get the first row (i.e., row 0)"
print x[0, :]
print

print "Get every 2nd column of the first row"
print x[0, ::2]
print


# In[23]:


# [ HW ] Print the minimum, maximum, mean, and standard deviation of all the 
# elements of the array x. 
# Note that you should not use loops for these, but should use the appropriate
# NumPy methods instead.

## Your code here
a = np.amin(x)
print a

b = np.amax(x)
print b

c = np.mean(x)
print c

d = np.std(x)
print d



# In[24]:


# [ HW ] Print the minimum, maximum, mean, and standard deviation of each column 
# of x, then do the same for each row of x.
# Note that you should not use loops for these, but should use the appropriate
# NumPy methods instead.

## Your code here

a = np.amin(x, axis=0)
print a

b = np.amax(x, axis=0)
print b

c = np.mean(x, axis=0)
print c

d = np.std(x, axis=0)
print d


e = np.amin(x, axis=1)
print e

f = np.amax(x, axis=1)
print f

g = np.mean(x, axis=1)
print g

h = np.std(x, axis=1)
print h


# In[25]:


# Here is a quick simulation of 100 fair "coin tosses"
heads = np.random.binomial(100, .5)
print "Number of heads:", heads

# [ HW ] Execute this cell to see what it does


# In[26]:


# [ HW ] Write code that repeats the 100 coin toss 
# experiment 50 times, and records the outcome in a
# NumPy array called head_counts

## Your code here
head_counts = np.random.binomial(100, .5, size = 50)
print head_counts


# # Introduction to plotting

# In[27]:


# Here is a simple plot using Matplotlib 
# [ HW ] Execute this cell to see what it does, and edit/experiment with it 
# to try to make it do other things, so that you get a feel for 
# how various options work 

x = np.linspace(0, 10, 30)  # An array of 30 points from 0 to 10
y = np.sin(x)
z = y + np.random.normal(size=30) * .2 # Noisy version
plt.plot(x, y, 'ro-', label='A sine wave')
plt.plot(x, z, 'b-', label='Noisy sine')
plt.legend(loc = 'lower right')
plt.xlabel("X axis")
plt.ylabel("Y axis")           
plt.show()


# In[28]:


# [ HW ] Take two of your favorite mathematical functions  (instead 
# of sin), and show them in the same plot

## Your code here
x = np.linspace(-5, 5, 20)
y = np.expm1(x)
z = np.power(x,3)
plt.plot(x, y, 'c.-', label='exp(x)-1')
plt.plot(x, z, 'y*-', label='x^3')
plt.legend(loc = 'lower right')
plt.xlabel("X axis")
plt.ylabel("Y axis")           
plt.show()


# In[29]:


# [ HW ] Make a histogram plot of the head_counts array you 
# created above, using Matplotlib's plt.hist() method

## Your code here
plt.hist(head_counts, range = (30, 80))


# # The Monty Hall Problem
# 
# In this problem, we will simulate a famous probability puzzle. You can read about the interesting story behind it (which involves Marilyn vos Savant, "the world's smartest person") [here](https://priceonomics.com/the-time-everyone-corrected-the-worlds-smartest/) (this link may also help clarify the problem, in case the description below is a little cryptic.
# <center>
# <img src="./img/marilyn.png" width="300">
# </center>
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




