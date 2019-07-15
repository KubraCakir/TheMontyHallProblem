#!/usr/bin/env python
# coding: utf-8



import numpy as np
import seaborn as sns





# In[35]:



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
