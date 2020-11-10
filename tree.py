import player as p

class TreeNode:
    def __init__(self):
        # self.test = '[p['


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