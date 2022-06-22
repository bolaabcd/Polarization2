import cli_utils as cli
import numpy as np
import os
from matplotlib import pyplot as plt
from numpy.random.mtrand import f
from types import FunctionType

from polarization_measure import pol_ER_discretized
from society_graph import Society_Graph
import default_beliefs,default_fs,default_influences,default_tolerances,belief_update_fs

# Connects each in a to every agents in b
def all_edges(a : list, b : list):
    ans = []
    for i in a:
        for j in b:
            ans.append((i,j))
    return ans

# All agents initially agree completely
def simple_clique_consensus(
        num_agents : int, 
        function : FunctionType,
        consensus_value : np.float64, 
        tolerance_value : np.float64,
        influence_value : np.float64,
        node_color : str = "tab:blue",
        edge_color : str = "tab:gray",
        group_num : int = 0,
        see_constant_agents : bool = True,
        constant_agents_tol : bool = False,
        pol_measure : FunctionType = pol_ER_discretized
    ) -> Society_Graph:
        return Society_Graph(
            num_agents,
            np.array([consensus_value for i in range(num_agents)]),
            default_influences.build_inf_graph_clique(num_agents,influence_value),
            default_fs.same(num_agents,function),
            default_tolerances.build_tol_matrix_constant(num_agents,tolerance_value),
            node_colors_vector = [node_color for i in range(num_agents)],
            edge_colors_matrix = [[edge_color for i in range(num_agents)] for j in range(num_agents)],
            node_groups_vector = [group_num for i in range(num_agents)],
            see_constant_agents = True,
            constant_agents_tol = False,
            pol_measure = pol_measure
        )

# Uniform distribution
def simple_clique_uniform(
        num_agents : int, 
        function : FunctionType,
        start_value : np.float64,
        end_value : np.float64,
        tolerance_value : np.float64,
        influence_value : np.float64,
        node_color : str = "tab:blue",
        edge_color : str = "tab:gray",
        group_num : int = 0,
        see_constant_agents : bool = True,
        constant_agents_tol : bool = False,
        pol_measure : FunctionType = pol_ER_discretized
    ) -> Society_Graph:
        return Society_Graph(
            num_agents,
            default_beliefs.build_belief(default_beliefs.Belief_Type.UNIFORM, num_agents, start_value, end_value),
            default_influences.build_inf_graph_clique(num_agents,influence_value),
            default_fs.same(num_agents,function),
            default_tolerances.build_tol_matrix_constant(num_agents,tolerance_value),
            node_colors_vector = [node_color for i in range(num_agents)],
            edge_colors_matrix = [[edge_color for i in range(num_agents)] for j in range(num_agents)],
            node_groups_vector = [group_num for i in range(num_agents)],
            see_constant_agents = True,
            constant_agents_tol = False,
            pol_measure = pol_measure
        )

# Clique but agents are divided in three opinion groups
def clique_tripartite(
        is_consensus : bool,
        num_agents : int, 
        function : FunctionType,
        belief_value1 : np.float64, 
        belief_value1_end : np.float64,
        belief_value2 : np.float64, 
        belief_value2_end : np.float64,
        belief_value3 : np.float64, 
        belief_value3_end : np.float64,
        influence_value1 : np.float64,
        influence_value2 : np.float64,
        influence_value3 : np.float64,
        influence_value12 : np.float64,
        influence_value21 : np.float64,
        influence_value23 : np.float64,
        influence_value32 : np.float64,
        influence_value13 : np.float64,
        influence_value31 : np.float64,
        tolerance_value1 : np.float64,
        tolerance_value2 : np.float64,
        tolerance_value3 : np.float64,
        tolerance_value12 : np.float64,
        tolerance_value21 : np.float64,
        tolerance_value23 : np.float64,
        tolerance_value32 : np.float64,
        tolerance_value13 : np.float64,
        tolerance_value31 : np.float64,
        see_constant_agents : bool = True,
        constant_agents_tol : bool = False,
        pol_measure : FunctionType = pol_ER_discretized
    ) -> Society_Graph:
        size1 = num_agents//3
        size2 = num_agents-2*size1
        size3 = size1
        group1 = -1
        group2 = -1
        group3 = -1
        if is_consensus:
            group1 = simple_clique_consensus(
                size1,
                function,
                belief_value1,
                tolerance_value1,
                influence_value1,
                node_color = "#ff7777",
                edge_color = "#ff7777",
                group_num = 0,
                see_constant_agents = see_constant_agents,
                constant_agents_tol = constant_agents_tol,
                pol_measure  = pol_measure
            )
            group2 = simple_clique_consensus(
                size2,
                function,
                belief_value2,
                tolerance_value2,
                influence_value2,
                node_color = "#77ff77",
                edge_color = "#77ff77",
                group_num = 1,
                see_constant_agents = see_constant_agents,
                constant_agents_tol = constant_agents_tol,
                pol_measure  = pol_measure
            )
            group3 = simple_clique_consensus(
                size3,
                function,
                belief_value3,
                tolerance_value3,
                influence_value3,
                node_color = "#7777ff",
                edge_color = "#7777ff",
                group_num = 2,
                see_constant_agents = see_constant_agents,
                constant_agents_tol = constant_agents_tol,
                pol_measure  = pol_measure
            )
        else:
            group1 = simple_clique_uniform(
                size1,
                function,
                belief_value1,
                belief_value1_end,
                tolerance_value1,
                influence_value1,
                node_color = "#ff7777",
                edge_color = "#ff7777",
                group_num = 0,
                see_constant_agents = see_constant_agents,
                constant_agents_tol = constant_agents_tol,
                pol_measure  = pol_measure
            )
            group2 = simple_clique_uniform(
                size2,
                function,
                belief_value2,
                belief_value2_end,
                tolerance_value2,
                influence_value2,
                node_color = "#77ff77",
                edge_color = "#77ff77",
                group_num = 1,
                see_constant_agents = see_constant_agents,
                constant_agents_tol = constant_agents_tol,
                pol_measure  = pol_measure
            )
            group3 = simple_clique_uniform(
                size3,
                function,
                belief_value3,
                belief_value3_end,
                tolerance_value3,
                influence_value3,
                node_color = "#7777ff",
                edge_color = "#7777ff",
                group_num = 2,
                see_constant_agents = see_constant_agents,
                constant_agents_tol = constant_agents_tol,
                pol_measure  = pol_measure
            )

        group1.append(group2.graph)
        group1.append(group3.graph)
        edges12 = all_edges(range(size1), range(size1, size1 + size2))
        edges21 = all_edges(range(size1, size1 + size2), range(size1))
        edges23 = all_edges(range(size1, size1 + size2), range(size1 + size2, size1 + size2 + size3))
        edges32 = all_edges(range(size1 + size2, size1 + size2 + size3), range(size1, size1 + size2))
        edges31 = all_edges(range(size1 + size2, size1 + size2 + size3), range(size1))
        edges13 = all_edges(range(size1), range(size1 + size2, size1 + size2 + size3))
        group1.graph.add_edges_from(edges12, inf = influence_value12, tol = tolerance_value12, color = "#773300", upf = function)
        group1.graph.add_edges_from(edges21, inf = influence_value21, tol = tolerance_value21, color = "#337700", upf = function)
        group1.graph.add_edges_from(edges23, inf = influence_value23, tol = tolerance_value23, color = "#007733", upf = function) 
        group1.graph.add_edges_from(edges32, inf = influence_value32, tol = tolerance_value32, color = "#003377", upf = function) 
        group1.graph.add_edges_from(edges31, inf = influence_value31, tol = tolerance_value31, color = "#330077", upf = function) 
        group1.graph.add_edges_from(edges13, inf = influence_value13, tol = tolerance_value13, color = "#770033", upf = function) 
        return group1

# Clique but everyone is influenced by two distinct agents
def clique_two_influencers_uniform(
        num_agents_middle : int, 
        update_function : FunctionType,
        start_value_middle : np.float64,
        end_value_middle : np.float64, 
        tolerance_value_middle : np.float64,
        influence_value_middle : np.float64,
        belief_value_1 : np.float64,
        beleif_value_2 : np.float64,
        influence_value_1mid : np.float64,
        influence_value_2mid : np.float64,
        influence_value_mid1 : np.float64,
        influence_value_mid2 : np.float64,
        tolerance_value_1mid : np.float64,
        tolerance_value_2mid : np.float64,
        tolerance_value_mid1 : np.float64,
        tolerance_value_mid2 : np.float64,
        constant_influencers : bool,
        see_constant_agents: bool = True,
        constant_agents_tol: bool = False,
        pol_measure : FunctionType = pol_ER_discretized
    ) -> Society_Graph:
    influencers = Society_Graph(
        2,
        [belief_value_1, beleif_value_2], 
        np.full((2,2),0.0),
        default_fs.same(2,update_function),
        [[1, 1], [1, 1]], 
        node_colors_vector = ["#ff0000", "#00ff00"],
        edge_colors_matrix = [["#ff3333" for i in range(2)] for j in range(2)],
        node_groups_vector = [0, 1],
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure = pol_measure
    )

    middle = simple_clique_uniform(
        num_agents_middle,
        update_function,
        start_value_middle,
        end_value_middle,
        tolerance_value_middle,
        influence_value_middle,
        node_color = "#00ff00",
        edge_color = "#33ff33",
        group_num = 2,
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure  = pol_measure
    )

    result = influencers
    result.append(middle)
    edges1 = all_edges([0],range(2, num_agents_middle + 2))
    edges2 = all_edges([1],range(2, num_agents_middle + 2))
    result.graph.add_edges_from(edges1, inf = influence_value_1mid, tol = tolerance_value_1mid, color = "#ff7700", upf = update_function)
    result.graph.add_edges_from(edges2, inf = influence_value_2mid, tol = tolerance_value_2mid, color = "#0077ff", upf = update_function)
    if not constant_influencers:
        result.graph.add_edge(2, 0, inf = influence_value_mid1, tol = tolerance_value_mid1, color = "#77ff00", upf = update_function)
        result.graph.add_edge(num_agents_middle + 1, 1, inf = influence_value_mid2, tol = tolerance_value_mid2, color = "#00ff77", upf = update_function)
    return result

# Clique but everyone is influenced by one agent
def clique_one_influencer_uniform(
        num_agents_middle : int, 
        update_function : FunctionType,
        belief_value_1 : np.float64,
        start_value_middle : np.float64,
        end_value_middle : np.float64, 
        influence_value_middle : np.float64,
        influence_value_1mid : np.float64,
        influence_value_mid1 : np.float64,
        tolerance_value_middle : np.float64,
        tolerance_value_1mid : np.float64,
        tolerance_value_mid1 : np.float64,
        constant_influencer : bool,
        see_constant_agents: bool = True,
        constant_agents_tol: bool = False,
        pol_measure : FunctionType = pol_ER_discretized
    ):
    influencer = Society_Graph(
        1,
        [belief_value_1], 
        np.full((1,1),0.0),
        default_fs.same(1,update_function),
        [[1]], 
        node_colors_vector = ["#ff0000" for i in range(1)],
        edge_colors_matrix = [["#ff3333" for i in range(1)] for j in range(1)],
        node_groups_vector = [0],
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure = pol_measure
    )

    middle = simple_clique_uniform(
        num_agents_middle,
        update_function,
        start_value_middle,
        end_value_middle,
        tolerance_value_middle,
        influence_value_middle,
        node_color = "#00ff00",
        edge_color = "#33ff33",
        group_num = 1,
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure  = pol_measure
    )

    result = influencer
    result.append(middle)
    edges1 = all_edges([0],range(1, num_agents_middle + 1))
    result.graph.add_edges_from(edges1, inf = influence_value_1mid, tol = tolerance_value_1mid, color = "#ff7700", upf = update_function)
    if not constant_influencer:
        result.graph.add_edge(1, 0, inf = influence_value_mid1, tol = tolerance_value_mid1, color = "#77ff00", upf = update_function)
    return result

# Two groups influence and are influenced by another one
def simple_tripartite(
        num_agents : int, 
        function : FunctionType,
        consensus_value1 : np.float64, 
        consensus_value2 : np.float64, 
        consensus_value3 : np.float64, 
        influence_value1 : np.float64,
        influence_value2 : np.float64,
        influence_value3 : np.float64,
        influence_value12 : np.float64,
        influence_value21 : np.float64,
        influence_value23 : np.float64,
        influence_value32 : np.float64,
        tolerance_value1 : np.float64,
        tolerance_value2 : np.float64,
        tolerance_value3 : np.float64,
        tolerance_value12 : np.float64,
        tolerance_value21 : np.float64,
        tolerance_value23 : np.float64,
        tolerance_value32 : np.float64,
        see_constant_agents: bool = True,
        constant_agents_tol: bool = False,
        pol_measure : FunctionType = pol_ER_discretized
    ) -> Society_Graph:
        size1 = num_agents//3
        size2 = num_agents-2*size1
        size3 = size1
        group1 = simple_clique_consensus(
            size1,
            function,
            consensus_value1,
            tolerance_value1,
            influence_value1,
            node_color = "#ff7777",
            edge_color = "#ff7777",
            group_num = 0,
            see_constant_agents = see_constant_agents,
            constant_agents_tol = constant_agents_tol,
            pol_measure  = pol_measure
        )
        group2 = simple_clique_consensus(
            size2,
            function,
            consensus_value2,
            tolerance_value2,
            influence_value2,
            node_color = "#77ff77",
            edge_color = "#77ff77",
            group_num = 1,
            see_constant_agents = see_constant_agents,
            constant_agents_tol = constant_agents_tol,
            pol_measure  = pol_measure
        )
        group3 = simple_clique_consensus(
            size3,
            function,
            consensus_value3,
            tolerance_value3,
            influence_value3,
            node_color = "#7777ff",
            edge_color = "#7777ff",
            group_num = 2,
            see_constant_agents = see_constant_agents,
            constant_agents_tol = constant_agents_tol,
            pol_measure  = pol_measure
        )

        group1.append(group2.graph)
        group1.append(group3.graph)
        edges12 = all_edges(range(size1), range(size1, size1 + size2))
        edges21 = all_edges(range(size1, size1 + size2), range(size1))
        edges23 = all_edges(range(size1, size1 + size2), range(size1 + size2, size1 + size2 + size3))
        edges32 = all_edges(range(size1 + size2, size1 + size2 + size3), range(size1, size1 + size2))
        group1.graph.add_edges_from(edges12, inf = influence_value12, tol = tolerance_value12, color = "#773300", upf = function)
        group1.graph.add_edges_from(edges21, inf = influence_value21, tol = tolerance_value21, color = "#337700", upf = function)
        group1.graph.add_edges_from(edges23, inf = influence_value23, tol = tolerance_value23, color = "#007733", upf = function) 
        group1.graph.add_edges_from(edges32, inf = influence_value32, tol = tolerance_value32, color = "#003377", upf = function) 
        return group1

# One of the groups has a influencer talking to it
def tripartite_one_influencer(
        num_ags_middle : int,
        belief_value1 : np.float64,
        belief_value2 : np.float64,
        update_function : np.float64,
        influence_value_mid : np.float64,
        influence_value_1mid : np.float64,
        influence_value_mid1 : np.float64,
        tolerance_value_mid : np.float64,
        tolerance_value_1mid : np.float64,
        tolerance_value_mid1 : np.float64,
        constant_influencer : bool,
        see_constant_agents: bool = True,
        constant_agents_tol: bool = False,
        pol_measure : FunctionType = pol_ER_discretized
    ) -> Society_Graph:
    result = Society_Graph(
        1,
        [belief_value1], 
        np.full((1,1),0),
        default_fs.same(1,update_function),
        [[1]], 
        node_colors_vector = ["#ff0000" for i in range(1)],
        edge_colors_matrix = [["#ff3333" for i in range(1)] for j in range(1)],
        node_groups_vector = [0],
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure = pol_measure
    )
    
    middle = simple_tripartite(
        num_ags_middle, 
        update_function,
        belief_value1, 
        (belief_value1 + belief_value2)/2,
        belief_value2, 
        influence_value_mid,
        influence_value_mid,
        influence_value_mid,
        influence_value_mid,
        influence_value_mid,
        influence_value_mid,
        influence_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure  = pol_measure
    )

    size1 = num_ags_middle//3
    group_1 = range(1,1+size1)
    edg_1 = all_edges([0],group_1)

    result.append(middle)
    result.graph.add_edges_from(edg_1, inf = influence_value_1mid, tol = tolerance_value_1mid, color = "#ff0000", upf = update_function)
    if not constant_influencer:
        result.graph.add_edge(2, 0, inf = influence_value_mid1, tol = tolerance_value_mid1, color = "#00ffff", upf = update_function)
    return result


# The two non-middle groups have influencers talking to them
def tripartite_two_influencers(
        num_ags_middle : int,
        belief_value1 : np.float64,
        belief_value2 : np.float64,
        update_function : np.float64,
        influence_value_mid : np.float64,
        influence_value_1mid : np.float64,
        influence_value_2mid : np.float64,
        influence_value_mid1 : np.float64,
        influence_value_mid2 : np.float64,
        tolerance_value_1mid : np.float64,
        tolerance_value_2mid : np.float64,
        tolerance_value_mid1 : np.float64,
        tolerance_value_mid2 : np.float64,
        tolerance_value_mid : np.float64,
        constant_influencers : bool,
        see_constant_agents: bool = True,
        constant_agents_tol: bool = False,
        pol_measure : FunctionType = pol_ER_discretized
    ):
    result = Society_Graph(
        2,
        [blf1_value, blf2_value], 
        np.full((2,2),0),
        default_fs.same(2,update_function), 
        [[1, 1], [1, 1]], 
        node_colors_vector = ["#ff0000", "#0000ff"],
        edge_colors_matrix = [["#ff3333" for i in range(2)] for j in range(2)],
        node_groups_vector = [0, 1],
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure = pol_measure
    )
    
    middle = simple_tripartite(
        num_ags_middle, 
        update_function,
        belief_value1, 
        (belief_value1 + belief_value2)/2,
        belief_value2, 
        influence_value_mid,
        influence_value_mid,
        influence_value_mid,
        influence_value_mid,
        influence_value_mid,
        influence_value_mid,
        influence_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        tolerance_value_mid,
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure  = pol_measure
    )

    size1 = num_ags_middle//3
    group_1 = range(2, 2 + size1)
    group_2 = range(2 + num_ags_middle-size1, 2 + num_ags_middle)
    edg_1 = all_edges([0], group_1)
    edg_2 = all_edges([1], group_2)

    result.append(middle)
    result.graph.add_edges_from(edg_1, inf = influence_value_1mid, tol = tolerance_value_1mid, color = "#ff5555", upf = update_function)
    result.graph.add_edges_from(edg_2, inf = influence_value_2mid, tol = tolerance_value_2mid, color = "#5555ff", upf = update_function)

    if not constant_influencers:
        result.graph.add_edge(2, 0, inf = influence_value_mid1, tol = tolerance_value_mid1, color = "#55ffff", upf = update_function)
        result.graph.add_edge(num_ags_middle + 1, 1, inf = influence_value_mid2, tol = tolerance_value_mid2, color = "#ffff55", upf = update_function)
    return result


# many_graphs is a tuple: Gr and name of the graph
# Gr is a list of parameters: (resulting_graphs,parameter)
# resulting_graphs is a list of Society_graphs
def simulate(many_graphs):
    Gr, name = graph
    Gr[0][0][0].draw_graph()
    if not os.path.exists(f"./generated/{name}/"):
        os.mkdir(f"./generated/{name}/")
    if not os.path.exists(f"./generated/{name}/{name}.png"):
        plt.savefig(f"./generated/{name}/{name}.png")
    plt.close()
    for i in cli.ProgressRange(len(Gr),"parameters"):
        if os.path.exists(f"./generated/{name}/{Gr[i][1]}/"):
            continue
        for j in range(len(Gr[i][0])):
            # Gr[i][0][j].quick_update(100)
            for k in range(100):
                Gr[i][0][j].update_beliefs()
            Gr[i][0][j].plot_history()
            file_name = f"./generated/{name}/{Gr[i][1]}/"
            if not os.path.exists(file_name):
                os.mkdir(file_name)
            if not os.path.exists(file_name+f"{j}.png"):
                plt.savefig(file_name+f"{j}.png")
            plt.close()
            Gr[i][0][j].plot_polarization()
            file_name = f"./generated/{name}/pol_{Gr[i][1]}/"
            if not os.path.exists(file_name):
                os.mkdir(file_name)
            if not os.path.exists(file_name+f"{j}.png"):
                plt.xlim([0,len(Gr[i][0][j].polarization_history)-1])
                plt.ylim([ 0,1])
                plt.savefig(file_name+f"{j}.png")
            plt.close()
