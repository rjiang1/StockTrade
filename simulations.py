import simulation_tree as t
import numpy as np
import pandas as pd
import player as p
import random
import matplotlib.pyplot as plt


if __name__ == "__main__":


    
    game_len_results = []
    nodes_processed_list = []
    random_cash_list = []
    game_len_results_basic = []
    nodes_processed_list_basic = []
  
    game_sizes = [5,25,45,65,85]

    
    for i in range(100):
        random_cash_list.append(random.randint(5000,15000)) # Generating 100 random cash values for 100 simulations with 5 game sizes 

    ## Beam Search AI

    for game_len in game_sizes :
        print("Game Length:",game_len)
        result_list = []
        nodes_count_list = []
        for cash in random_cash_list:
            print("starting with cash:",cash)
            player_obj = p.Player('AAPL', cash, {'AAPL': 0})
            node = t.Node(player=player_obj)
            result = t.beam_search(node, 4, game_len)
            #result = t.basic_AI(node, 4, game_len)
            final_result = result[0]
            nodes_processed = result[1]
            result_list.append(final_result)
            nodes_count_list.append(nodes_processed)
            
        game_len_results.append(result_list)
        nodes_processed_list.append(nodes_count_list)
 
    print(game_len_results)
    print(nodes_processed_list)


    ## Baseline AI

    for game_len in game_sizes :
        print("Game Length:",game_len)
        result_list = []
        nodes_count_list = []
        for cash in random_cash_list:
            print("starting with cash:",cash)
            player_obj = p.Player('AAPL', cash, {'AAPL': 0})
            node = t.Node(player=player_obj)
            #result = t.beam_search(node, 4, game_len)
            result = t.basic_AI(node, 4, game_len)
            final_result = result[0]
            nodes_processed = result[1]
            result_list.append(final_result)
            nodes_count_list.append(nodes_processed)
            
        game_len_results_basic.append(result_list)
        nodes_processed_list_basic.append(nodes_count_list)

    print(game_len_results_basic)
    print(nodes_processed_list_basic)
    
    k = 5
    ## Graphs for beam search performance
    for size_result in game_len_results:
        print(size_result)
        N = len(size_result)
        ind = np.arange(N) 
        width = 0.5       
        plt.bar(ind, size_result, width)

        plt.ylabel('Profit')
        plt.title('Beam_Search_AI_performance %02d'%(k))
        plt.xlabel('Starting cash at each Iteration')
        plt.xticks(ind + width / 2, random_cash_list, rotation = 'vertical')
        plt.legend(loc='best')
        plt.savefig('Beam_Per%02d.png'%(k),dpi=300, bbox_inches='tight')
        k+=20
        plt.show()

    k = 5 
    ## Graphs for beam search efficiency
    for size_result in nodes_processed_list:
        print(size_result)
        N = len(size_result)
        ind = np.arange(N) 
        width = 0.5       
        plt.bar(ind, size_result, width)

        plt.ylabel('Number of Nodes Processed')
        plt.title('Beam_Search_AI_Efficiency %02d'%(k))
        plt.xlabel('Starting cash at each Iteration')
        plt.xticks(ind + width / 2, random_cash_list, rotation = 'vertical')
        plt.legend(loc='best')
        plt.savefig('Beam_Eff%02d.png'%(k),dpi=300, bbox_inches='tight')
        k+=20
        plt.show()
    
    k = 5
    ## Graphs for base line AI performance
    for size_result in game_len_results_basic:
        print(size_result)
        N = len(size_result)
        ind = np.arange(N) 
        width = 0.5       
        plt.bar(ind, size_result, width)

        plt.ylabel('Profit')
        plt.title('BaseLine_AI_performance %02d'%(k))
        plt.xlabel('Starting cash at each Iteration')
        plt.xticks(ind + width / 2, random_cash_list, rotation = 'vertical')
        plt.legend(loc='best')
        plt.savefig('Base_Per%02d.png'%(k),dpi=300, bbox_inches='tight')
        k+=20
        plt.show()

    k = 5    
    ## Graphs for base line AI efficiency
    for size_result in nodes_processed_list_basic:
        print(size_result)
        N = len(size_result)
        ind = np.arange(N) 
        width = 0.5       
        plt.bar(ind, size_result, width)

        plt.ylabel('Number of Nodes Processed')
        plt.title('BaseLine_AI_Efficiency %02d'%(k))
        plt.xlabel('Starting cash at each Iteration')
        plt.xticks(ind + width / 2, random_cash_list, rotation = 'vertical')
        plt.legend(loc='best')
        plt.savefig('Base_Eff%02d.png'%(k),dpi=300, bbox_inches='tight')
        k+=20
        plt.show()

    

