import simulation_tree as t
import numpy as np
import pandas as pd
import player as p

if __name__ == "__main__":

    x = input("Input the number of games")
    game_l = input("Input the number of days of trading")
    cash = 10000
    result_list = []
    for k in range(x):
        player_obj = p.Player('AAPL', cash, {'AAPL': 0})
        node = t.Node(player=player_obj)
        # final_result = t.beam_search(node, 4, game_l)
        final_result = t.basic_AI(node, 4, game_l)
        result_list.append(final_result)

    print("Below are the profits from", x, "games witha a game length of", game_l)
    print(result_list)
