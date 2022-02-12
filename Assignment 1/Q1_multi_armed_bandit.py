from bandit_env import bandit_env 
import numpy as np
import random

np.random.seed(0)

game = bandit_env([2.5, -3.5, 1.0, 5.0, -2.5], [0.33, 1.0, 0.66, 1.98, 1.65])
print(game.n)
print(game.r_mean)
print(game.r_stddev)

