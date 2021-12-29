from types import FunctionType
from networkx.classes import graph
from networkx.classes.digraph import DiGraph
from networkx.exception import NetworkXError
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

BELIEF_VALUE = "blf"
INFLUENCE_VALUE = "inf"
UPDATE_F = "upf"
TOLERANCE_VALUE = "tol"

# Each node has a tolerance value, the f part of a belief-update-function,  a belief value and 
# an identifier. Each edge has an influence value.
class Society_Graph:
    def __init__(
        self, 
        num_agents : int, 
        initial_belief : list,
        initial_influence : np.ndarray,
        initial_tolerance : list,
        initial_fs : list
        ):
        self.belief_history = []
        self.num_agents = num_agents
        self.graph = nx.DiGraph()
        for i in range(num_agents):
            self.graph.add_node(i)
        self.set_beliefs(initial_belief)
        self.set_influences(initial_influence)
        self.set_tolerances(initial_tolerance)
        self.set_fs(initial_fs)

    def set_fs(self,fs_list : list):
        if self.num_agents != len(fs_list):
            raise ValueError("Invalid size of fs list.")
        for i, fun in enumerate(fs_list):
            self.set_f(i, fun)
    def set_f(self, i : int, fun : FunctionType):
        self.graph.nodes[i][UPDATE_F] = fun

    def set_beliefs(self, belief_list : list):
        if self.num_agents != len(belief_list):
            raise ValueError("Invalid size of belief list.")
        for i, val in enumerate(belief_list):
            self.set_belief(i, val)
        self.belief_history.append(self.get_beliefs())
    def set_belief(self, i : int, val : float):
        if val > 1 or val < 0:
            raise ValueError("Invalid belief value.")
        self.graph.nodes[i][BELIEF_VALUE] = val
    
    def set_influences(self, influence_matrix: np.ndarray):
        if self.num_agents != influence_matrix.shape[0]:
            raise ValueError("Invalid size of influence matrix.")
        if self.num_agents != influence_matrix.shape[1]:
            raise ValueError("Invalid size of influence matrix.")
        
        for i in range(influence_matrix.shape[0]):
            for j in range(influence_matrix.shape[1]):
                self.set_influence(i,j,influence_matrix[i][j])
    def set_influence(self, i : int, j : int, val : float):
        if val < 0 or val > 1:
            raise ValueError("Invalid influence value.")
        if val != 0:
            if not self.graph.has_edge(i,j):
                self.graph.add_edge(i,j)
            self.graph[i][j][INFLUENCE_VALUE] = val
        else:
            try:
                self.graph.remove_edge(i,j)
            except NetworkXError:
                pass
    
    def set_tolerances(self, tolerance_list : list):
        if self.num_agents != len(tolerance_list):
            raise ValueError("Invalid size of tolerance list.")
        for i, val in enumerate(tolerance_list):
            self.set_tolerance(i, val)
    def set_tolerance(self, i : int, val : float):
        if val < -1 or val > 1:
            raise ValueError("Invalid tolerance value.")
        self.graph.nodes[i][TOLERANCE_VALUE] = val
    
    def apply_f(self, nbr : int, n : int, graph = None):
        if graph == None:
            graph = self.graph
        f = graph.nodes[n][UPDATE_F]
        diff = graph.nodes[nbr][BELIEF_VALUE] - graph.nodes[n][BELIEF_VALUE]
        tol = graph.nodes[n][TOLERANCE_VALUE]
        return f(diff,tol) # x, k
        
    def set_between_0_1(self, n : int):
        self.graph.nodes[n][BELIEF_VALUE] = max(0,self.graph.nodes[n][BELIEF_VALUE])
        self.graph.nodes[n][BELIEF_VALUE] = min(1,self.graph.nodes[n][BELIEF_VALUE])
    
    def get_beliefs(self):
        return [self.graph.nodes[n][BELIEF_VALUE] for n in self.graph]

    def update_beliefs(self):
        graph = self.graph.copy()
        for n in graph:
            if graph.in_degree(n) == 0:
                continue
            sum = 0
            for nbr in graph.predecessors(n):
                sum += self.apply_f(nbr,n,graph)*graph[nbr][n][INFLUENCE_VALUE]
            self.graph.nodes[n][BELIEF_VALUE] += sum/graph.in_degree(n)
            self.set_between_0_1(n)
        self.belief_history.append(self.get_beliefs())

    def quick_update(self, number_of_updates):
        n = self.num_agents
        f0 = self.graph.nodes[0][UPDATE_F]
        for i in range(self.graph.number_of_nodes()):
            if self.graph.nodes[i][UPDATE_F] != f0:
                raise RuntimeError("Invalid state for quick_update: not all agents use the same update function.")
        blf_mat = [self.graph.nodes[i][BELIEF_VALUE] for i in range(self.graph.number_of_nodes())]
        blf_mat = np.array(blf_mat)
        tol_mat = np.full((n, n), 0) + np.array([self.graph.nodes[i][TOLERANCE_VALUE]  for i in range(self.graph.number_of_nodes())])[np.newaxis,:]
        inf_mat = nx.convert_matrix.to_numpy_array(self.graph,weight=INFLUENCE_VALUE)
        neighbours = [np.count_nonzero(inf_mat[:, i]) for i, _ in enumerate(blf_mat)]

        for i in range(number_of_updates):
            diff = np.ones((len(blf_mat), 1)) @  np.asarray(blf_mat)[np.newaxis]
            diff = np.transpose(diff) - diff
            preAns = f0(diff,tol_mat)*inf_mat
            preAns = np.add.reduce(preAns) / neighbours
            preAns = np.nan_to_num(preAns)
            preAns += blf_mat
            blf_mat = np.clip(preAns,0,1)
            self.belief_history.append(np.ndarray.tolist(blf_mat))
        self.set_beliefs(np.ndarray.tolist(blf_mat))

    def plot_history(self):
        plt.plot(self.belief_history)

    def append(self, other : DiGraph):
        if type(other) is Society_Graph:
            other = other.graph
        n = self.graph.number_of_nodes()
        for i in range(other.number_of_nodes()):
            self.graph.add_node(i+n)
            self.set_belief(i+n,other.nodes[i][BELIEF_VALUE])
            self.set_tolerance(i+n,other.nodes[i][TOLERANCE_VALUE])
            self.set_f(i+n,other.nodes[i][UPDATE_F])
        for i,j in other.edges():
            self.set_influence(i+n,j+n,other[i][j][INFLUENCE_VALUE])
        self.num_agents = self.graph.number_of_nodes()
        self.belief_history = [self.get_beliefs()]
    
    def draw_graph(self):
        nx.draw(self.graph)