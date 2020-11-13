import tree as t
import numpy as np
import pandas as pd
import player as p

if __name__ == "__main__":

    result_list = []
    cash = int(input("Enter Your Starting Cash: "))
    player_obj = p.Player('AAPL', cash, {'AAPL': 0})
    node = t.Node(player=player_obj)

    trade_days = int(input("How many days would you like the AI to trade for?"))

    AI = input("Which AI you want to choose: BaselineAI (Enter B), BeamSearchAI (Enter BS): ")

    if AI == 'B':
        print("you chose Baseline AI")
        t.basic_AI(node, 4, trade_days)
    else:
        print("You chose BeamSearch AI")
        t.beam_search(node, 4, trade_days)
        
    

