import NN_tree as t
import numpy as np
import pandas as pd
import player as p

if __name__ == "__main__":

    result_list = []
    actionsListPredicted = [['h', 'h', 'h', 'h', 'h'],
                           ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h'],
                           ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
                           ['h', 'h', 'h', 'h', 'h', 'h', 's', 's', 's', 's', 's', 's',
                            's', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h'],
                           ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h',
                            'h']]
    
    #cash = int(input("Enter Your Starting Cash: "))
    while True:
          try:
            cash = int(input("Enter Your Starting Cash: "))
            if cash > 5000:
                play = True
                break
            else:
                print(f"Please enter cash more than 5000")  
          except:
                continue
    player_obj = p.Player('AAPL', cash, {'AAPL': 0})
    node = t.Node(player=player_obj)

    while True:
          try:
            trade_days = int(input("How many days would you like the AI to trade for A)5 B)25 c)45 D)65 E)45 days: "))
            if trade_days == 5 or trade_days == 25 or trade_days == 45 or trade_days == 65 or trade_days == 85:
                play = True
                break
            else:
                print(f"Choose among 5, 25, 45, 65, 85")
          except:
                continue
    player_obj = p.Player('AAPL', cash, {'AAPL': 0})
    node = t.Node(player=player_obj)

    

    if trade_days == 5:
        actions = actionsListPredicted[0]
    elif trade_days == 25:
        actions = actionsListPredicted[1]
    elif trade_days == 45:
        actions = actionsListPredicted[2]
    elif trade_days == 65:
        actions = actionsListPredicted[3]
    else:
        actions = actionsListPredicted[4]
    #AI = input("Which AI you want to choose: BaselineAI (Enter B), BeamSearchAI (Enter BS): ")

    while True:
          try:
            AI = input("Which AI you want to choose: BaselineAI (Enter B), BeamSearchAI (Enter BS), NN + BeamSearch (Enter NNBS): ")
            if AI == "B" or AI == "b":
                break
            elif AI == "BS" or AI == "bs":
                break
            elif AI == "NNBS" or AI == "nnbs":
                break
            else:
                print(f"Enter valid choice\n")  
          except:
                continue

    if AI == 'B':
        print("you chose Baseline AI")
        t.basic_AI(node, 4, trade_days)
    elif AI == 'BS':
        print("You chose BeamSearch AI")
        t.beam_search(node, 4, trade_days)
    else:
        print("You chose NN + BeamSearch AI")
        t.nn_beam_search(node, 4 , trade_days, actions)
        
    

