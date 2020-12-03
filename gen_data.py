import player as p
import numpy as np
import pandas as pd
import random
import math
import copy
import AI_turns as ait
import alt_tree as at

data = pd.read_csv("train2.csv")




if __name__ == "__main__":
    # data['y_target'] = y_tar
    # print(data)

    # data.to_csv('train.csv')
    # data['buy'] = ''
    # data['sell'] = ''
    # data['hold'] = ''

    # print(data['y_target'])
    # one_hot = pd.get_dummies(data['y_target'])
    # print(one_hot)
    # data = pd.concat([data, one_hot], axis=1)
    # print(data)
    # data.drop(['y_target'], axis=1, inplace=True)
    # print(data)
    # data.to_csv('train2.csv')
    print(data)