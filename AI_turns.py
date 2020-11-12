import tree as t
import numpy as np
import pandas as pd
import player as p

if __name__ == "__main__":
    #for i in [30,60,90,120]:
    result_list = []
    for k in range(10):
        node = t.Node()
        # final_result = t.beam_search(node, 4, 10)
        final_result = t.basic_AI(node, 4, 10)
        result_list.append(final_result)
    print(result_list)   
    # Find out why beam search always produces the same profit
    #node = t.Node()
    #t.beam_search(node, 4, 120)
    #t.basic_AI(node, 4, 30)

