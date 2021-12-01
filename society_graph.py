import numpy as np
import networkx as nx

BELIEF_VALUE = "blf"
INFLUENCE_VALUE = "inf"
UPDATE_FUNCTION = "upfun"
TOLERANCE_VALUE = "tol"

# Each node has a tolerance value, an update-function, a belief value and an identifier.
# Each edge has an influence value.
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
        if self.num_agents != len(belief_list):
            raise ValueError("Invalid size of belief list.")
        for i, val in enumerate(belief_list):
            self.set_belief(i, val)
    def set_belief(self, i, val):
        self.graph[i][BELIEF_VALUE] = val
    
    def set_influences(self, influence_matrix: np.ndarray):
        if self.num_agents != influence_matrix.shape[0]:
            raise ValueError("Invalid size of influence matrix.")
        if self.num_agents != influence_matrix.shape[1]:
            raise ValueError("Invalid size of influence matrix.")
        
        for i in range(influence_matrix.shape[0]):
            for j in range(influence_matrix.shape[1]):
                self.set_influence(i,j,influence_matrix[i][j])
    def set_influence(self, i, j, val):
        self.graph[i][j][INFLUENCE_VALUE] = val
    
    def set_tolerances(self, tolerance_list : list):
        if self.num_agents != len(tolerance_list):
            raise ValueError("Invalid size of tolerance list.")
        for i, val in enumerate(tolerance_list):
            self.set_tolerance(i, val)
    def set_tolerance(self, i, val):
        self.graph[i][TOLERANCE_VALUE] = val
    
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
            for nbr in self.graph.predecessors():
                sum += self.apply_function(nbr,n)*self.graph[nbr][n][INFLUENCE_VALUE]
            self.graph[n][BELIEF_VALUE] += sum/self.graph.in_degree(n)
            self.set_inside_interval(n)