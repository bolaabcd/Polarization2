import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import networkx as nx
from types import FunctionType
from networkx.classes.digraph import DiGraph
from networkx.exception import NetworkXError

from polarization_measure import pol_ER_discretized, get_max_pol

# Note: this code needs some refactoring, it was done in a such a way that the tests that used its older versions would still work.

BELIEF_VALUE = "blf"
INFLUENCE_VALUE = "inf"
UPDATE_F = "upf"
TOLERANCE_VALUE = "tol"
COLOR = "color"
GROUP = "group"

# Each node has a tolerance value, the f part of a belief-update-function,  a belief value and 
# an identifier. Each edge has an influence value.
class Society_Graph:
    def __init__(
        self,
        num_agents : int, 
        initial_belief_vector : np.ndarray,
        initial_influence_matrix : np.ndarray,
        initial_fs_matrix : np.ndarray,
        initial_tolerance_matrix : np.ndarray,
        node_colors_vector : np.ndarray = None,
        edge_colors_matrix : np.ndarray = None,
        node_groups_vector : np.ndarray = None,
        see_constant_agents: bool = True,
        constant_agents_tol: bool = False,
        pol_measure : FunctionType = pol_ER_discretized
        ) -> None:
        self.num_agents = num_agents
        self.graph = nx.DiGraph()

        if node_colors_vector is None:
            node_colors_vector = np.full(num_agents, "tab:blue")
        if edge_colors_matrix is None:
            edge_colors_matrix = np.full((num_agents,num_agents), "tab:gray")
        if node_groups_vector is None:
            node_groups_vector = np.full(num_agents, 0)

        initial_belief_vector = np.array(initial_belief_vector)
        initial_influence_matrix = np.array(initial_influence_matrix)
        initial_fs_matrix = np.array(initial_fs_matrix)
        initial_tolerance_matrix = np.array(initial_tolerance_matrix)
        node_colors_vector = np.array(node_colors_vector)
        edge_colors_matrix = np.array(edge_colors_matrix)
        node_groups_vector = np.array(node_groups_vector)

        self.see_constant_agents = see_constant_agents
        self.constant_agents_tol = constant_agents_tol
        self.pol_msr = pol_measure
        self.belief_history = []
        self.polarization_history = []

        self.set_nodes(initial_belief_vector, node_colors_vector, node_groups_vector)
        self.set_edges(initial_influence_matrix, edge_colors_matrix, initial_tolerance_matrix, initial_fs_matrix)

        self.register_state()
        
        # self.set_beliefs(np.array(initial_belief_vector))
        # self.set_influences(np.array(initial_influence_matrix), np.array(edge_colors_matrix))
        # self.set_tolerances(np.array(initial_tolerance_matrix))
        # self.set_fs(np.array(initial_fs_matrix))

    def set_nodes(self, initial_beliefs : np.ndarray, colors : np.ndarray, groups : np.ndarray):
        if len(colors) != self.num_agents:
            raise ValueError("Invalid size of list of node colors.")
        if len(groups) != self.num_agents:
            raise ValueError("Invalid size of list of node groups.")
        for i in range(self.num_agents):
            self.graph.add_node(i, group = groups[i], color = colors[i])
        self.set_beliefs(initial_beliefs)
    def set_beliefs(self, belief_values : np.ndarray) -> None:
        if self.num_agents != len(belief_values):
            raise ValueError("Invalid size of belief values list.")
        for i, val in enumerate(belief_values):
            self.set_belief(i, val)
        # self.register_state()
    def set_belief(self, i : int, val : np.float64) -> None:
        if val > 1 or val < 0:
            raise ValueError("Invalid belief value.")
        self.graph.nodes[i][BELIEF_VALUE] = val
    
    def set_edges(self, initial_influences : np.ndarray, edge_colors : np.ndarray, initial_tolerances : np.ndarray, initial_fs : np.ndarray) -> None:
        if self.num_agents != initial_fs.shape[0]:
            raise ValueError("Invalid size of one-to-one functions matrix.")
        if self.num_agents != initial_fs.shape[1]:
            raise ValueError("Invalid size of one-to-one functions matrix.")
        if self.num_agents != initial_influences.shape[0]:
            raise ValueError("Invalid size of influence matrix.")
        if self.num_agents != initial_influences.shape[1]:
            raise ValueError("Invalid size of influence matrix.")
        if self.num_agents != initial_tolerances.shape[0]:
            raise ValueError("Invalid size of tolerance matrix.")
        if self.num_agents != initial_tolerances.shape[1]:
            raise ValueError("Invalid size of tolerance matrix.")
        if np.any(initial_tolerances < -1) or np.any(initial_tolerances > 1):
            raise ValueError("Invalid tolerance value.")
        if np.any(initial_influences <  0) or np.any(initial_influences > 1):
            raise ValueError("Invalid influence value.")

        for i in range(self.num_agents):
            for j in range(self.num_agents):
                self.set_influence(i, j, initial_influences[i][j])
                if self.graph.has_edge(i, j):
                    self.graph[i][j][UPDATE_F] = initial_fs[i][j]
                    self.graph[i][j][TOLERANCE_VALUE] = initial_tolerances[i][j]
                    self.graph[i][j][COLOR] = edge_colors[i][j]
    def set_influence(self, i : int, j : int, val : np.float64) -> None:
        if val < 0 or val > 1:
            raise ValueError("Invalid influence value.")
        if val != 0:
            if not self.graph.has_edge(i,j):
                self.graph.add_edge(i,j, inf = val)
        elif self.graph.has_edge(i,j):
            self.graph.remove_edge(i,j)

    def register_state(self) -> None: # only saves what can change in our model: the belief values and the polarization measure.
        blfs = self.get_beliefs()
        # print(len(self.get_constant_agents()), self.num_agents, np.array(blfs)[self.get_valid_agents()].shape)
        if np.array(blfs)[self.get_valid_agents()].shape[0] == 0:
            return

        self.belief_history.append(np.array(blfs)[self.get_valid_agents()])
        ignore = []
        if not self.constant_agents_tol:
            ignore = self.get_constant_agents()
        self.polarization_history.append(self.pol_msr(blfs, ignore_these_indexes=ignore)/get_max_pol(self.num_agents - len(ignore)))

    def apply_f(self, nbr : int, n : int, graph = None) -> np.float64:
        if graph is None:
            graph = self.graph
        f = graph.nodes[n][UPDATE_F]
        diff = graph.nodes[nbr][BELIEF_VALUE] - graph.nodes[n][BELIEF_VALUE]
        tol = graph[n][nbr][TOLERANCE_VALUE]
        return f(diff, tol)
    def set_between_0_1(self, n : int) -> None:
        self.graph.nodes[n][BELIEF_VALUE] = max(0,self.graph.nodes[n][BELIEF_VALUE])
        self.graph.nodes[n][BELIEF_VALUE] = min(1,self.graph.nodes[n][BELIEF_VALUE])
    def get_beliefs(self) -> np.ndarray:
        return np.array([self.graph.nodes[n][BELIEF_VALUE] for n in self.graph])

    def update_beliefs_slow(self) -> None:
        graph = self.graph.copy()
        for n in graph:
            if graph.in_degree(n) == 0:
                continue
            sum = 0
            for nbr in graph.predecessors(n):
                sum += self.apply_f(nbr,n,graph)*graph[nbr][n][INFLUENCE_VALUE]
            self.graph.nodes[n][BELIEF_VALUE] += sum/graph.in_degree(n)
            self.set_between_0_1(n)
        self.register_state()

    def quick_update(self, number_of_updates : int) -> None:
        # print(self.belief_history)
        n = self.num_agents

        f0 = 0
        ok = False
        for ed in self.graph.edges:
            f0 = self.graph[ed[0]][ed[1]][UPDATE_F]
            ok = True
            break
        if not ok:
            raise RuntimeError("Invalid state for quick_update: no edges.")

        for i in self.graph.nodes():
            for j in self.graph.predecessors(i):
                if self.graph[j][i][UPDATE_F] != f0:
                    raise RuntimeError("Invalid state for quick_update: not all edges use the same update function.")
        
        blf_mat = [self.graph.nodes[i][BELIEF_VALUE] for i in range(n)]
        blf_mat = np.array(blf_mat)
        tol_mat = nx.convert_matrix.to_numpy_array(self.graph, weight = TOLERANCE_VALUE) # sets to 1 if edge is not specified
        inf_mat = nx.convert_matrix.to_numpy_array(self.graph, weight = INFLUENCE_VALUE) # sets to 1 if edge is not specified
        neighbours = [np.count_nonzero(inf_mat[:, i]) for i, _ in enumerate(blf_mat)]
        for i in range(number_of_updates):
            diff = np.ones((len(blf_mat), 1)) @  np.asarray(blf_mat)[np.newaxis]
            diff = np.transpose(diff) - diff
            preAns = f0(diff,tol_mat)*inf_mat
            preAns = np.add.reduce(preAns) / neighbours # preAns is now how much we will add to each belief value. (the summation part)
            preAns = np.nan_to_num(preAns) # If there are no neighbours, we don't want to change anything, so set NaNs to zero.
            preAns += blf_mat # preAns now contains K_i^{t+1}, for every agent i
            blf_mat = np.clip(preAns,0,1) # preAns now contains B_i^{t+1}, for every agent i
            self.set_beliefs(np.ndarray.tolist(blf_mat))
            self.register_state()


    def get_constant_agents(self) -> np.ndarray:
        constant_agents = []
        for i in range(self.num_agents):
            if self.graph.in_degree(i) == 0:
                constant_agents.append(i)
        return np.array(constant_agents)
    def get_valid_agents(self) -> np.ndarray:
        valids = np.array([True for i in range(self.num_agents)])
        if self.see_constant_agents:
            return valids
        for i in self.get_constant_agents():
            valids[i] = False
        return valids

    def append(self, other : DiGraph) -> None: # also accepts other as Society Graph
        if type(other) is Society_Graph:
            other = other.graph
        n = self.graph.number_of_nodes()
        for i in range(other.number_of_nodes()):
            self.graph.add_node(i+n, color = other.nodes[i][COLOR], group = other.nodes[i][GROUP])
            self.set_belief(i+n, other.nodes[i][BELIEF_VALUE])
        for i,j in other.edges():
            if other[i][j][INFLUENCE_VALUE] != 0:
                self.set_influence(i+n,j+n,other[i][j][INFLUENCE_VALUE])
                self.graph[i+n][j+n][UPDATE_F] = other[i][j][UPDATE_F]
                self.graph[i+n][j+n][TOLERANCE_VALUE] = other[i][j][TOLERANCE_VALUE]
                self.graph[i+n][j+n][COLOR] = other[i][j][COLOR]
        self.num_agents = self.graph.number_of_nodes()
        self.polarization_history = []
        self.belief_history = []
        self.register_state()

    def plot_history(self, ax : plt.Axes = None, fig : plt.Figure = None) -> (plt.Axes, plt.Figure):
        if fig is None and ax is not None:
            raise ValueError("Invalid values: matplotlib ax specified, but figure not specified.")
        if fig is None:
            fig = plt.figure()
        if ax is None:
            ax = fig.add_subplot()
        ax.set_ylim(0,1)
        ax.plot(np.array(self.belief_history))
        valid_ags_list = np.array(range(self.num_agents))[self.get_valid_agents()]
        for i,j in enumerate(ax.lines):
            j.set_color(self.graph.nodes[valid_ags_list[i]][COLOR])

        return ax, fig

    def plot_polarization(self, ax : plt.Axes = None, fig : plt.Figure = None, color : str = 'tab:blue') -> (plt.Axes, plt.Figure):
        if fig is None and ax is not None:
            raise ValueError("Invalid values: matplotlib ax specified, but figure not specified.")
        if fig is None:
            fig = plt.figure()
        if ax is None:
            ax = fig.add_subplot()
        ax.set_ylim(0,1)
        ax.plot(np.array(self.polarization_history), color = color)
        return ax, fig
	
    def plot_hist_pol(self, axt : plt.Axes = None, axb : plt.Axes = None, fig : plt.Figure = None, color : str = 'tab:blue') -> (plt.Axes, plt.Figure):
        if fig is None and axb is not None and axt is not None:
            raise ValueError("Invalid values: matplotlib axes specified, but figure not specified.")
        if fig is None:
            fig = plt.figure()
        if axb is None or axt is None:
            gs = gridspec.GridSpec(3, 1, figure=fig, hspace=0)
            axt = fig.add_subplot(gs[:-1, :])
            axb = fig.add_subplot(gs[-1, :], sharex=axt)
        axb.set_ylim(0,1)
        axt.set_ylim(0,1)
        axt.tick_params(axis='y',colors = 'tab:blue')
        axt.set_yticks([0.2,0.4,0.6,0.8,1])
        axb.tick_params(axis='y', colors = '#770000')
        self.plot_history(ax = axt, fig = fig)
        axt.set_ylabel("Belief")
        self.plot_polarization(ax = axb, fig = fig, color = "#770000")
        axb.set_ylabel("Polarization")
        axb.set_xlabel("Time")
        return axb, axt, fig

    def draw_graph(self) -> None:
        nx.draw(
            self.graph, 
            node_color = [self.graph.nodes[i][COLOR] for i in self.graph.nodes],
            edge_color = [self.graph.edges[i][COLOR] for i in self.graph.edges]
        )
