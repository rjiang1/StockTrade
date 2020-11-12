import tree as t
import numpy as np
import pandas as pd
import player as p

if __name__ == "__main__":

    node = t.Node()
    t.beam_search(node, 4, 10)
