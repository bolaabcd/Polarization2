from types import FunctionType
from networkx.classes.digraph import DiGraph
from networkx.exception import NetworkXError
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from polarization_measure import pol_ER_discretized, get_max_pol

# Note: this code needs some refactoring, it was done in a such a way that the tests that used its older versions would still work.

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
        initial_tolerance,
        initial_fs,
        backfire_effect: bool = True, # False means boomerang effect
        node_color : str = "tab:blue",
        edge_color : str = "tab:gray",
        see_constant_agents: bool = True
        ):
        self.belief_history = []
        self.polarization_history = []
        self.pol = pol_ER_discretized
        self.num_agents = num_agents
        self.graph = nx.DiGraph()
        self.node_color = node_color
        self.edge_color = edge_color
        for i in range(num_agents):
            self.graph.add_node(i,subset = 0, node_color = node_color)
        if type(initial_tolerance[0]) != type((1,1)):
            initial_tolerance = zip(initial_tolerance, initial_tolerance)
        self.see_constant_agents = see_constant_agents
        if backfire_effect:
            self.backfire_effect = 0
        else:
            self.backfire_effect = 1
        self.set_beliefs(initial_belief)
        self.set_influences(initial_influence)
        self.set_tolerances(initial_tolerance)
        self.set_fs(initial_fs)
        self.subsets = 1

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
        self.belief_history.append(list(np.array(self.get_beliefs())[self.get_valid_agents()]))
        constant_agents = []
        for i in range(self.num_agents):
            if self.graph.in_degree(i) == 0:
                constant_agents.append(i)
        self.polarization_history.append(self.pol(self.get_beliefs(),ignore_these_indexes=self.get_constant_agents())/get_max_pol(self.num_agents-len(self.get_constant_agents())))
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
                self.set_influence(i,j,influence_matrix[i][j], self.edge_color)
    def set_influence(self, i : int, j : int, val : float, color : str):
        if val < 0 or val > 1:
            raise ValueError("Invalid influence value.")
        if val != 0:
            if not self.graph.has_edge(i,j):
                self.graph.add_edge(i,j, edge_color = color)
            self.graph[i][j][INFLUENCE_VALUE] = val
        else:
            try:
                self.graph.remove_edge(i,j)
            except NetworkXError:
                pass
    
    def set_tolerances(self, tolerance_list):
        if type(tolerance_list) == type(np.array([])) and len(tolerance_list.shape) == 2:
            if self.num_agents != len(tolerance_list) or self.num_agents != len(tolerance_list[0]):
                raise ValueError("Invalid size of tolerance list.")
            for i in range(self.num_agents):
                for j in range(self.num_agents):
                    self.set_tolerance(i,j,tolerance_list[i][j])
        else:
            if self.num_agents != len(tolerance_list):
                raise ValueError("Invalid size of tolerance list.")
            for i, val in enumerate(tolerance_list):
                self.set_tolerance(i, val)
    def set_tolerance(self, i : int, val : tuple, val2 = None):
        if val2 == None:
            if type(val) == type((0,0)):
                if val[0] < -1 or val[0] > 1 or val[1] < -1 or val[1] > 1:
                    raise ValueError("Invalid tolerance value.")
            else:
                raise ValueError("Invalid tolerance value.")

            for j in self.graph.neighbors(i):
                if self.backfire_effect:
                    self.graph[j][i][TOLERANCE_VALUE] = val[0]
                else:
                    self.graph[i][j][TOLERANCE_VALUE] = val[1]
        else:
            j, val = val, val2
            self.graph[i][j][TOLERANCE_VALUE] = val
    
    def apply_f(self, nbr : int, n : int, graph = None):
        if graph == None:
            graph = self.graph
        f = graph.nodes[n][UPDATE_F]
        diff = graph.nodes[nbr][BELIEF_VALUE] - graph.nodes[n][BELIEF_VALUE]
        tol = graph[n][nbr][TOLERANCE_VALUE]
        return f(diff, tol)
        
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
        valids = self.get_valid_agents()
        self.belief_history.append(list(np.array(self.get_beliefs())[valids]))
        constant_agents = []
        for i in range(self.num_agents):
            if self.graph.in_degree(i) == 0:
                constant_agents.append(i)
        self.polarization_history.append(self.pol(self.get_beliefs(),ignore_these_indexes=self.get_constant_agents())/get_max_pol(self.num_agents-len(self.get_constant_agents())))

    def quick_update(self, number_of_updates):
        n = self.num_agents
        f0 = self.graph.nodes[0][UPDATE_F]

        for i in range(self.graph.number_of_nodes()):
            if self.graph.nodes[i][UPDATE_F] != f0:
                raise RuntimeError("Invalid state for quick_update: not all agents use the same update function.")
        blf_mat = [self.graph.nodes[i][BELIEF_VALUE] for i in range(self.graph.number_of_nodes())]
        blf_mat = np.array(blf_mat)
        tol_mat = nx.convert_matrix.to_numpy_array(self.graph,weight=TOLERANCE_VALUE)
        inf_mat = nx.convert_matrix.to_numpy_array(self.graph,weight=INFLUENCE_VALUE)
        neighbours = [np.count_nonzero(inf_mat[:, i]) for i, _ in enumerate(blf_mat)]
        valids = self.get_valid_agents()
        for i in range(number_of_updates):
            diff = np.ones((len(blf_mat), 1)) @  np.asarray(blf_mat)[np.newaxis]
            diff = np.transpose(diff) - diff
            preAns = f0(diff,tol_mat)*inf_mat
            preAns = np.add.reduce(preAns) / neighbours
            preAns = np.nan_to_num(preAns)
            preAns += blf_mat
            blf_mat = np.clip(preAns,0,1)
            self.belief_history.append(np.ndarray.tolist(blf_mat[valids]))
            constant_agents = []
            for i in range(self.num_agents):
                if self.graph.in_degree(i) == 0:
                    constant_agents.append(i)
            self.polarization_history.append(self.pol(np.ndarray.tolist(blf_mat),ignore_these_indexes=self.get_constant_agents())/get_max_pol(self.num_agents-len(self.get_constant_agents())))
        self.set_beliefs(np.ndarray.tolist(blf_mat))
    def get_valid_agents(self):
        valids = [True for i in range(self.num_agents)]
        if self.see_constant_agents:
            return valids
        for i in self.get_constant_agents():
            valids[i] = False
        return valids
    def plot_history(self):
        plt.plot(self.belief_history)
    
    def plot_polarization(self):
        plt.plot(self.polarization_history)

    def append(self, other : DiGraph): # also accepts other as Society Graph
        if type(other) is Society_Graph:
            assert(other.backfire_effect == self.backfire_effect)
            other = other.graph
        n = self.graph.number_of_nodes()
        for i in range(other.number_of_nodes()):
            self.graph.add_node(i+n, node_color = other.nodes[i]["node_color"])
            self.set_belief(i+n,other.nodes[i][BELIEF_VALUE])
            self.set_f(i+n,other.nodes[i][UPDATE_F])
            self.graph.nodes[i+n]['subset'] = self.subsets
        for i,j in other.edges():
            self.set_influence(i+n,j+n,other[i][j][INFLUENCE_VALUE], other[i][j]["edge_color"])
            self.set_tolerance(i+n,j+n,other[i][j][TOLERANCE_VALUE])
        self.num_agents = self.graph.number_of_nodes()
        self.belief_history = [list(np.array(self.get_beliefs())[self.get_valid_agents()])]
        self.polarization_history = [self.pol(self.get_beliefs(),ignore_these_indexes=self.get_constant_agents())/get_max_pol(self.num_agents-len(self.get_constant_agents()))]
        self.subsets += 1
    
    def get_constant_agents(self):
        constant_agents = []
        for i in range(self.num_agents):
            if self.graph.in_degree(i) == 0:
                constant_agents.append(i)
        return constant_agents
    
    def draw_graph(self):
        nx.draw(
            self.graph, 
            node_color = [self.graph.nodes[i]["node_color"] for i in self.graph.nodes],
            edge_color = [self.graph.edges[i]["edge_color"] for i in self.graph.edges]
        )