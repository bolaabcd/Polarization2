import numpy as np
import networkx as nx

BELIEF_VALUE = "blf"
INFLUENCE_VALUE = "inf"
UPDATE_FUNCTION = "upfun"
TOLERANCE_VALUE = "tol"

# Each node has a tolerance value, an update-function, a belief value and a identifier.
# Each edge has a influence value.
class Society_Graph:
    def __init__(
        self, 
        num_agents : int, 
        initial_belief : list,
        initial_influence : np.ndarray,
        initial_tolerance : list,
        ):
        self.num_agents = num_agents
        self.graph = nx.DiGraph()
        self.set_beliefs(initial_belief)
        self.set_influences(initial_influence)
        self.set_tolerances(initial_tolerance)


    def set_beliefs(self, belief_list : list):
        pass
    def set_influences(self, influence_matrix: np.ndarray):
        pass
    def set_tolerances(self, tolerance_list : list):
        pass
    def apply_function(self, nbr, n):
        func = self.graph[n][UPDATE_FUNCTION]
        diff = self.graph[nbr][BELIEF_VALUE] - self.graph[n][BELIEF_VALUE]
        tol = self.graph[nbr][TOLERANCE_VALUE]
        return func(diff,tol)
        
    def set_inside_interval(self, n):
        self.graph[n][BELIEF_VALUE] = max(0,self.graph[n][BELIEF_VALUE])
        self.graph[n][BELIEF_VALUE] = min(1,self.graph[n][BELIEF_VALUE])
    
    def update(self):
        for n in self.graph:
            sum = 0
            for nbr,blf in self.graph.pred[n].data(BELIEF_VALUE):
                sum += self.apply_function(nbr,n)*self.graph[nbr][n][INFLUENCE_VALUE]
            self.graph[n][BELIEF_VALUE] += sum/self.graph.in_degree(n)
            self.set_inside_interval(n)