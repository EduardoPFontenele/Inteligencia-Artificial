from class_Problem import Problem
from class_Node import Node, expand
import math
from collections import deque # para implementar fila

failure = Node("failure", path_cost=math.inf) #  nó para indicar falha

# Implementa busca em largura
def depth_first_search(problem):

    # Cria o nó inicial
    node = Node(problem.initial)

    # Verifica se o nó inicial é o objetivo
    if problem.is_goal(node.state):
        return node.path_actions()
    
    # Inicializa a fila com a raiz
    frontier = [node]
    explored = set()

    while frontier:

        node = frontier.pop()
        explored.add(node.state)    # marca o estado do nó como explorado

        # Expande o nó
        for child in expand(problem,node):

            if child.state not in explored:
                if problem.is_goal(child.state):
                    return child.path_actions()
                
                frontier.append(child)

    return failure