import player as p
import numpy as np
import pandas as pd
import random
import math
import copy


data = pd.read_csv("AAPL.csv", usecols=[1, 2, 3, 4, 6, 7, 8])
twentyMA = data['20_day']
opening_prices = data['Open']


# Recent game_length days data
# df = data.tail(game_length+1).copy()

# stockObject = p.Stock('AAPL',df.iloc[turns,0])

# starting_cash = 0
# five_percent = 0

class Node:
    def __init__(self, action=None, player=p.Player('AAPL',10000,{'AAPL':0})):
        self.action = action  # the action here means what action the parent took. The root will be hold by default
        self.cash = player.cash  # the portfolio value to at that point in the node
        self.children = []  # this is going to be filled with Node() objects
        self.player = player
        self.starting_cash = player.cash
        self.five_percent = math.floor(self.starting_cash * 0.05)


def perform_action(choice, playerObj, stockObject, shares):
    player_child = p.Player(name='AAPL', money=copy.copy(playerObj.cash), portf=copy.copy(playerObj.portfolio))

    if choice == 'S' or choice == 's':

        n_shares_sold = shares
        player_child.sell(stockObject, int(n_shares_sold), 'AAPL')

    elif choice == 'B' or choice == 'b':
        n_shares_bought = shares
        player_child.buy(stockObject, int(n_shares_bought))

    elif choice == 'H' or choice == 'h':
        pass



    return Node(action=choice, player=player_child)  # that has taken the action


def take_beams(k, array, level):  # for each level in the array, this function takes the k best
    # in this function we will also need to apply the heuristic to take the k best nodes
    moving_average = twentyMA.iloc[-level-1]
    price_difference = opening_prices.iloc[-level-1] - moving_average
    # we will take the difference of the stock prices
    # we then take the number of shares the player has
    # multiply the difference with the shares to find
    # the idea is that prices will move towards averages
    # therefore a negative price difference means the price is undervalued
    # the opposite for positive
    # return the k most negative differences by multiplying the number of shares owned
    # with the difference

    # another approach is to measure stock values + cash as a heuristic -- Pavan

    buys = []
    sells = []
    holds = []
    for node in array:
        player = node.player
        action = node.action
        if action == 'b':
            buys.append(node)
        elif action == 's':
            sells.append(node)
        else:
            holds.append(node)

    def best(node_object):
        return node_object.player.cash + (node_object.player.portfolio['AAPL'] * opening_prices.iloc[-level-1])

    buys.sort(reverse=True, key=best)
    sells.sort(reverse=True, key=best)
    holds.sort(reverse=True, key=best)

    def take(x, bucket):
        if len(bucket) < x:
            return bucket
        else:
            return bucket[0:x]

    k_vals = []

    if price_difference < 0:
        k_vals.extend(take(math.ceil(k/2), buys))
        k_vals.extend(take(math.floor(k/2), holds))
    else:
        k_vals.extend(take(math.ceil(k/2), sells))
        k_vals.extend(take(math.floor(k/2), holds))

    k_actions = []
    for ka in k_vals:
        k_actions.append(ka.action)

    print("level:",level)
    print("No of nodes Processed: ",len(array))
    print("Actions AI chose:",k_actions)
    # for ka in k_vals:
    #    print("portfolio:",ka.player.portfolio)
    #    print("price:",ka.player.cash)
    input("Press Enter to Continue")

    return k_vals


def random_take_beam(k, array,level):  # for each level in the array, this function takes k nodes randomly
    num_node = k 
    label_list = [i for i in range(len(array))]  # [0, 1, 2, 3, 4,...,len(array)]
    label_list_random = random.sample(label_list, min(num_node, len(array)))  # choose k labels randomly from the label list

    # nodes_random = array[label_list_random, :]  # array([node[label_random_1], node[label_random_2],...,node[label_random_k]])
    nodes_random = [array[i] for i in label_list_random]
    actions_random = [node.action for node in nodes_random]
    print("level:", level)
    print("No of nodes Processed: ",len(array))
    print("Actions AI chose:",actions_random)
    input("Press Enter to Continue")
    return nodes_random

def nn_take_beams(k, array, level, act):  # for each level in the array, this function takes the k best
    # in this function we will also need to apply the heuristic to take the k best nodes
    moving_average = twentyMA.iloc[-level - 1]
    price_difference = opening_prices.iloc[-level - 1] - moving_average
    # we will take the difference of the stock prices
    # we then take the number of shares the player has
    # multiply the difference with the shares to find
    # the idea is that prices will move towards averages
    # therefore a negative price difference means the price is undervalued
    # the opposite for positive
    # return the k most negative differences by multiplying the number of shares owned
    # with the difference

    # another approach is to measure stock values + cash as a heuristic -- Pavan
    nn_action = act
    buys = []
    sells = []
    holds = []
    for node in array:
        player = node.player
        action = node.action
        if action == 'b':
            buys.append(node)
        elif action == 's':
            sells.append(node)
        else:
            holds.append(node)

    def best(node_object):
        return node_object.player.cash + (node_object.player.portfolio['AAPL'] * opening_prices.iloc[-level - 1])

    buys.sort(reverse=True, key=best)
    sells.sort(reverse=True, key=best)
    holds.sort(reverse=True, key=best)

    def take(x, bucket):
        if len(bucket) < x:
            return bucket
        else:
            return bucket[0:x]

    k_vals = []

    if price_difference < 0:
        k_vals.extend(take(math.ceil(k / 2), buys))
        k_vals.extend(take(math.floor(k / 2), holds))
    else:
        k_vals.extend(take(math.ceil(k / 2), sells))
        k_vals.extend(take(math.floor(k / 2), holds))

    k_vals.sort(reverse=True, key=best)
    k_vals[-1].actions = nn_action

    k_actions = []
    for ka in k_vals:
        k_actions.append(ka.action)

    print("level:", level)
    print("No of nodes Processed: ",len(array))
    print("Action NN chose:", nn_action)
    print("Actions NN + BeamSearch AI chose:",k_actions)
    # for ka in k_vals:
    # print("portfolio:",ka.player.portfolio)
    # print("price:",ka.player.cash)
    # input("Press Enter to Continue")
    input("Press Enter to Continue")
    return k_vals



def doable(act, stockObj, node, shares):  # to check if an action is viable
    player = node.player
    #player = p.Player(name='AAPL', money=copy.copy(node.player.cash), portf=copy.copy(node.player.portfolio))
    if act == 'b':
        if shares <= 0:
            print("Can't buy 0 or less shares")
            return False
        elif stockObj.price * shares > player.cash:
            print("Not enough cash")
            return False
    elif act == 's':
        if shares > player.portfolio[stockObj.ticker]:
            print("Not enough shares")
            return False
    return True


def beam_search(root, k, game_length):  # k is the beam size
    current_q = [root]  # we will iterate through this to create child
    next_q = []  # we will que children nodes here
    df = data.tail(game_length+1).copy()
    count = 0
    for level in range(game_length):
        stockObject = p.Stock('AAPL', df.iloc[level,0])

        while current_q:
            node = current_q.pop()
            
            for act in ['b', 's', 'h']:  # buy sell hold
                shares = int(root.five_percent/float(df.iloc[level][0]))
                if doable(act, stockObject, node, shares):
                    count+=1
                    new_node_obj = Node()
                    child = perform_action(act, node.player, stockObject, shares)
                    node.children.append(child)
                    next_q.append(child)

        if level != game_length-1:
            current_q = take_beams(k, next_q, level)

        if level == game_length-1:
            
            final_result = take_beams(1, next_q, level)

            # TotalShares = sum(playerObj.portfolio.values())
            TotalCash = final_result[0].player.cash + \
                        (final_result[0].player.portfolio['AAPL'] * df.iloc[game_length, 0])

            print("Cash", final_result[0].player.cash)
            print("Portfolio", final_result[0].player.portfolio)
            print("Last day Open Price", df.iloc[game_length, 0])
            print("Total Cash Value", TotalCash)
            print("Total no of nodes Processed:",count)

            if TotalCash > root.starting_cash:
                print(f" Wow! our AI made profit of:{TotalCash - root.starting_cash}\n")
            elif TotalCash < root.starting_cash:
                print(f"Oh No! our AI lost :{root.starting_cash - TotalCash}\n")
            else:
                print(f"No profit/ loss\n")

            # return take_beams(1, next_q, level)  # in the end of the game we will take the best node
            return (TotalCash - root.starting_cash)
        next_q = []


def basic_AI(root, k, game_length):  # k is the beam size
    current_q = [root]  # we will iterate through this to create child
    next_q = []  # we will que children nodes here
    df = data.tail(game_length+1).copy()
    count = 0
    for level in range(game_length):
        stockObject = p.Stock('AAPL', df.iloc[level,0])
        while current_q:
            node = current_q.pop()
            for act in ['b', 's', 'h']:  # buy sell hold
                shares = int(root.five_percent/float(df.iloc[level][0]))
                if doable(act, stockObject, node, shares):
                    count+=1
                    # new_node_obj = Node(action = act, player = p.Player(name = 'bob', money = copy.copy(node.player.cash), portf = copy.copy(node.player.portfolio)))
                    child = perform_action(act, node.player, stockObject, shares)
                    node.children.append(child)
                    next_q.append(child)

        if level != game_length-1:
            current_q = random_take_beam(k, next_q, level)
            
        if level == game_length-1:
            final_result = random_take_beam(1, next_q, level)

            # TotalShares = sum(playerObj.portfolio.values())
            TotalCash = final_result[0].player.cash + \
                        (final_result[0].player.portfolio['AAPL'] * df.iloc[game_length, 0])

            print("Cash", final_result[0].player.cash)
            print("Portfolio", final_result[0].player.portfolio)
            print("Last day Open Price", df.iloc[game_length, 0])
            print("Total Cash Value", TotalCash)
            print("Total No of nodes processed:",count)
            if TotalCash > root.starting_cash:
                print(f"Wow! baseline AI made profit of:{TotalCash - root.starting_cash}\n")
            elif TotalCash < root.starting_cash:
                print(f"Oh No! baseline AI lost :{root.starting_cash - TotalCash}\n")
            else:
                print(f"No profit/  loss\n")

            return (TotalCash - root.starting_cash)  # in the end of the game we will take one node randomly
        next_q = []

def nn_beam_search(root, k, game_length, actions):  # k is the beam size
    current_q = [root]  # we will iterate through this to create child
    next_q = []  # we will que children nodes here
    df = data.tail(game_length + 1).copy()
    count = 0
    result = []
    for level in range(game_length):
        stockObject = p.Stock('AAPL', df.iloc[level, 0])

        #  stockObject = p.Stock('AAPL', df.iloc[game_length,0]) --> this is funny bug

        # print("level:",game_length)

        # print("open price on given day:",df.iloc[level,0])

        while current_q:
            node = current_q.pop()

            for act in ['b', 's', 'h']:  # buy sell hold
                shares = int(root.five_percent / float(df.iloc[level][0]))
                if doable(act, stockObject, node, shares):
                    count+=1
                    # print("action and shares",act,shares)
                    child = perform_action(act, node.player, stockObject, shares)
                    node.children.append(child)
                    next_q.append(child)

        if level != game_length-1:
            current_q = nn_take_beams(k, next_q, level, actions[level])
        

        if level == game_length - 1:
            
            final_result = nn_take_beams(1, next_q, level, actions[level])
            # TotalShares = sum(playerObj.portfolio.values())
            TotalCash = final_result[0].player.cash + \
                        (final_result[0].player.portfolio['AAPL'] * df.iloc[game_length, 0])

            print("Cash", final_result[0].player.cash)
            print("Portfolio", final_result[0].player.portfolio)
            print("Last day Open Price", df.iloc[game_length, 0])
            print("Total Cash Value", TotalCash)
            print("Total Nodes Processed", count)
            if TotalCash > root.starting_cash:
                print(f"Wow! our AI made profit of:{TotalCash - root.starting_cash}\n")
            elif TotalCash < root.starting_cash:
                print(f"Oh No! our AI lost :{root.starting_cash - TotalCash}\n")
            else:
                print(f"No profit/ loss\n")

            # return take_beams(1, next_q, level)  # in the end of the game we will take the best node
            result.append((TotalCash - root.starting_cash))
            result.append(count)
            return result
        next_q = []

"""
class TreeNode:
    self.state # data structure with current cash, portfolio, price info
    self.child_list # list of child nodes (starts empty before tree search)
    def children(self):
        # returns list of children.  generates the list the first time this is called
        if len(self.child_list) > 0: return self.child_list
        for action in self.state.valid_actions():
            child_state = self.state.perform(action)
            child_node = TreeNode(child_state)
            self.child_list.append(child_node)
        return self.child_list

def beam_search(root, K):
    # K is the beam size
    beam = [root]
    while beam is not empty:
        new_beam = []
        for node in beam:
            if node is game over:
                if this is the best final game score so far, save this node
            else:
                add node's children to new_beam
        for child in new_beam:
            estimate child's value with heuristic function
        discard all but the top K most valuable children in new_beam
        beam = new_beam
    return the path from the root to the best game-over node

root = TreeNode(initial_state())
path = beam_search(root)
"""
