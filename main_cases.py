import networkx as nx
import numpy as np
import os
from matplotlib import pyplot as plt
from numpy.random.mtrand import f
from types import FunctionType

from example_cases import all_edges, simple_clique_uniform
from polarization_measure import pol_ER_discretized
from society_graph import Society_Graph, INFLUENCE_VALUE, TOLERANCE_VALUE
import cli_utils as cli
import default_beliefs,default_fs,default_influences,default_tolerances,belief_update_fs

# truth influences scientists. Some scientists are science comunicators, who influence all of the others. The others may influence the scientists and themselves.
def scientists_buffer(
        # ammount of each class (1 truth always)
        num_scientists : int,
        num_comunicators : int, # extra scientists
        num_others : int,
        # influence values
        inf_truth_scientists : np.float64,
        inf_scientists_scientists : np.float64,
        inf_scientists_others : np.float64,
        inf_others_scientists : np.float64,
        inf_others_others : np.float64,
        # update functions
        upf_truth_scientists : FunctionType,
        upf_scientists_scientists : FunctionType,
        upf_scientists_others : FunctionType,
        upf_others_scientists : FunctionType,
        upf_others_others : FunctionType,
        # tolerance values
        tol_truth_scientists : np.float64,
        tol_scientists_scientists : np.float64,
        tol_scientists_others : np.float64,
        tol_others_scientists : np.float64,
        tol_others_others : np.float64,
        # belief values
        bel_scientists_distr : np.float64,
        bel_others_distr : np.float64,
        bel_truth : np.float64 = 1.0,
        # comunicators get directly influenced by truth?
        comunicators_see_truth : bool = False,
        # post-simulation settings
        see_constant_agents: bool = True,
        constant_agents_tol: bool = False,
        pol_measure : FunctionType = pol_ER_discretized,
        random_others : bool = False
    ) -> Society_Graph:
    # Simplifying later simulations
    num_scientists = int(num_scientists)
    num_comunicators = int(num_comunicators)
    num_others = int(num_others)
    truth_node = Society_Graph(
        1,
        [bel_truth], 
        np.full((1,1),0),
        default_fs.same(1,upf_truth_scientists),
        [[1]], 
        node_colors_vector  = ["#D81B60"],
        edge_colors_matrix  = [["#D81B60"]],
        node_groups_vector  = [0],
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure  = pol_measure
    )
    size1 = 1
    
    scientists = Society_Graph(
        num_scientists,
        bel_scientists_distr[0](default_beliefs.Belief_Type.UNIFORM, num_scientists,*(bel_scientists_distr[1])),
        default_influences.build_inf_graph_clique(num_scientists, inf_scientists_scientists),
        default_fs.same(num_scientists, upf_scientists_scientists),
        default_tolerances.build_tol_matrix_constant(num_scientists, tol_scientists_scientists),
        node_colors_vector  = np.full(num_scientists, "#D81B60"),
        edge_colors_matrix  = np.full((num_scientists, num_scientists), "#D81B60"),
        node_groups_vector  = np.full(num_scientists, 1),
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure  = pol_measure
    )
    size2 = num_scientists

    comunicators = Society_Graph(
        num_comunicators,
        bel_scientists_distr[0](default_beliefs.Belief_Type.UNIFORM, num_comunicators,*(bel_scientists_distr[1])),
        default_influences.build_inf_graph_clique(num_comunicators, inf_scientists_scientists),
        default_fs.same(num_comunicators, upf_scientists_scientists),
        default_tolerances.build_tol_matrix_constant(num_comunicators, tol_scientists_scientists),
        node_colors_vector  = np.full(num_comunicators, "#1E88E5"),
        edge_colors_matrix  = np.full((num_comunicators, num_comunicators), "#1E88E5"),
        node_groups_vector  = np.full(num_comunicators, 2),
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure  = pol_measure
    )
    size3 = num_comunicators

    others = Society_Graph(
        num_others, bel_others_distr[0](default_beliefs.Belief_Type.UNIFORM, num_others, *(bel_others_distr[1])),
        default_influences.build_inf_graph_clique(num_others, inf_others_others),
        default_fs.same(num_others,upf_others_others),
        default_tolerances.build_tol_matrix_constant(num_others, tol_others_others),
        node_colors_vector  = np.full(num_others, "#FFC107"),
        edge_colors_matrix  = np.full((num_others, num_others), "#FFC107"),
        node_groups_vector  = np.full(num_others, 3),
        see_constant_agents = see_constant_agents,
        constant_agents_tol = constant_agents_tol,
        pol_measure  = pol_measure
    )
    if random_others:
        for e in others.graph.edges:
            others.graph[e[0]][e[1]][TOLERANCE_VALUE] = np.random.random()*2-1
            others.graph[e[0]][e[1]][INFLUENCE_VALUE] = np.random.random()

    size4 = num_others

    truth_to_scientists = all_edges(range(size1), range(size1, size1 + size2))
    truth_to_comunicators = all_edges(range(size1), range(size1 + size2, size1 + size2 + size3))

    scientists_to_comunicators = all_edges(range(size1, size1 + size2), range(size1 + size2, size1 + size2 + size3))
    comunicators_to_scientists = all_edges(range(size1 + size2, size1 + size2 + size3), range(size1, size1 + size2))

    comunicators_to_others = all_edges(range(size1 + size2, size1 + size2 + size3), range(size1 + size2 + size3, size1 + size2 + size3 + size4))
    # comunicators are also considered scientists here
    others_to_scientists = all_edges(range(size1 + size2 + size3, size1 + size2 + size3 + size4), range(size1, size1 + size2 + size3))

    result = truth_node
    result.append(scientists)
    result.append(comunicators)
    result.append(others)
    if inf_truth_scientists != 0:
        result.graph.add_edges_from(truth_to_scientists, inf = inf_truth_scientists, tol = tol_truth_scientists, upf = upf_truth_scientists, color = "#D81B60")
        if comunicators_see_truth:
            result.graph.add_edges_from(truth_to_comunicators, inf = inf_truth_scientists, tol = tol_truth_scientists, upf = upf_truth_scientists, color = "#D81B60")
    if inf_scientists_scientists != 0:
        result.graph.add_edges_from(scientists_to_comunicators, inf = inf_scientists_scientists, tol = tol_scientists_scientists, upf = upf_scientists_scientists, color = "#004D40")
        result.graph.add_edges_from(comunicators_to_scientists, inf = inf_scientists_scientists, tol = tol_scientists_scientists, upf = upf_scientists_scientists, color = "#004D40")
    # print(result.graph.number_of_nodes(), 'a')
    if inf_scientists_others != 0:
        result.graph.add_edges_from(comunicators_to_others, inf = inf_scientists_others, tol = tol_scientists_others, upf = upf_scientists_others, color = "#004D40")
    if inf_others_scientists != 0:
        result.graph.add_edges_from(others_to_scientists, inf = inf_others_scientists, tol = tol_others_scientists, upf = upf_others_scientists, color = "#004D40")

    if random_others:
        for e in comunicators_to_others:
            result.graph[e[0]][e[1]][TOLERANCE_VALUE] = np.random.random()*2-1
            result.graph[e[0]][e[1]][INFLUENCE_VALUE] = np.random.random()
    return result


def many_sides(
        # number of sides, agents initially defending sides and neutral agents
        num_sides : int,
        num_agents_sides : int,
        num_neutral_agents : int,
        # influences from the sides to agents, and from agent to agent
        influence_sides_agent : np.float64,
        influence_agent_agent : np.float64,
        # update functions
        update_sides_agent : np.float64,
        update_agent_agent : np.float64,
        # tolerances
        tolerance_sides_agent : np.float64,
        tolerance_agent_agent : np.float64,
        # value of agent defend side is side_value +- side_diff
        side_diff : np.float64,
        # interval of belief values of neutral agents
        neutral_low : np.float64 = 0,
        neutral_high : np.float64 = 1,
        # post-simulation settings
        see_constant_agents: bool = True,
        constant_agents_tol: bool = False,
        pol_measure : FunctionType = pol_ER_discretized
    ) -> Society_Graph:

    # Simplifying later simulations
    num_sides = int(num_sides)
    num_agents_sides = np.array(num_agents_sides, dtype=np.int64)
    num_neutral_agents = int(num_neutral_agents)

    sides = simple_clique_uniform(
        num_sides, # num_agents : int, 
        update_agent_agent, # function : FunctionType,
        0, # start_value : np.float64,
        1, # end_value : np.float64,
        tolerance_agent_agent, # tolerance_value : np.float64,
        0, # influence_value : np.float64,
        "#D81B60",
        "#D81B60",
        0, # group_num : int = 0,
        see_constant_agents = see_constant_agents, # see_constant_agents : bool = True,
        constant_agents_tol = constant_agents_tol # constant_agents_tol : bool = False
    )
    size1 = num_sides

    size2 = 0
    assert(len(num_agents_sides) == num_sides)
    side_agents = []
    pref = [0 for i in range(num_sides)]
    k = 0
    for cnt, i in enumerate(num_agents_sides):
        size2 += i
        if cnt != 0:
            pref[cnt] = pref[cnt-1] + i
        else:
            pref[cnt] = i
        val = k/(num_sides - 1)
        k += 1
        side_agents += [
            simple_clique_uniform(
                i, # num_agents : int, 
                update_agent_agent, # function : FunctionType,
                max(val - side_diff, 0), # start_value : np.float64,
                min(val + side_diff, 1), # end_value : np.float64,
                tolerance_agent_agent, # tolerance_value : np.float64,
                influence_agent_agent, # influence_value : np.float64,
                "#1E88E5",
                "#1E88E5",
                cnt + 1, # group_num : int = 0,
                see_constant_agents = see_constant_agents, # see_constant_agents : bool = True,
                constant_agents_tol = constant_agents_tol # constant_agents_tol : bool = False
            )
        ]
    size2 = size2

    neutral_agents = simple_clique_uniform(
        num_neutral_agents, # num_agents : int, 
        update_agent_agent, # function : FunctionType,
        neutral_low, # start_value : np.float64,
        neutral_high, # end_value : np.float64,
        tolerance_agent_agent, # tolerance_value : np.float64,
        influence_agent_agent, # influence_value : np.float64,
        "#FFC107",
        "#FFC107",
        len(num_agents_sides) + 1, # group_num : int = 0,
        see_constant_agents = see_constant_agents, # see_constant_agents : bool = True,
        constant_agents_tol = constant_agents_tol # constant_agents_tol : bool = False
    )
    size3 = num_neutral_agents

    side_to_sideagents = []
    for i in range(num_sides):
        if i != 0:
            side_to_sideagents += all_edges([i], range(size1+pref[i-1], size1+pref[i]))
        else:
            side_to_sideagents += all_edges([i], range(size1, size1+pref[i]))

    sideagents_to_agents = all_edges(range(size1, size1+size2), range(size1+size2,size1+size2+size3))
    agents_to_sideagents = all_edges(range(size1+size2, size1+size2+size3), range(size1,size1+size2))

    result = sides
    for i in side_agents:
        result.append(i)
    result.append(neutral_agents)

    # print(np.array(result.belief_history))
    if influence_sides_agent != 0:
        result.graph.add_edges_from(side_to_sideagents, inf = influence_sides_agent, tol = tolerance_sides_agent, upf = update_sides_agent, color = '#004D40')
    if influence_agent_agent != 0:
        result.graph.add_edges_from(sideagents_to_agents, inf = influence_agent_agent, tol = tolerance_agent_agent, upf = update_agent_agent, color = '#004D40')
        result.graph.add_edges_from(agents_to_sideagents, inf = influence_agent_agent, tol = tolerance_agent_agent, upf = update_agent_agent, color = '#004D40')

    return result
