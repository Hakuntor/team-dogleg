"""
The main part of the enviroment. Here the wanted behaviour/rules are added
"""

import gym
from gym import error, spaces, utils
from gym.utils import seeding

# Our custom environment. It inherits form the gym.Env class
class Well2DEnv(gym.Env): # Are numbers not allowed?
    # To render the environment we speicify the "human" way (video window)
    metadata = {'render.modes': ['human']}
    
    def __init__(self):
        pass

