class Player:
    def __init__(self,name,money = 10000,portf = {}):
        self.portfolio = portf
        self.cash = money
        self.equity_val = 0
    # the "tick" argument refers to an object of the "Stock" class
    def buy(self,tick,shares): #tick here refers to the ticker variable
        if tick.price*shares>self.cash:
            print("Not enough cash")
        else:
            self.portfolio[tick.ticker] = shares #Here i store the ticker 
                                                #name as the key
                                                #and the number of 
                                                #shares as the value
            self.cash-=tick.price*shares
    def sell(self,tick,n_shares,name): #"name" here refer to the stock 
                                       # within out portfolio

        if name in self.portfolio:     #check if stock in portfolio 
            if n_shares > self.portfolio[tick.ticker]:
                print("Not enough shares")
            else:
                self.cash += tick.price*n_shares
                if self.portfolio[name] == 0:
                    del self.portfolio[name]
                else:
                    self.portfolio[name]-=n_shares
        else:
            print("You do not own this stock")

class Stock:
    def __init__(self,ticker,price):
        self.ticker = ticker
        self.price = price

    def update(self,new_price):
        self.price = new_price
    
