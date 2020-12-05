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

np_data = data[['Open', 'Close', 'Low', 'Close', 'Volume', '20_day', '50_day']].to_numpy()
data7d = np.reshape(np_data, (7, 10043, 1))

a = np.shape(np.reshape(np_data, (7, 10043, 1))) #"7d" array
print(data7d)


# print(np.shape(np_data))