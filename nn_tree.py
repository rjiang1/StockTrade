import player as p
import numpy as np
import pandas as pd
import random
import math
import copy
import alt_tree as at
import torch as tr
import torch.nn as nn

data = pd.read_csv("train2.csv")

print(data)