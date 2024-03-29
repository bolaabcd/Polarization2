from example_cases import *
from cli_utils import ProgressRange

import matplotlib.gridspec as gridspec

FUNCTION = belief_update_fs.quadratic_update

# society type -> parameter -> range
all_sims = (
	(
		simple_tripartite,
		"simple_tripartite",
		[
	        33,# num_agents : int, 
	        FUNCTION,# function : FunctionType,
	        0,# consensus_value1 : np.float64, 
	        0.5,# consensus_value2 : np.float64, 
	        1,# consensus_value3 : np.float64, 
	        1,# influence_value1 : np.float64,
	        1,# influence_value2 : np.float64,
	        1,# influence_value3 : np.float64,
	        1,# influence_value12 : np.float64,
	        1,# influence_value21 : np.float64,
	        1,# influence_value23 : np.float64,
	        1,# influence_value32 : np.float64,
	        1,# tolerance_value1 : np.float64,
	        1,# tolerance_value2 : np.float64,
	        1,# tolerance_value3 : np.float64,
	        1,# tolerance_value12 : np.float64,
	        1,# tolerance_value21 : np.float64,
	        1,# tolerance_value23 : np.float64,
	        1,# tolerance_value32 : np.float64,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
			None,# num_agents : int, 
			None,# function : FunctionType,
			None,# consensus_value1 : np.float64, 
			None,# consensus_value2 : np.float64, 
			None,# consensus_value3 : np.float64, 
			(0,1),# influence_value1 : np.float64,
			(0,1),# influence_value2 : np.float64,
			None,# influence_value3 : np.float64,
			(0,1),# influence_value12 : np.float64,
			None,# influence_value21 : np.float64,
			None,# influence_value23 : np.float64,
			None,# influence_value32 : np.float64,
			(-1,1),# tolerance_value1 : np.float64,
			(-1,1),# tolerance_value2 : np.float64,
			None,# tolerance_value3 : np.float64,
			(-1,1),# tolerance_value12 : np.float64,
			(-1,1),# tolerance_value21 : np.float64,
			None,# tolerance_value23 : np.float64,
			None,# tolerance_value32 : np.float64,
			# see_constant_agents: bool = True,
			# constant_agents_tol: bool = False,
			# pol_measure : FunctionType = pol_ER_discretized
		],
		[
			"num_agents", 
	        "update_function",
	        "consensus_value1", 
	        "consensus_value2", 
	        "consensus_value3", 
	        "influence_value1",
	        "influence_value2",
	        "influence_value3",
	        "influence_value12",
	        "influence_value21",
	        "influence_value23",
	        "influence_value32",
	        "tolerance_value1",
	        "tolerance_value2",
	        "tolerance_value3",
	        "tolerance_value12",
	        "tolerance_value21",
	        "tolerance_value23",
	        "tolerance_value32",
		],
	),

	(
		simple_clique_uniform,
		"simple_clique_uniform",
		[
	        33,# num_agents : int, 
	        FUNCTION,# function : FunctionType,
	        0,# start_value : np.float64,
	        1,# end_value : np.float64,
	        1,# tolerance_value : np.float64,
	        1,# influence_value : np.float64,
	        # node_color : str = "tab:blue",
	        # edge_color : str = "tab:gray",
	        # group_num : int = 0,
	        # see_constant_agents : bool = True,
	        # constant_agents_tol : bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
			None,# num_agents : int, 
	        None,# function : FunctionType,
	        None,# start_value : np.float64,
	        None,# end_value : np.float64,
	        (-1,1),# tolerance_value : np.float64,
	        ( 0,1),# influence_value : np.float64,
	        # node_color : str = "tab:blue",
	        # edge_color : str = "tab:gray",
	        # group_num : int = 0,
	        # see_constant_agents : bool = True,
	        # constant_agents_tol : bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
			"num_agents", 
	        "function",
	        "start_value",
	        "end_value",
	        "tolerance_value",
	        "influence_value",
		],
	),

	(
		clique_tripartite,
		"clique_tripartite",
		[
	        False,# is_consensus : bool,
	        33,# num_agents : int, 
	        FUNCTION,# function : FunctionType,
	        0,# belief_value1 : np.float64, 
	        0.2,# belief_value1_end : np.float64,
	        0.4,# belief_value2 : np.float64, 
	        0.6,# belief_value2_end : np.float64,
	        0.8,# belief_value3 : np.float64, 
	        1,# belief_value3_end : np.float64,
	        1,# influence_value1 : np.float64,
	        1,# influence_value2 : np.float64,
	        1,# influence_value3 : np.float64,
	        1,# influence_value12 : np.float64,
	        1,# influence_value21 : np.float64,
	        1,# influence_value23 : np.float64,
	        1,# influence_value32 : np.float64,
	        1,# influence_value13 : np.float64,
	        1,# influence_value31 : np.float64,
	        1,# tolerance_value1 : np.float64,
	        1,# tolerance_value2 : np.float64,
	        1,# tolerance_value3 : np.float64,
	        1,# tolerance_value12 : np.float64,
	        1,# tolerance_value21 : np.float64,
	        1,# tolerance_value23 : np.float64,
	        1,# tolerance_value32 : np.float64,
	        1,# tolerance_value13 : np.float64,
	        1,# tolerance_value31 : np.float64,
	        # see_constant_agents : bool = True,
	        # constant_agents_tol : bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        None,# is_consensus : bool,
	        None,# num_agents : int, 
	        None,# function : FunctionType,
	        None,# belief_value1 : np.float64, 
	        None,# belief_value1_end : np.float64,
	        None,# belief_value2 : np.float64, 
	        None,# belief_value2_end : np.float64,
	        None,# belief_value3 : np.float64, 
	        None,# belief_value3_end : np.float64,
	        (0,1),# influence_value1 : np.float64,
	        (0,1),# influence_value2 : np.float64,
	        None,# influence_value3 : np.float64,
	        (0,1),# influence_value12 : np.float64,
	        (0,1),# influence_value21 : np.float64,
	        None,# influence_value23 : np.float64,
	        None,# influence_value32 : np.float64,
	        None,# influence_value13 : np.float64,
	        None,# influence_value31 : np.float64,
	        (-1,1),# tolerance_value1 : np.float64,
	        (-1,1),# tolerance_value2 : np.float64,
	        None,# tolerance_value3 : np.float64,
	        (-1,1),# tolerance_value12 : np.float64,
	        (-1,1),# tolerance_value21 : np.float64,
	        None,# tolerance_value23 : np.float64,
	        None,# tolerance_value32 : np.float64,
	        None,# tolerance_value13 : np.float64,
	        None,# tolerance_value31 : np.float64,
	        # see_constant_agents : bool = True,
	        # constant_agents_tol : bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        "is_consensus",
	        "num_agents", 
	        "function",
	        "belief_value1", 
	        "belief_value1_end",
	        "belief_value2", 
	        "belief_value2_end",
	        "belief_value3", 
	        "belief_value3_end",
	        "influence_value1",
	        "influence_value2",
	        "influence_value3",
	        "influence_value12",
	        "influence_value21",
	        "influence_value23",
	        "influence_value32",
	        "influence_value13",
	        "influence_value31",
	        "tolerance_value1",
	        "tolerance_value2",
	        "tolerance_value3",
	        "tolerance_value12",
	        "tolerance_value21",
	        "tolerance_value23",
	        "tolerance_value32",
	        "tolerance_value13",
	        "tolerance_value31",
		],
	),

	(
		clique_two_influencers_uniform,
		"clique_two_constant_influencers_uniform",
		[
            31,# num_agents_middle : int, 
	        FUNCTION,# update_function : FunctionType,
	        0,# start_value_middle : np.float64,
	        1,# end_value_middle : np.float64, 
	        1,# tolerance_value_middle : np.float64,
	        1,# influence_value_middle : np.float64,
	        0,# belief_value_1 : np.float64,
	        1,# beleif_value_2 : np.float64,
	        1,# influence_value_1mid : np.float64,
	        1,# influence_value_2mid : np.float64,
	        1,# influence_value_mid1 : np.float64,
	        1,# influence_value_mid2 : np.float64,
	        1,# tolerance_value_1mid : np.float64,
	        1,# tolerance_value_2mid : np.float64,
	        1,# tolerance_value_mid1 : np.float64,
	        1,# tolerance_value_mid2 : np.float64,
	        True,# constant_influencers : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
            None,# num_agents_middle : int, 
	        None,# update_function : FunctionType,
	        None,# start_value_middle : np.float64,
	        None,# end_value_middle : np.float64, 
	        (-1,1),# tolerance_value_middle : np.float64,
	        (0,1),# influence_value_middle : np.float64,
	        None,# belief_value_1 : np.float64,
	        None,# beleif_value_2 : np.float64,
	        (0,1),# influence_value_1mid : np.float64,
	        None,# influence_value_2mid : np.float64,
	        None,# influence_value_mid1 : np.float64,
	        None,# influence_value_mid2 : np.float64,
	        (-1,1),# tolerance_value_1mid : np.float64,
	        None,# tolerance_value_2mid : np.float64,
	        None,# tolerance_value_mid1 : np.float64,
	        None,# tolerance_value_mid2 : np.float64,
	        None,# constant_influencers : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
            "num_agents_middle", 
	        "update_function",
	        "start_value_middle",
	        "end_value_middle", 
	        "tolerance_value_middle",
	        "influence_value_middle",
	        "belief_value_1",
	        "beleif_value_2",
	        "influence_value_1mid",
	        "influence_value_2mid",
	        "influence_value_mid1",
	        "influence_value_mid2",
	        "tolerance_value_1mid",
	        "tolerance_value_2mid",
	        "tolerance_value_mid1",
	        "tolerance_value_mid2",
	        "constant_influencers",
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
	),

	(
		clique_two_influencers_uniform,
		"clique_two_nonconstant_influencers_uniform",
		[
            31,# num_agents_middle : int, 
	        FUNCTION,# update_function : FunctionType,
	        0,# start_value_middle : np.float64,
	        1,# end_value_middle : np.float64, 
	        1,# tolerance_value_middle : np.float64,
	        1,# influence_value_middle : np.float64,
	        0,# belief_value_1 : np.float64,
	        1,# beleif_value_2 : np.float64,
	        1,# influence_value_1mid : np.float64,
	        1,# influence_value_2mid : np.float64,
	        0.1,# influence_value_mid1 : np.float64,
	        0.1,# influence_value_mid2 : np.float64,
	        1,# tolerance_value_1mid : np.float64,
	        1,# tolerance_value_2mid : np.float64,
	        1,# tolerance_value_mid1 : np.float64,
	        1,# tolerance_value_mid2 : np.float64,
	        False,# constant_influencers : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
            None,# num_agents_middle : int, 
	        None,# update_function : FunctionType,
	        None,# start_value_middle : np.float64,
	        None,# end_value_middle : np.float64, 
	        (-1,1),# tolerance_value_middle : np.float64,
	        (0,1),# influence_value_middle : np.float64,
	        None,# belief_value_1 : np.float64,
	        None,# beleif_value_2 : np.float64,
	        (0,1),# influence_value_1mid : np.float64,
	        None,# influence_value_2mid : np.float64,
	        (0,1),# influence_value_mid1 : np.float64,
	        None,# influence_value_mid2 : np.float64,
	        (-1,1),# tolerance_value_1mid : np.float64,
	        None,# tolerance_value_2mid : np.float64,
	        (-1,1),# tolerance_value_mid1 : np.float64,
	        None,# tolerance_value_mid2 : np.float64,
	        None,# constant_influencers : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
            "num_agents_middle", 
	        "update_function",
	        "start_value_middle",
	        "end_value_middle", 
	        "tolerance_value_middle",
	        "influence_value_middle",
	        "belief_value_1",
	        "beleif_value_2",
	        "influence_value_1mid",
	        "influence_value_2mid",
	        "influence_value_mid1",
	        "influence_value_mid2",
	        "tolerance_value_1mid",
	        "tolerance_value_2mid",
	        "tolerance_value_mid1",
	        "tolerance_value_mid2",
	        "constant_influencers",
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
	),

	(
		clique_one_influencer_uniform,
		"clique_one_constant_influencer_uniform",
		[
	        32,# num_agents_middle : int, 
	        FUNCTION,# update_function : FunctionType,
	        1,# belief_value_1 : np.float64,
	        0,# start_value_middle : np.float64,
	        1,# end_value_middle : np.float64, 
	        1,# influence_value_middle : np.float64,
	        1,# influence_value_1mid : np.float64,
	        1,# influence_value_mid1 : np.float64,
	        1,# tolerance_value_middle : np.float64,
	        1,# tolerance_value_1mid : np.float64,
	        1,# tolerance_value_mid1 : np.float64,
	        True,# constant_influencer : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        None,# num_agents_middle : int, 
	        None,# update_function : FunctionType,
	        None,# belief_value_1 : np.float64,
	        None,# start_value_middle : np.float64,
	        None,# end_value_middle : np.float64, 
	        (0,1),# influence_value_middle : np.float64,
	        (0,1),# influence_value_1mid : np.float64,
	        None,# influence_value_mid1 : np.float64,
	        (-1,1),# tolerance_value_middle : np.float64,
	        (-1,1),# tolerance_value_1mid : np.float64,
	        None,# tolerance_value_mid1 : np.float64,
	        None,# constant_influencer : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        "num_agents_middle",# num_agents_middle : int, 
	        "update_function",# update_function : FunctionType,
	        "belief_value_1",# belief_value_1 : np.float64,
	        "start_value_middle",# start_value_middle : np.float64,
	        "end_value_middle",# end_value_middle : np.float64, 
	        "influence_value_middle",# influence_value_middle : np.float64,
	        "influence_value_1mid",# influence_value_1mid : np.float64,
	        "influence_value_mid1",# influence_value_mid1 : np.float64,
	        "tolerance_value_middle",# tolerance_value_middle : np.float64,
	        "tolerance_value_1mid",# tolerance_value_1mid : np.float64,
	        "tolerance_value_mid1",# tolerance_value_mid1 : np.float64,
	        "constant_influencer",# constant_influencer : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
	),

	(
		clique_one_influencer_uniform,
		"clique_one_nonconstant_influencer_uniform",
		[
	        32,# num_agents_middle : int, 
	        FUNCTION,# update_function : FunctionType,
	        1,# belief_value_1 : np.float64,
	        0,# start_value_middle : np.float64,
	        1,# end_value_middle : np.float64, 
	        1,# influence_value_middle : np.float64,
	        1,# influence_value_1mid : np.float64,
	        0.1,# influence_value_mid1 : np.float64,
	        1,# tolerance_value_middle : np.float64,
	        1,# tolerance_value_1mid : np.float64,
	        1,# tolerance_value_mid1 : np.float64,
	        False,# constant_influencer : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        None,# num_agents_middle : int, 
	        None,# update_function : FunctionType,
	        None,# belief_value_1 : np.float64,
	        None,# start_value_middle : np.float64,
	        None,# end_value_middle : np.float64, 
	        (0,1),# influence_value_middle : np.float64,
	        (0,1),# influence_value_1mid : np.float64,
	        (0,1),# influence_value_mid1 : np.float64,
	        (-1,1),# tolerance_value_middle : np.float64,
	        (-1,1),# tolerance_value_1mid : np.float64,
	        (-1,1),# tolerance_value_mid1 : np.float64,
	        None,# constant_influencer : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        "num_agents_middle",# num_agents_middle : int, 
	        "update_function",# update_function : FunctionType,
	        "belief_value_1",# belief_value_1 : np.float64,
	        "start_value_middle",# start_value_middle : np.float64,
	        "end_value_middle",# end_value_middle : np.float64, 
	        "influence_value_middle",# influence_value_middle : np.float64,
	        "influence_value_1mid",# influence_value_1mid : np.float64,
	        "influence_value_mid1",# influence_value_mid1 : np.float64,
	        "tolerance_value_middle",# tolerance_value_middle : np.float64,
	        "tolerance_value_1mid",# tolerance_value_1mid : np.float64,
	        "tolerance_value_mid1",# tolerance_value_mid1 : np.float64,
	        "constant_influencer",# constant_influencer : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
	),

	(
		tripartite_one_influencer,
		"tripartite_one_constant_influencer",
		[
	        32,# num_ags_middle : int,
	        1,# belief_value1 : np.float64,
	        0,# belief_value2 : np.float64,
	        FUNCTION,# update_function : np.float64,
	        1,# influence_value_mid : np.float64,
	        1,# influence_value_1mid : np.float64,
	        1,# influence_value_mid1 : np.float64,
	        1,# tolerance_value_mid : np.float64,
	        1,# tolerance_value_1mid : np.float64,
	        1,# tolerance_value_mid1 : np.float64,
	        True,# constant_influencer : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        None,# num_ags_middle : int,
	        None,# belief_value1 : np.float64,
	        None,# belief_value2 : np.float64,
	        None,# update_function : np.float64,
	        (0,1),# influence_value_mid : np.float64,
	        (0,1),# influence_value_1mid : np.float64,
	        None,# influence_value_mid1 : np.float64,
	        (-1,1),# tolerance_value_mid : np.float64,
	        (-1,1),# tolerance_value_1mid : np.float64,
	        None,# tolerance_value_mid1 : np.float64,
	        None,# constant_influencer : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        "num_ags_middle",# : int,
	        "belief_value1",# : np.float64,
	        "belief_value2",# : np.float64,
	        "update_function",# : np.float64,
	        "influence_value_mid",# : np.float64,
	        "influence_value_1mid",# : np.float64,
	        "influence_value_mid1",# : np.float64,
	        "tolerance_value_mid",# : np.float64,
	        "tolerance_value_1mid",# : np.float64,
	        "tolerance_value_mid1",# : np.float64,
	        "constant_influencer",# : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
	),

	(
		tripartite_one_influencer,
		"tripartite_one_nonconstant_influencer",
		[
	        32,# num_ags_middle : int,
	        1,# belief_value1 : np.float64,
	        0,# belief_value2 : np.float64,
	        FUNCTION,# update_function : np.float64,
	        1,# influence_value_mid : np.float64,
	        1,# influence_value_1mid : np.float64,
	        0.1,# influence_value_mid1 : np.float64,
	        1,# tolerance_value_mid : np.float64,
	        1,# tolerance_value_1mid : np.float64,
	        1,# tolerance_value_mid1 : np.float64,
	        False,# constant_influencer : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        None,# num_ags_middle : int,
	        None,# belief_value1 : np.float64,
	        None,# belief_value2 : np.float64,
	        None,# update_function : np.float64,
	        (0,1),# influence_value_mid : np.float64,
	        (0,1),# influence_value_1mid : np.float64,
	        (0,1),# influence_value_mid1 : np.float64,
	        (-1,1),# tolerance_value_mid : np.float64,
	        (-1,1),# tolerance_value_1mid : np.float64,
	        (-1,1),# tolerance_value_mid1 : np.float64,
	        None,# constant_influencer : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        "num_ags_middle",# : int,
	        "belief_value1",# : np.float64,
	        "belief_value2",# : np.float64,
	        "update_function",# : np.float64,
	        "influence_value_mid",# : np.float64,
	        "influence_value_1mid",# : np.float64,
	        "influence_value_mid1",# : np.float64,
	        "tolerance_value_mid",# : np.float64,
	        "tolerance_value_1mid",# : np.float64,
	        "tolerance_value_mid1",# : np.float64,
	        "constant_influencer",# : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
	),

	(
		tripartite_two_influencers,
		"tripartite_two_constant_influencers",
		[
	        31,# num_ags_middle : int,
	        0,# belief_value1 : np.float64,
	        1,# belief_value2 : np.float64,
	        FUNCTION,# update_function : np.float64,
	        1,# influence_value_mid : np.float64,
	        1,# influence_value_1mid : np.float64,
	        1,# influence_value_2mid : np.float64,
	        1,# influence_value_mid1 : np.float64,
	        1,# influence_value_mid2 : np.float64,
	        1,# tolerance_value_1mid : np.float64,
	        1,# tolerance_value_2mid : np.float64,
	        1,# tolerance_value_mid1 : np.float64,
	        1,# tolerance_value_mid2 : np.float64,
	        1,# tolerance_value_mid : np.float64,
	        True,# constant_influencers : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        None,# num_ags_middle : int,
	        None,# belief_value1 : np.float64,
	        None,# belief_value2 : np.float64,
	        None,# update_function : np.float64,
	        (0,1),# influence_value_mid : np.float64,
	        (0,1),# influence_value_1mid : np.float64,
	        None,# influence_value_2mid : np.float64,
	        None,# influence_value_mid1 : np.float64,
	        None,# influence_value_mid2 : np.float64,
	        (-1,1),# tolerance_value_1mid : np.float64,
	        None,# tolerance_value_2mid : np.float64,
	        None,# tolerance_value_mid1 : np.float64,
	        None,# tolerance_value_mid2 : np.float64,
	        (-1,1),# tolerance_value_mid : np.float64,
	        None,# constant_influencers : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        "num_ags_middle",# : int,
	        "belief_value1",# : np.float64,
	        "belief_value2",# : np.float64,
	        "update_function",# : np.float64,
	        "influence_value_mid",# : np.float64,
	        "influence_value_1mid",# : np.float64,
	        "influence_value_2mid",# : np.float64,
	        "influence_value_mid1",# : np.float64,
	        "influence_value_mid2",# : np.float64,
	        "tolerance_value_1mid",# : np.float64,
	        "tolerance_value_2mid",# : np.float64,
	        "tolerance_value_mid1",# : np.float64,
	        "tolerance_value_mid2",# : np.float64,
	        "tolerance_value_mid",# : np.float64,
	        "constant_influencers",# : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
	),

	(
		tripartite_two_influencers,
		"tripartite_two_nonconstant_influencers",
		[
	        31,# num_ags_middle : int,
	        0,# belief_value1 : np.float64,
	        1,# belief_value2 : np.float64,
	        FUNCTION,# update_function : np.float64,
	        1,# influence_value_mid : np.float64,
	        1,# influence_value_1mid : np.float64,
	        1,# influence_value_2mid : np.float64,
	        0.1,# influence_value_mid1 : np.float64,
	        0.1,# influence_value_mid2 : np.float64,
	        1,# tolerance_value_1mid : np.float64,
	        1,# tolerance_value_2mid : np.float64,
	        1,# tolerance_value_mid1 : np.float64,
	        1,# tolerance_value_mid2 : np.float64,
	        1,# tolerance_value_mid : np.float64,
	        False,# constant_influencers : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        None,# num_ags_middle : int,
	        None,# belief_value1 : np.float64,
	        None,# belief_value2 : np.float64,
	        None,# update_function : np.float64,
	        (0,1),# influence_value_mid : np.float64,
	        (0,1),# influence_value_1mid : np.float64,
	        None,# influence_value_2mid : np.float64,
	        (0,1),# influence_value_mid1 : np.float64,
	        None,# influence_value_mid2 : np.float64,
	        (-1,1),# tolerance_value_1mid : np.float64,
	        None,# tolerance_value_2mid : np.float64,
	        (-1,1),# tolerance_value_mid1 : np.float64,
	        None,# tolerance_value_mid2 : np.float64,
	        (-1,1),# tolerance_value_mid : np.float64,
	        None,# constant_influencers : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
		[
	        "num_ags_middle",# : int,
	        "belief_value1",# : np.float64,
	        "belief_value2",# : np.float64,
	        "update_function",# : np.float64,
	        "influence_value_mid",# : np.float64,
	        "influence_value_1mid",# : np.float64,
	        "influence_value_2mid",# : np.float64,
	        "influence_value_mid1",# : np.float64,
	        "influence_value_mid2",# : np.float64,
	        "tolerance_value_1mid",# : np.float64,
	        "tolerance_value_2mid",# : np.float64,
	        "tolerance_value_mid1",# : np.float64,
	        "tolerance_value_mid2",# : np.float64,
	        "tolerance_value_mid",# : np.float64,
	        "constant_influencers",# : bool,
	        # see_constant_agents: bool = True,
	        # constant_agents_tol: bool = False,
	        # pol_measure : FunctionType = pol_ER_discretized
		],
	),
)

def simulate(many_sims, nframes = 100, nsteps = 100):
	if not os.path.exists("generated"):
		os.mkdir("generated")
	for maker, name, defaults, ranges, names in many_sims:
		maker(*defaults).draw_graph()
		if not os.path.exists(f"generated/{name}/"):
			os.mkdir(f"generated/{name}/")
		if not os.path.exists(f"generated/{name}/graph.svg"):
			plt.savefig(f"generated/{name}/graph.svg")
		plt.close()
		for i,rangee in enumerate(ranges):
			if rangee is not None:
				if not os.path.exists(f"generated/{name}/{names[i]}/"):
					os.mkdir(f"generated/{name}/{names[i]}/")
				if not os.path.exists(f"generated/{name}/{names[i]}/ags/"):
					os.mkdir(f"generated/{name}/{names[i]}/ags/")
				if not os.path.exists(f"generated/{name}/{names[i]}/pols/"):
					os.mkdir(f"generated/{name}/{names[i]}/pols/")
				if not os.path.exists(f"generated/{name}/{names[i]}/ags_pols/"):
					os.mkdir(f"generated/{name}/{names[i]}/ags_pols/")
				for j in ProgressRange(nframes):
					if not os.path.exists(f"generated/{name}/{names[i]}/ags/{j}.svg"):
						defcopy = defaults.copy()
						defcopy[i] = rangee[0] + (rangee[1]-rangee[0])*j/(nframes-1)
						# print("AAA\nAAAA")
						Gr = maker(*defcopy)
						# print("AAA\nAAAA")
						try:
							Gr.quick_update(nsteps)
						except:
							pass
						plt.close()
						Gr.plot_history()
						plt.savefig(f"generated/{name}/{names[i]}/ags/{j}.svg")
						plt.close()
					if not os.path.exists(f"generated/{name}/{names[i]}/pols/{j}.svg"):
						defcopy = defaults.copy()
						defcopy[i] = rangee[0] + (rangee[1]-rangee[0])*j/(nframes-1)
						Gr = maker(*defcopy)
						try:
							Gr.quick_update(nsteps)
						except:
							pass
						plt.close()
						Gr.plot_polarization()
						plt.savefig(f"generated/{name}/{names[i]}/pols/{j}.svg")
						plt.close()
					if not os.path.exists(f"generated/{name}/{names[i]}/ags_pols/{j}.svg"):
						defcopy = defaults.copy()
						defcopy[i] = rangee[0] + (rangee[1]-rangee[0])*j/(nframes-1)
						Gr = maker(*defcopy)
						try:
							Gr.quick_update(nsteps)
						except:
							pass
						plt.close()
						Gr.plot_hist_pol()
						plt.savefig(f"generated/{name}/{names[i]}/ags_pols/{j}.svg")
						plt.close()

if __name__ == "__main__":
	simulate(all_sims)
