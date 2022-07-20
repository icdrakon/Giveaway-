#!/usr/bin/env python
# coding: utf-8

# import variables


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
import os


# shuffle


import random

with open('expanded.club-q3-diamond', mode="r", encoding="utf-8") as myFile:
    lines = myFile.readlines()

random.shuffle(lines)
print (lines)


# format


import random

with open('fg', mode="r", encoding="utf-8") as myFile:
    lines = myFile.readlines()

random.shuffle(lines)
print (lines)


