import tree as t
import numpy as np
import pandas as pd
import player as p

if __name__ == "__main__":

    node = t.Node()
    # t.beam_search(node, 4, 15)
    # Find out why beam search always produces the same profit
    t.basic_AI(node, 4, 9)

