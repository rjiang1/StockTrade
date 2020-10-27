import numpy as np
import pandas as pd
import player as p

data = pd.read_csv("AAPL.csv", usecols=[1,2,3,4,6,7,8])
##data.head()

## Recent 30 days data
df = data.tail(31).copy()
##df.head()


if __name__ == "__main__":
    play = True

    while (play):
        playerObj = p.Player('Apple',10000,{'Apple':0})
        turns = 0
        n_shares_bought = 0
        n_shares_sold = 0
        TotalShares = 0
        TotalCash = 0
        
        ## GAME SIZE
        gameSize = int(input("How many days of stock you want to predict?"))
        
        while turns < gameSize:

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

        if TotalCash > 10000:
            print(f"Congrats! you made profit of:{TotalCash - 10000}\n")
        elif TotalCash < 10000:
            print(f"Oh No! you lost :{10000 - TotalCash}\n")
        else:
            print(f"No profit/ loss\n")

        print(f"Game end\n")
        print(f"<><><><><><><><><><><><><><><><><><>\n")
        
       
        while True:
          try:
            stillPlay = input("Want to play again!! Enter Y/y or N/n: ")
            if stillPlay == "y" or stillPlay == "Y":
                play = True
                break
            elif stillPlay == "n" or stillPlay == "N":
                play = False
                break
            else:
                print(f"Enter Valid choice\n")  
          except:
                continue

    print("Thanks For Playing Game!!")

        


