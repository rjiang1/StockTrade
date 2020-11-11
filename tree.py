import player as p
import numpy as np
import pandas as pd
import random

data = pd.read_csv("AAPL.csv", usecols=[1, 2, 3, 4, 6, 7, 8])

# Recent game_length days data
# df = data.tail(game_length+1).copy()

# stockObject = p.Stock('Apple',df.iloc[turns,0])


class Node:
    def __init__(self, action=None, player=p.Player('Apple',10000,{'Apple':0})):
        self.action = action  # the action here means what action the parent took. The root will be hold by default
        self.cash = player.cash  # the portfolio value to at that point in the node
        self.children = []  # this is going to be filled with Node() objects
        self.player = player


def perform_action(choice, playerObj, stockObject, shares):
    if choice == 'S' or choice == 's':

        n_shares_sold = shares
        playerObj.sell(stockObject, int(n_shares_sold), 'Apple')

    elif choice == 'B' or choice == 'b':

        n_shares_bought = shares
        playerObj.buy(stockObject, int(n_shares_bought))

    elif choice == 'H' or choice == 'h':
        pass
  
    return Node(action=choice, player=playerObj.copy())  # that has taken the action


def take_beams(k, array):  # for each level in the array, this function takes the k best
    # in this function we will also need to apply the heuristic to take the k best nodes
    return []


def random_take_beam(k,array):  # for each level in the array, this function takes k nodes randomly
    num_node = k 
    label_list = [i for i in range(len(array))]  # [0, 1, 2, 3, 4,...,len(array)]
    label_list_random = random.sample(label_list, num_node)  # choose k labels randomly from the label list

    nodes_random = array[label_list_random, :]  # array([node[label_random_1], node[label_random_2],...,node[label_random_k]])
    return nodes_random


def doable(act,stockObj, player, shares):  # to check if an action is viable
    if act == 'b':
        if shares <= 0:
            print("Can't by 0 or less shares")
            return False
        elif stockObj.price * shares > player.cash:
            print("Not enough cash")
            return False
    if act == 's':
        if shares > player.portfolio['Apple']:
            print("Not enough shares")
            return False
    return True


def beam_search(root, k, game_length):  # k is the beam size
    current_q = [root]  # we will iterate through this to create child
    next_q = []  # we will que children nodes here
    df = data.tail(game_length+1).copy()
    for level in range(game_length):
        stockObject = p.Stock('Apple',df.iloc[game_length,0])
        while current_q:
            node = current_q.pop()
            for act in ['b', 's', 'h']:  # buy sell hold
                shares = 500/float(df.iloc[level][0])
                if doable(act, stockObject, player, shares):

                    child = perform_action(act, node, stockObject, shares)
                    node.children.append(child)
                    next_q.append(child)

        current_q = take_beams(k, next_q)
        if level == game_length-1:
            return take_beams(1, next_q)  # in the end of the game we will take the best node
        next_q = []


def basic_AI(root, k, game_length):  # k is the beam size
    current_q = [root]  # we will iterate through this to create child
    next_q = []  # we will que children nodes here
    df = data.tail(game_length+1).copy()
    for level in range(game_length):
        stockObject = p.Stock('Apple',df.iloc[game_length,0])
        while current_q:
            node = current_q.pop()
            for act in ['b', 's', 'h']:  # buy sell hold
                shares = 500/float(df.iloc[level][0])
                if doable(act,stockObject, player, shares):
                    child = perform_action(act,node.copy(), stockObject, shares)
                    child = Node(action=act, player=node.copy())
                    node.children.append(child)
                    next_q.append(child)

        current_q = random_take_beam(k, next_q)
        if level == game_length-1:
            return random_take_beam(1, next_q)  # in the end of the game we will take one node randomly
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
