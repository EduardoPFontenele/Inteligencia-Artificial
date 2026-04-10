class Problem:
    # Construtor
    def __init__(self, initial = None, goal = None, **kwds):
        
        # Variáveis de instância
        self.initial = initial
        self.goal = goal

        for key, value in kwds.items():
            # Função para criar variaveis de instância com a chave e valor de um dicionario
            setattr(self,key,value)

    # Ações possíveis a partir de um estado
    def actions(self,state):
        raise NotImplementedError
    
    # Quanto custa ir de um estado para outro
    def action_cost(self, state, action):
        return 1

    # Resultado de uma ação a partir de um estado
    def successor(self, state, action):
        raise NotImplementedError

    # Verifica se um estado é um estado objetivo
    def is_goal(self, state):
        if state == self.goal:
            return True
        
        return False
    
    # sempre que printar um objeto da classe Problem, mostra o print da forma que está na função
    def __repr__(self):
        return f"Problem(initial = {self.initial!r}, goal = {self.goal!r})"