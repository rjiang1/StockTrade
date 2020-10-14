import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
from keras.layers import Dense, Dropout,LSTM
from keras.models import Model
from keras.layers import Input, Dense

data = pd.read_csv("AAPL.csv", usecols=[1,2,3,4,6,7,8])

opens = data['Open']
highs = data['High']
lows = data['Low']
close = data['Close']
volume = data['Volume']
twen_d = data['20_day'] #20 day moving averages
fif_d = data['50_day']    #50 day moving aberages

print(opens)