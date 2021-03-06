from main_cases import *
from run_base_tests import simulate
from default_beliefs import build_belief

FUNCTION = belief_update_fs.quadratic_update

# society type -> parameter -> range
all_sims = (
    (
        scientists_buffer,
        "scientists_buffer_comun_dont_see_truth",
        [
            10,# num_scientists : int,
            3,# num_comunicators : int, # extra scientists
            20,# num_others : int,
            1,# inf_truth_scientists : np.float64,
            0.5,# inf_scientists_scientists : np.float64,
            0.2,# inf_scientists_others : np.float64,
            0.0,# inf_others_scientists : np.float64,
            0.3,# inf_others_others : np.float64,
            FUNCTION,# upf_truth_scientists : FunctionType,
            FUNCTION,# upf_scientists_scientists : FunctionType,
            FUNCTION,# upf_scientists_others : FunctionType,
            FUNCTION,# upf_others_scientists : FunctionType,
            FUNCTION,# upf_others_others : FunctionType,
            1,# tol_truth_scientists : np.float64,
            1,# tol_scientists_scientists : np.float64,
            1,# tol_scientists_others : np.float64,
            1,# tol_others_scientists : np.float64,
            1,# tol_others_others : np.float64,
            (build_belief, (3/5,1)),# bel_scientists_distr : np.float64,
            (build_belief, (0,1/4)),# bel_others_distr : np.float64,
            1,# bel_truth : np.float64 = 1.0,
            False,# comunicators_see_truth : bool = False,
            # see_constant_agents: bool = True,
            # constant_agents_tol: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
        [
            (1,15),# num_scientists : int,
            (1,15),# num_comunicators : int, # extra scientists
            (1,30),# num_others : int,
            (0,1),# inf_truth_scientists : np.float64,
            (0,1),# inf_scientists_scientists : np.float64,
            (0,1),# inf_scientists_others : np.float64,
            (0,1),# inf_others_scientists : np.float64,
            (0,1),# inf_others_others : np.float64,
            None,# upf_truth_scientists : FunctionType,
            None,# upf_scientists_scientists : FunctionType,
            None,# upf_scientists_others : FunctionType,
            None,# upf_others_scientists : FunctionType,
            None,# upf_others_others : FunctionType,
            (-1,1),# tol_truth_scientists : np.float64,
            (-1,1),# tol_scientists_scientists : np.float64,
            (-1,1),# tol_scientists_others : np.float64,
            (-1,1),# tol_others_scientists : np.float64,
            (-1,1),# tol_others_others : np.float64,
            None,# bel_scientists_distr : np.float64,
            None,# bel_others_distr : np.float64,
            None,# bel_truth : np.float64 = 1.0,
            None,# comunicators_see_truth : bool = False,
            # see_constant_agents: bool = True,
            # constant_agents_tol: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
        [
            "num_scientists",# : int,
            "num_comunicators",# : int, # extra scientists
            "num_others",# : int,
            "inf_truth_scientists",# : np.float64,
            "inf_scientists_scientists",# : np.float64,
            "inf_scientists_others",# : np.float64,
            "inf_others_scientists",# : np.float64,
            "inf_others_others",# : np.float64,
            "upf_truth_scientists",# : FunctionType,
            "upf_scientists_scientists",# : FunctionType,
            "upf_scientists_others",# : FunctionType,
            "upf_others_scientists",# : FunctionType,
            "upf_others_others",# : FunctionType,
            "tol_truth_scientists",# : np.float64,
            "tol_scientists_scientists",# : np.float64,
            "tol_scientists_others",# : np.float64,
            "tol_others_scientists",# : np.float64,
            "tol_others_others",# : np.float64,
            "bel_scientists_distr",# : np.float64,
            "bel_others_distr",# : np.float64,
            "bel_truth",# : np.float64 = 1.0,
            "comunicators_see_truth",# : bool = False,
            # see_constant_agents: bool = True,
            # constant_agents_tol: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
    ),

    (
        scientists_buffer,
        "scientists_buffer_comun_see_truth",
        [
            10,# num_scientists : int,
            3,# num_comunicators : int, # extra scientists
            20,# num_others : int,
            1,# inf_truth_scientists : np.float64,
            0.5,# inf_scientists_scientists : np.float64,
            0.2,# inf_scientists_others : np.float64,
            0.0,# inf_others_scientists : np.float64,
            0.3,# inf_others_others : np.float64,
            FUNCTION,# upf_truth_scientists : FunctionType,
            FUNCTION,# upf_scientists_scientists : FunctionType,
            FUNCTION,# upf_scientists_others : FunctionType,
            FUNCTION,# upf_others_scientists : FunctionType,
            FUNCTION,# upf_others_others : FunctionType,
            1,# tol_truth_scientists : np.float64,
            1,# tol_scientists_scientists : np.float64,
            1,# tol_scientists_others : np.float64,
            1,# tol_others_scientists : np.float64,
            1,# tol_others_others : np.float64,
            (build_belief, (3/5,1)),# bel_scientists_distr : np.float64,
            (build_belief, (0,1/4)),# bel_others_distr : np.float64,
            1,# bel_truth : np.float64 = 1.0,
            True,# comunicators_see_truth : bool = False,
            # see_constant_agents: bool = True,
            # constant_agents_tol: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
        [
            (1,15),# num_scientists : int,
            (1,15),# num_comunicators : int, # extra scientists
            (1,30),# num_others : int,
            (0,1),# inf_truth_scientists : np.float64,
            (0,1),# inf_scientists_scientists : np.float64,
            (0,1),# inf_scientists_others : np.float64,
            (0,1),# inf_others_scientists : np.float64,
            (0,1),# inf_others_others : np.float64,
            None,# upf_truth_scientists : FunctionType,
            None,# upf_scientists_scientists : FunctionType,
            None,# upf_scientists_others : FunctionType,
            None,# upf_others_scientists : FunctionType,
            None,# upf_others_others : FunctionType,
            (-1,1),# tol_truth_scientists : np.float64,
            (-1,1),# tol_scientists_scientists : np.float64,
            (-1,1),# tol_scientists_others : np.float64,
            (-1,1),# tol_others_scientists : np.float64,
            (-1,1),# tol_others_others : np.float64,
            None,# bel_scientists_distr : np.float64,
            None,# bel_others_distr : np.float64,
            None,# bel_truth : np.float64 = 1.0,
            None,# comunicators_see_truth : bool = False,
            # see_constant_agents: bool = True,
            # constant_agents_tol: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
        [
            "num_scientists",# : int,
            "num_comunicators",# : int, # extra scientists
            "num_others",# : int,
            "inf_truth_scientists",# : np.float64,
            "inf_scientists_scientists",# : np.float64,
            "inf_scientists_others",# : np.float64,
            "inf_others_scientists",# : np.float64,
            "inf_others_others",# : np.float64,
            "upf_truth_scientists",# : FunctionType,
            "upf_scientists_scientists",# : FunctionType,
            "upf_scientists_others",# : FunctionType,
            "upf_others_scientists",# : FunctionType,
            "upf_others_others",# : FunctionType,
            "tol_truth_scientists",# : np.float64,
            "tol_scientists_scientists",# : np.float64,
            "tol_scientists_others",# : np.float64,
            "tol_others_scientists",# : np.float64,
            "tol_others_others",# : np.float64,
            "bel_scientists_distr",# : np.float64,
            "bel_others_distr",# : np.float64,
            "bel_truth",# : np.float64 = 1.0,
            "comunicators_see_truth",# : bool = False,
            # see_constant_agents: bool = True,
            # constant_agents_tol: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
    ),


    (
        many_sides,
        "many_sides_no_pol_const_ags",
        [
            5,# num_sides : int,
            [2 for i in range(5)],# num_agents_sides : int,
            10,# num_neutral_agents : int,
            1,# influence_sides_agent : np.float64,
            0.5,# influence_agent_agent : np.float64,
            FUNCTION,# update_sides_agent : np.float64,
            FUNCTION,# update_agent_agent : np.float64,
            1,# tolerance_sides_agent : np.float64,
            1,# tolerance_agent_agent : np.float64,
            0.1,# side_diff : np.float64,
            0.3,# neutral_low : np.float64 = 0,
            0.7,# neutral_high : np.float64 = 1,
            False,# see_constant_agents: bool = True,
            False,# constant_agents_tol: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
        [
            None,# num_sides : int,
            None,# num_agents_sides : int,
            (2,100),# num_neutral_agents : int,
            (0,1),# influence_sides_agent : np.float64,
            (0,1),# influence_agent_agent : np.float64,
            None,# update_sides_agent : np.float64,
            None,# update_agent_agent : np.float64,
            (-1,1),# tolerance_sides_agent : np.float64,
            (-1,1),# tolerance_agent_agent : np.float64,
            None,# side_diff : np.float64,
            None,# neutral_low : np.float64 = 0,
            None,# neutral_high : np.float64 = 1,
            None,# see_constant_agents: bool = True,
            None,# constant_agents_tol: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
        [
            "num_sides",# : int,
            "num_agents_sides",# : int,
            "num_neutral_agents",# : int,
            "influence_sides_agent",# : np.float64,
            "influence_agent_agent",# : np.float64,
            "update_sides_agent",# : np.float64,
            "update_agent_agent",# : np.float64,
            "tolerance_sides_agent",# : np.float64,
            "tolerance_agent_agent",# : np.float64,
            "side_diff",# : np.float64,
            "neutral_low",# : np.float64 = 0,
            "neutral_high",# : np.float64 = 1,
            "see_constant_agents",#: bool = True,
            "constant_agents_tol",#: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
    ),

    (
        many_sides,
        "many_sides_const_ags",
        [
            5,# num_sides : int,
            [2 for i in range(5)],# num_agents_sides : int,
            10,# num_neutral_agents : int,
            1,# influence_sides_agent : np.float64,
            0.5,# influence_agent_agent : np.float64,
            FUNCTION,# update_sides_agent : np.float64,
            FUNCTION,# update_agent_agent : np.float64,
            1,# tolerance_sides_agent : np.float64,
            1,# tolerance_agent_agent : np.float64,
            0.1,# side_diff : np.float64,
            0.3,# neutral_low : np.float64 = 0,
            0.7,# neutral_high : np.float64 = 1,
            False,# see_constant_agents: bool = True,
            True,# constant_agents_tol: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
        [
            None,# num_sides : int,
            None,# num_agents_sides : int,
            (2,100),# num_neutral_agents : int,
            (0,1),# influence_sides_agent : np.float64,
            (0,1),# influence_agent_agent : np.float64,
            None,# update_sides_agent : np.float64,
            None,# update_agent_agent : np.float64,
            (-1,1),# tolerance_sides_agent : np.float64,
            (-1,1),# tolerance_agent_agent : np.float64,
            None,# side_diff : np.float64,
            None,# neutral_low : np.float64 = 0,
            None,# neutral_high : np.float64 = 1,
            None,# see_constant_agents: bool = True,
            None,# constant_agents_tol: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
        [
            "num_sides",# : int,
            "num_agents_sides",# : int,
            "num_neutral_agents",# : int,
            "influence_sides_agent",# : np.float64,
            "influence_agent_agent",# : np.float64,
            "update_sides_agent",# : np.float64,
            "update_agent_agent",# : np.float64,
            "tolerance_sides_agent",# : np.float64,
            "tolerance_agent_agent",# : np.float64,
            "side_diff",# : np.float64,
            "neutral_low",# : np.float64 = 0,
            "neutral_high",# : np.float64 = 1,
            "see_constant_agents",#: bool = True,
            "constant_agents_tol",#: bool = False,
            # pol_measure : FunctionType = pol_ER_discretized
        ],
    ),
)

simulate(all_sims, nsteps = 500)
