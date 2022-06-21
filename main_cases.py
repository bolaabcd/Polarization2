import networkx as nx
import numpy as np
import os
from matplotlib import pyplot as plt
from numpy.random.mtrand import f
from types import FunctionType

from society_graph import Society_Graph
from example_cases import all_edges, simple_clique_uniform
import cli_utils as cli
import default_beliefs,default_fs,default_influences,default_tolerances,belief_update_fs

# truth influences scientists. Some scientists are science comunicators, who influence all of the others. The others may influence the scientists and themselves.
def scientists_buffer(
		# ammount of each class (1 truth always)
        num_scientists,
        num_comunicators, # extra scientists
        num_others,
        # influence values
        inf_truth,
        inf_scientists_scientists,
        inf_scientists_others,
        inf_others_scientists,
        inf_others_others,
        # update functions
        updt_truth,
        updt_scientists,
        updt_others,
        # tolerance values
        out_tol_truth,
        in_tol_scientists,
        out_tol_scientists,
        in_tol_others,
        out_tol_others,
        # belief values
        bel_scientists_distr,
        bel_others_distr,
        bel_truth = 1.0,
        # is this Backfire-Effect? (or is it Boomerang-Effect)
        backfire_effect = True,
        # do comunicators get influence from the truth?
        comunicators_see_truth = False,
    ):
    truth_node = Society_Graph(
        1,
        [bel_truth], 
        np.full((1,1),0),
        [(1,out_tol_truth)], 
        default_fs.same(1,updt_truth),
        backfire_effect,
        "tab:red"
    )
    size1 = 1
    
    scientists = Society_Graph(
        num_scientists,
        bel_scientists_distr[0](default_beliefs.Default_Belief.UNIFORM, num_scientists,*(bel_scientists_distr[1])),
        default_influences.build_inf_graph_clique(num_scientists, inf_scientists_scientists),
        default_tolerances.build_tol_list_constant(num_scientists, in_tol_scientists, out_tol_scientists),
        default_fs.same(num_scientists,updt_scientists),
        backfire_effect,
        "tab:orange"
    )
    size2 = num_scientists

    comunicators = Society_Graph(
        num_comunicators,
        bel_scientists_distr[0](default_beliefs.Default_Belief.UNIFORM, num_comunicators,*(bel_scientists_distr[1])),
        default_influences.build_inf_graph_clique(num_comunicators, inf_scientists_scientists),
        default_tolerances.build_tol_list_constant(num_comunicators, in_tol_scientists, out_tol_scientists),
        default_fs.same(num_comunicators,updt_scientists),
        backfire_effect,
        "tab:green"
    )
    size3 = num_comunicators

    others = Society_Graph(
        num_others,
        bel_others_distr[0](default_beliefs.Default_Belief.UNIFORM, num_others, *(bel_others_distr[1])),
        default_influences.build_inf_graph_clique(num_others, inf_others_others),
        default_tolerances.build_tol_list_constant(num_others, in_tol_others, out_tol_others),
        default_fs.same(num_others,updt_others),
        backfire_effect
    )
    size4 = num_others

    truth_to_scientists = all_edges(range(size1), range(size1, size1+size2))
    truth_to_comunicators = all_edges(range(size1), range(size1+size2,size1+size2+size3))

    scientists_to_comunicators = all_edges(range(size1, size1+size2), range(size1+size2, size1+size2+size3))
    comunicators_to_scientists = all_edges(range(size1+size2, size1+size2+size3), range(size1, size1+size2))

    comunicators_to_others = all_edges(range(size1+size2, size1+size2+size3), range(size1+size2+size3, size1+size2+size3+size4))
    # comunicators are also considered scientists here
    others_to_scientists = all_edges(range(size1+size2+size3, size1+size2+size3+size4), range(size1, size1+size2+size3))

    # nx.set_node_attributes(truth_node.graph,1,"subset")
    # nx.set_node_attributes(scientists.graph,2,"subset")
    # nx.set_node_attributes(comunicators.graph,3,"subset")
    # nx.set_node_attributes(others.graph,4,"subset")
    result = truth_node
    result.append(scientists)
    result.append(comunicators)
    result.append(others)
    if inf_truth != 0:
        result.graph.add_edges_from(truth_to_scientists, inf = inf_truth, edge_color = 'tab:red')
        if comunicators_see_truth:
            result.graph.add_edges_from(truth_to_comunicators, inf = inf_truth, edge_color = 'tab:red')
    if inf_scientists_scientists != 0:
        result.graph.add_edges_from(scientists_to_comunicators, inf = inf_scientists_scientists, edge_color = 'tab:orange')
        result.graph.add_edges_from(comunicators_to_scientists, inf = inf_scientists_scientists, edge_color = 'tab:green')
    # print(result.graph.number_of_nodes(), 'a')
    if inf_scientists_others != 0:
        result.graph.add_edges_from(comunicators_to_others, inf = inf_scientists_others, edge_color = 'tab:green')
    if inf_others_scientists != 0:
        result.graph.add_edges_from(others_to_scientists, inf = inf_others_scientists, edge_color = 'tab:blue')

    return result


def many_sides(
        # number of sides, agents initially defending sides and neutral agents
        num_sides,
        num_agents_sides,
        num_neutral_agents,
        # influences from the sides to agents, and from agent to agent
        influences_sides_agent,
        influence_agent_agent,
        # update function
        agent_update,
        # tolerances
        in_tolerance_agent,
        out_tolerance_agent,
        out_tolerance_sides,
        # value of agent defend side is side_value +- side_diff
        side_diff,
        # interval of belief values of neutral agents
        neutral_low = 0,
        neutral_high = 1,
        # will we use backfire-effect? (or boomerang effect?)
        is_backfire = True,
        ignore_constant = False
    ):
    sides = simple_clique_uniform(
        num_sides, # num_agents 
        agent_update, # function
        0, # start_value
        1, # end_value
        (1,out_tolerance_sides), # tolerance_value
        0, # influence_value
        is_backfire,
        "tab:red",#node_color
        ignore_constant = ignore_constant
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
                i,# num_agents, 
                agent_update,# function,
                max(val - side_diff, 0),# start_value,
                min(val + side_diff, 1),# end_value, 
                (in_tolerance_agent, out_tolerance_agent),# tolerance_value,
                influence_agent_agent,# influence_value,
                is_backfire,
                "tab:orange",
                ignore_constant = ignore_constant
            )
        ]
    size2 = size2

    neutral_agents = simple_clique_uniform(
        num_neutral_agents,# num_agents, 
        agent_update,# function,
        neutral_low,# start_value,
        neutral_high,# end_value, 
        (in_tolerance_agent, out_tolerance_agent),# tolerance_value,
        influence_agent_agent,# influence_value,
        is_backfire,
        "tab:green",#node_color
        ignore_constant = ignore_constant
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
    agents_to_agents = all_edges(range(size1+size2, size1+size2+size3), range(size1+size2, size1+size2+size3))

    result = sides
    for i in side_agents:
        result.append(i)
    result.append(neutral_agents)

    if influences_sides_agent != 0:
        result.graph.add_edges_from(side_to_sideagents, inf = influences_sides_agent, edge_color = 'tab:red')
    if influence_agent_agent != 0:
        result.graph.add_edges_from(sideagents_to_agents, inf = influence_agent_agent, edge_color = 'tab:orange')
        result.graph.add_edges_from(agents_to_sideagents, inf = influence_agent_agent, edge_color = 'tab:green')
        result.graph.add_edges_from(agents_to_agents, inf = influence_agent_agent, edge_color = 'tab:gray')

    return result