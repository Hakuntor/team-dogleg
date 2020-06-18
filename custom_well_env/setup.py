"""
Setup file for the custom environment. 
Specifies the current verison and what other packages must be installed to use 
the environment
"""

from setuptools import setup

setup(
    name="gym_2DWell",
    version="0.0.1",
    install_requires=["gym"] # Add more modules as development proceeds
) 
