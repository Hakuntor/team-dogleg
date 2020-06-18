"""
Initialization file for the environment
"""
from gym.envs.registration import register

register(
    id="2DWell-v0",
    entry_point = "gym_2DWell.envs:2DWellEnv"
)