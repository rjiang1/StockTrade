﻿# StockTrade
Run the Player_Turns.ipynb/ Player_Turns.py file.

It's a single player stock price prediction game.

First player will be prompted for number of days he/ she wanted to predict Apple company stocks.

After your portfolio will get Initialized to '0' Apple stocks and 10000 as your cash.

Apple stocks open, close, high, low and volume gets displayed on screen (1 day stock details).

For each turn the player will be prompted for 4 actions
* Buy - Enter B/b to buy a stock and then you have to enter number of stocks you want to buy, one cannot buy stocks worth more than his/ her cash balance.
* Sell - Enter S/s to sell a stock and then you have to enter number of stocks you want to sell, one cannot sell stocks whose count is more than what he/ she actually owns.
* Do Nothing/ Hold - Enter H/h, you will be shown next day apple stock.
* Exit - Enter E/e you will be exited out of prediction game and then your portfolio, profit/ loss will be shown.

Once his/ her prediction ends after n days (n is what you gave as input at first) we will be calculating totalCash as cash Balance + total shares cost that one holds according to n+1 day apple stocks open price.

Next player portfolio, whether he/ she ended up in profit [win] i.e., totalCash > 10000 (starting balance) or loss i.e., totalCash < 10000 will be displayed.

For each turn the player is given information on the current day's information of the stock AAPL.

* High - The highest price the stock traded for that day
* Low  - The lowest price the stock traded for that day
* Close - The final price of the stock that day
* Volume - The amount of trades everyone in the stockmarket mad
* 20_day - The average price of the stock over the course of the last 20 days
* 50_day - The average price of the stock over the course of the last 50 days

It will update the value of your portfolio accordingly at the start of each turn.

After game ends it will again prompt you to enter Y/ N to play the game again. Enter Y/y to play game again or enter N/n to exit game.

**The closing price of the previous day and the opening price of the current day will be different due to after hours trading and premarket trading.**

﻿#BeamSearch
 
 BeamSearch_Tree_AI:
 
 Run the AI_turns.py file. (If you want to run the baseline AI comment the line:  -------- and uncomment the line:---------- in AI_turns.py)
 
 Its a single player game that AI plays. 
 
You will be prompted to enter the number of days you wanted AI to predict and the cash with which AI should start with. Now portfolio of AI gets intialized to zero apple shares and cash as the value you entered (Try to enter cash atleast 5000 cash as each apple stock costs around 100-120 dollars, this will help you to see the performance of AI). Then it will show the level of tree generated by BeamSearch algorithm and set of actions that AI has taken at that particular level. Next you can hit enter to see the next level actions taken by AI. In this way should continue to hit enter until AI finishes the game. 


Once AI prediction ends after n days (n is what you gave as input at first) we will be calculating totalCash as cash Balance + total shares cost that one holds according to n+1 day apple stocks open price.

Next AI portfolio, whether AI ended up in profit [win] i.e., totalCash > Cash (starting balance) or loss i.e., totalCash < Cash will be displayed.
 
 
 

