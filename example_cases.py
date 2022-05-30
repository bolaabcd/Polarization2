from types import FunctionType
from matplotlib import pyplot as plt
from numpy.random.mtrand import f
from society_graph import Society_Graph
import cli_utils as cli
import numpy as np
import os
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
        num_agents, 
        function,
        consensus_value, 
        tolerance_value,
        influence_value,
    ):
        return Society_Graph(
            num_agents,
            np.array([consensus_value for i in range(num_agents)]),
            default_influences.build_inf_graph_clique(num_agents,influence_value),
            default_tolerances.build_tol_list_constant(num_agents,tolerance_value),
            default_fs.same(num_agents,function)
        )

# Uniform distribution
def simple_clique_uniform(
        num_agents, 
        function,
        start_value,
        end_value, 
        tolerance_value,
        influence_value,
    ):
        return Society_Graph(
            num_agents,
            np.array([start_value+(end_value-start_value)*i/(num_agents-1) for i in range(num_agents)]),
            default_influences.build_inf_graph_clique(num_agents,influence_value),
            default_tolerances.build_tol_list_constant(num_agents,tolerance_value),
            default_fs.same(num_agents,function)
        )

# Clique but agents are divided in three opinion groups
def clique_tripartite(
        consensus,
        num_agents, 
        function,
        belief_value1, 
        belief_value1_end,
        belief_value2, 
        belief_value2_end,
        belief_value3, 
        belief_value3_end,
        tolerance_value1,
        tolerance_value2,
        tolerance_value3,
        influence_value1,
        influence_value2,
        influence_value3,
        influence_value12,
        influence_value21,
        influence_value23,
        influence_value32,
        influence_value13,
        influence_value31
    ):
        size1 = num_agents//3
        size2 = num_agents-2*size1
        size3 = size1
        group1 = -1
        group2 = -1
        group3 = -1
        if consensus:
            group1 = simple_clique_consensus(
                size1,
                function,
                belief_value1,
                tolerance_value1,
                influence_value1
            )
            group2 = simple_clique_consensus(
                size2,
                function,
                belief_value2,
                tolerance_value2,
                influence_value2
            )
            group3 = simple_clique_consensus(
                size3,
                function,
                belief_value3,
                tolerance_value3,
                influence_value3
            )
        else:
            group1 = simple_clique_uniform(
                size1,
                function,
                belief_value1,
                belief_value1_end,
                tolerance_value1,
                influence_value1
            )
            group2 = simple_clique_uniform(
                size2,
                function,
                belief_value2,
                belief_value2_end,
                tolerance_value2,
                influence_value2
            )
            group3 = simple_clique_uniform(
                size3,
                function,
                belief_value3,
                belief_value3_end,
                tolerance_value3,
                influence_value3
            )

        group1.append(group2.graph)
        group1.append(group3.graph)
        edges12 = all_edges(range(size1), range(size1,size1+size2))
        edges21 = all_edges(range(size1,size1+size2), range(size1))
        edges23 = all_edges(range(size1,size1+size2), range(size1+size2,size1+size2+size3))
        edges32 = all_edges(range(size1+size2,size1+size2+size3), range(size1,size1+size2))
        edges31 = all_edges(range(size1+size2,size1+size2+size3), range(size1))
        edges13 = all_edges(range(size1), range(size1+size2,size1+size2+size3))
        group1.graph.add_edges_from(edges12, inf = influence_value12)
        group1.graph.add_edges_from(edges21, inf = influence_value21)
        group1.graph.add_edges_from(edges23, inf = influence_value23) 
        group1.graph.add_edges_from(edges32, inf = influence_value32) 
        group1.graph.add_edges_from(edges31, inf = influence_value31) 
        group1.graph.add_edges_from(edges13, inf = influence_value13) 
        return group1

# Clique but everyone is influenced by two distinct agents
def clique_two_influencers_uniform(
        num_agents_middle, 
        update_function,
        start_value_middle,
        end_value_middle, 
        tolerance_value_middle,
        influence_value_middle,
        belief_value_1,
        beleif_value_2,
        tolerance_value_1,
        tolerance_value_2,
        weak_inf_1,
        weak_inf_2,
        influence_value_1,
        influence_value_2,
        constant_influencers
    ):
    influencers = Society_Graph(
        2,
        [belief_value_1, beleif_value_2], 
        np.full((2,2),0.0),
        [tolerance_value_1, tolerance_value_2], 
        default_fs.same(2,update_function)
    )

    middle = simple_clique_uniform(
        num_agents_middle,
        update_function,
        start_value_middle,
        end_value_middle,
        tolerance_value_middle,
        influence_value_middle
    )

    result = influencers
    result.append(middle)
    edges1 = all_edges([0],range(2,num_agents_middle+2))
    edges2 = all_edges([1],range(2,num_agents_middle+2))
    result.graph.add_edges_from(edges1,inf=influence_value_1)
    result.graph.add_edges_from(edges2,inf=influence_value_2)
    if not constant_influencers:
        result.graph.add_edge(2, 0, inf=weak_inf_1)
        result.graph.add_edge(num_agents_middle+1, 1, inf=weak_inf_2)
    return result

# Clique but everyone is influenced by one agent
def clique_one_influencer_uniform(
        num_agents_middle, 
        update_function,
        start_value_middle,
        end_value_middle, 
        tolerance_value_middle,
        influence_value_middle,
        belief_value_1,
        tolerance_value_1,
        weak_inf_1,
        influence_value_1,
        constant_influencer
    ):
    influencer = Society_Graph(
        1,
        [belief_value_1], 
        np.full((1,1),0.0),
        [tolerance_value_1], 
        default_fs.same(1,update_function)
    )

    middle = simple_clique_uniform(
        num_agents_middle,
        update_function,
        start_value_middle,
        end_value_middle,
        tolerance_value_middle,
        influence_value_middle
    )

    result = influencer
    result.append(middle)
    edges1 = all_edges([0],range(1,num_agents_middle+1))
    result.graph.add_edges_from(edges1,inf=influence_value_1)
    if not constant_influencer:
        result.graph.add_edge(1,0,inf=weak_inf_1)
    return result

# Two groups influence and are influenced by another one
def simple_tripartite(
        num_agents, 
        function,
        consensus_value1, 
        consensus_value2, 
        consensus_value3, 
        tolerance_value1,
        tolerance_value2,
        tolerance_value3,
        influence_value1,
        influence_value2,
        influence_value3,
        influence_value12,
        influence_value21,
        influence_value23,
        influence_value32
    ):
        size1 = num_agents//3
        size2 = num_agents-2*size1
        size3 = size1
        group1 = simple_clique_consensus(
            size1,
            function,
            consensus_value1,
            tolerance_value1,
            influence_value1
        )
        group2 = simple_clique_consensus(
            size2,
            function,
            consensus_value2,
            tolerance_value2,
            influence_value2
        )
        group3 = simple_clique_consensus(
            size3,
            function,
            consensus_value3,
            tolerance_value3,
            influence_value3
        )

        group1.append(group2.graph)
        group1.append(group3.graph)
        edges12 = all_edges(range(size1), range(size1,size1+size2))
        edges21 = all_edges(range(size1,size1+size2), range(size1))
        edges23 = all_edges(range(size1,size1+size2), range(size1+size2,size1+size2+size3))
        edges32 = all_edges(range(size1+size2,size1+size2+size3), range(size1,size1+size2))
        group1.graph.add_edges_from(edges12, inf = influence_value12)
        group1.graph.add_edges_from(edges21, inf = influence_value21)
        group1.graph.add_edges_from(edges23, inf = influence_value23) 
        group1.graph.add_edges_from(edges32, inf = influence_value32) 
        return group1

# One of the groups has a influencer talking to it
def tripartite_one_influencer(
        inf1_value,
        inf_mid_value,
        blf1_value,
        blf2_value,
        tol1_value,
        tol_mid_value,
        update_function,
        num_ags_middle,
        constant_influencer,
        weak_influence1,
    ):
    result = Society_Graph(
        1,
        [blf1_value], 
        np.full((1,1),0),
        [tol1_value], 
        default_fs.same(1,update_function)
    )
    
    middle = simple_tripartite(
        num_ags_middle,
        update_function,
        blf1_value,
        (blf1_value+blf2_value)/2,
        blf2_value,
        tol_mid_value,
        tol_mid_value,
        tol_mid_value,
        inf_mid_value,
        inf_mid_value,
        inf_mid_value,
        inf_mid_value,
        inf_mid_value,
        inf_mid_value,
        inf_mid_value
    )

    size1 = num_ags_middle//3
    group_1 = range(1,1+size1)
    edg_1 = all_edges([0],group_1)

    result.append(middle)
    result.graph.add_edges_from(edg_1, inf = inf1_value)

    if not constant_influencer:
        result.graph.add_edge(2,0, inf = weak_influence1)
    return result


# The two non-middle groups have influencers talking to them
def tripartite_two_influencers(
        inf1_value,
        inf2_value,
        inf_mid_value,
        blf1_value,
        blf2_value,
        tol1_value,
        tol_mid_value,
        tol2_value,
        update_function,
        num_ags_middle,
        constant_influencers,
        weak_influence1,
        weak_influence2
    ):
    result = Society_Graph(
        2,
        [blf1_value, blf2_value], 
        np.full((2,2),0),
        [tol1_value, tol2_value], 
        default_fs.same(2,update_function)
    )
    
    middle = simple_tripartite(
        num_ags_middle,
        update_function,
        blf1_value,
        (blf1_value+blf2_value)/2,
        blf2_value,
        tol_mid_value,
        tol_mid_value,
        tol_mid_value,
        inf_mid_value,
        inf_mid_value,
        inf_mid_value,
        inf_mid_value,
        inf_mid_value,
        inf_mid_value,
        inf_mid_value
    )

    size1 = num_ags_middle//3
    group_1 = range(2,2+size1)
    group_2 = range(2+num_ags_middle-size1,2+num_ags_middle)
    edg_1 = all_edges([0],group_1)
    edg_2 = all_edges([1],group_2)

    result.append(middle)
    result.graph.add_edges_from(edg_1, inf = inf1_value)
    result.graph.add_edges_from(edg_2, inf = inf2_value)

    if not constant_influencers:
        result.graph.add_edge(2,0, inf = weak_influence1)
        result.graph.add_edge(num_ags_middle+1,1,inf = weak_influence2)
    return result


# graph is a tuple: Gr and name of the graph
# Gr is a list of parameters: (resulting_graphs,parameter)
# resulting_graphs is a list of graphs
def simulate(graph):
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
                plt.savefig(file_name+f"{j}.png")
            plt.close()
