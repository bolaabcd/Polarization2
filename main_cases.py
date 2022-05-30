import networkx as nx
import numpy as np
import os
from matplotlib import pyplot as plt
from numpy.random.mtrand import f
from types import FunctionType

import cli_utils as cli
import default_beliefs,default_fs,default_influences,default_tolerances,belief_update_fs
from society_graph import Society_Graph
from example_cases import all_edges

# truth influences scientists. Some scientists are sciencecomunicators, who influence all of the others. The others may influence the scientists and themselves.
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
        # are comunicators also scientists? (do they get influence from the truth?)
        comunicators_are_scientists = False,
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
        if comunicators_are_scientists:
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
