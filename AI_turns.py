import tree as t
import numpy as np
import pandas as pd
import player as p

if __name__ == "__main__":

    result_list = []
    
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

    trade_days = int(input("How many days would you like the AI to trade for?"))

    #AI = input("Which AI you want to choose: BaselineAI (Enter B), BeamSearchAI (Enter BS): ")

    while True:
          try:
            AI = input("Which AI you want to choose: BaselineAI (Enter B/b), BeamSearchAI (Enter BS/bs): ")
            if AI == "B" or AI == "b":
                break
            elif AI == "BS" or AI == "bs":
                break
            else:
                print(f"Enter valid choice\n")  
          except:
                continue

    if AI == 'B':
        print("you chose Baseline AI")
        t.basic_AI(node, 4, trade_days)
    else:
        print("You chose BeamSearch AI")
        t.beam_search(node, 4, trade_days)
        
    

