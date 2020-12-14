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
            AI = input("Which AI you want to choose: Human (Enter H), BaselineAI (Enter B), BeamSearchAI (Enter BS), NN + BeamSearch (Enter NNBS): ")
            if AI == "H":
                break
            elif AI == "B" or AI == "b":
                break
            elif AI == "BS" or AI == "bs":
                break
            elif AI == "NNBS" or AI == "nnbs":
                break
            else:
                print(f"Enter valid choice\n")  
          except:
                continue


    if AI == 'H':

        data = pd.read_csv("AAPL.csv", usecols=[1,2,3,4,6,7,8])


        ## Recent 30 days data
        df = data.tail(31).copy()
        
        playerObj = p.Player('Apple',cash,{'Apple':0})
        turns = 0
        n_shares_bought = 0
        n_shares_sold = 0
        TotalShares = 0
        TotalCash = 0

        while turns < trade_days:

            print(f"Player your Shares : {playerObj.portfolio} your Cash: {playerObj.cash}\n")
                    
            print(f"Day {turns+1} apple stock: Open-->{float(df.iloc[turns][0])} \n")
            print(f"High-->{float(df.iloc[turns][1])} \n")
            print(f"Low-->{float(df.iloc[turns][2])} \n")
            print(f"Close-->{float(df.iloc[turns][3])} \n")
            print(f"Volume-->{float(df.iloc[turns][4])} \n")
           

            print("4 things you can do")
            print("1. Buy(B/b)  2. Sell(S/s) 3. Hold(H/h) 4. Exit(E/e) \n")
            choice = input("what you want to do?!!!!\n")
            #str1 = 'Apple'+str(turns)
            stockObject = p.Stock('Apple',df.iloc[turns,0])
            
        

            if choice == 'S' or choice == 's':
                #stck = input("which stock you want to sell?")
                n_shares_sold = int(input("How many shares you want to sell--> "))
                if n_shares_sold > playerObj.portfolio['Apple']:
                    print(f"Sorry you dont own that many stocks, Try again!!! \n")
                    continue
                playerObj.sell(stockObject,int(n_shares_sold),'Apple')

            elif choice == 'B' or choice == 'b':
                n_shares_bought = int(input("How many shares you want to buy--> "))
                if (n_shares_bought * float(df.iloc[turns][0])) > playerObj.cash:
                    print(f"Sorry you cant afford that many stocks, Try again!!! \n")
                    continue
                playerObj.buy(stockObject,int(n_shares_bought))

            elif choice == 'H' or choice == 'h':
                turns+=1
                continue
            
            elif choice == 'E' or choice == 'e':
                break

            else:
                print("<<>><<>><<>>Enter Valid Choice<<>><<>><<>> \n")
                continue
                
            turns+=1


        TotalShares = sum(playerObj.portfolio.values()) 
        TotalCash = playerObj.cash+(TotalShares*df.iloc[turns,0])

        print(f"Player your shares : {playerObj.portfolio} your cash :{playerObj.cash} shares cost : {TotalShares*float(df.iloc[turns,0])}\n")

        if TotalCash > cash:
            print(f"Congrats! you made profit of:{TotalCash - cash}\n")
        elif TotalCash < cash:
            print(f"Oh No! you lost :{cash - TotalCash}\n")
        else:
            print(f"No profit/ loss\n")

        print(f"Game end\n")
        print(f"<><><><><><><><><><><><><><><><><><>\n")
           
    elif AI == 'B':
        print("you chose Baseline AI")
        t.basic_AI(node, 4, trade_days)
    elif AI == 'BS':
        print("You chose BeamSearch AI")
        t.beam_search(node, 4, trade_days)
    else:
        print("You chose NN + BeamSearch AI")
        t.nn_beam_search(node, 4 , trade_days, actions)
        
    

