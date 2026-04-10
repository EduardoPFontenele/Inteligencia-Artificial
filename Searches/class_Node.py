class Node:
    # Construtor
    def __init__(self, state, parent = None, action = None, path_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    # Retorna a sequência de ações para chegar a este nó
    def path_actions(self):
        # Se o nó não tem pai
        if self.parent is None:
            return []
        
        else:
            return self.parent.path_actions() + [self.action]
    
    # Retorna a sequência de estados para chegar a este nó
    def path_states(self):
        if self.parent is None:
            return []
        
        else:
            return self.parent.path_states() + [self.state]
    
    # sempre que printar um objeto da classe Node, mostra o print da forma que está na função
    def __repr__(self):
        return f"Node({self.state!r})"

# Expande o nó usando ações do problema
def expand(problem,node):

    state = node.state
    
    for action in problem.actions(state):
        
        next_state = problem.successor(state,action)
        cost = node.path_cost + problem.action_cost(state,action)
        yield Node(next_state, node, action, cost)