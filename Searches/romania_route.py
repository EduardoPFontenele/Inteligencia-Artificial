from class_Problem import Problem
from class_Node import Node,expand
from BFS import breadth_first_search

class Map:
    # Construtor
    def __init__(self):
        self.graph = {
            'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
            'Zerind': {'Arad': 75, 'Oradea': 71},
            'Oradea': {'Zerind': 71, 'Sibiu': 151},
            'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
            'Timisoara': {'Arad': 118, 'Lugoj': 111},
            'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
            'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
            'Drobeta': {'Mehadia': 75, 'Craiova': 120},
            'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
            'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
            'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
            'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
            'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Urziceni': 85, 'Giurgiu': 90},
            'Giurgiu': {'Bucharest': 90},
            'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
            'Vaslui': {'Urziceni': 142, 'Iasi': 92},
            'Iasi': {'Vaslui': 92, 'Neamt': 87},
            'Neamt': {'Iasi': 87},
            'Hirsova': {'Urziceni': 98, 'Eforie': 86},
            'Eforie': {'Hirsova': 86}
        }

    def get_neighbors(self, city):
        # Retorna uma cidade, caso não tenha visinhos, retona um dicionário vazio
        return self.graph.get(city, {})
    
class RouteRomania(Problem):

    # Construtor da classe com herança
    def __init__(self, initial=None, goal=None, **kwds):
        super().__init__(initial, goal, **kwds)
        self.map = Map()

    def actions(self, state):
        return list(self.map.get_neighbors(state).keys())

    def successor(self, state, action):
        possible_actions = self.actions(state)
        
        if action in possible_actions:
            return action
        
        return state
    
    def action_cost(self, state, action):
        return self.map.get_neighbors(state)[action]
    
if __name__ == "__main__":
    problem = RouteRomania(initial='Arad', goal ='Neamt')
    solution = breadth_first_search(problem)
    print("Solução encontrada:", solution)