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
)

simulate(all_sims)

# many_sides_param_list = []
# print(1)
# numsides = []
# for i in range(100):
#     gr = many_sides(
# 	    ## number of sides, agents initially defending sides and neutral agents
#         int(100*i/99+2),#num_sides,
#         [2 for i in range(int(100*i/99+2))],#num_agents_sides,
#         10,#num_neutral_agents,
#         ## influences from the sides to agents, and from agent to agent
#         1,#influences_sides_agent,
#         0.5,#influence_agent_agent,
#         ## update function
#         FUNCTION,#agent_update,
#         ## tolerances
#         1,#in_tolerance_agent,
#         1,#out_tolerance_agent,
#         1,#out_tolerance_sides,
#         ## value of agent defend side is side_value +- side_diff
#         0.1,#side_diff,
#         ## interval of belief values of neutral agents
#         0.3,#neutral_low = 0,
#         0.7,#neutral_high = 1,
#         ## will we use backfire-effect? (or boomerang effect?)
#         True,#is_backfire = True
#         True# ignore_constant = False
#     )
#     numsides.append(gr)
# many_sides_param_list.append((numsides,"numsides"+NAME))
# sideinf = []
# for i in range(100):
#     gr = many_sides(
#         ## number of sides, agents initially defending sides and neutral agents
#         5,#num_sides,
#         [2 for i in range(5)],#num_agents_sides,
#         10,#num_neutral_agents,
#         ## influences from the sides to agents, and from agent to agent
#         i/99,#influences_sides_agent,
#         0.5,#influence_agent_agent,
#         ## update function
#         FUNCTION,#agent_update,
#         ## tolerances
#         1,#in_tolerance_agent,
#         1,#out_tolerance_agent,
#         1,#out_tolerance_sides,
#         ## value of agent defend side is side_value +- side_diff
#         0.1,#side_diff,
#         ## interval of belief values of neutral agents
#         0.3,#neutral_low = 0,
#         0.7,#neutral_high = 1,
#         ## will we use backfire-effect? (or boomerang effect?)
#         True,#is_backfire = True
#         False# ignore_constant = False
#     )
#     sideinf.append(gr)
# many_sides_param_list.append((sideinf,"sideinf"+NAME))
# sideagentssize = []
# for i in range(100):
#     gr = many_sides(
#         ## number of sides, agents initially defending sides and neutral agents
#         5,#num_sides,
#         [int(100*i/99+2) for j in range(5)],#num_agents_sides,
#         10,#num_neutral_agents,
#         ## influences from the sides to agents, and from agent to agent
#         1,#influences_sides_agent,
#         0.5,#influence_agent_agent,
#         ## update function
#         FUNCTION,#agent_update,
#         ## tolerances
#         1,#in_tolerance_agent,
#         1,#out_tolerance_agent,
#         1,#out_tolerance_sides,
#         ## value of agent defend side is side_value +- side_diff
#         0.1,#side_diff,
#         ## interval of belief values of neutral agents
#         0.3,#neutral_low = 0,
#         0.7,#neutral_high = 1,
#         ## will we use backfire-effect? (or boomerang effect?)
#         True,#is_backfire = True
#         False# ignore_constant = False
#     )
#     sideagentssize.append(gr)
# many_sides_param_list.append((sideagentssize,"sideagentssize"+NAME))

# backfire_agent = []
# for i in range(100):
#     gr = many_sides(
# 	    ## number of sides, agents initially defending sides and neutral agents
#         5,#num_sides,
#         [2 for i in range(5)],#num_agents_sides,
#         10,#num_neutral_agents,
#         ## influences from the sides to agents, and from agent to agent
#         1,#influences_sides_agent,
#         0.5,#influence_agent_agent,
#         ## update function
#         FUNCTION,#agent_update,
#         ## tolerances
#         2*i/99-1,#in_tolerance_agent,
#         1,#out_tolerance_agent,
#         1,#out_tolerance_sides,
#         ## value of agent defend side is side_value +- side_diff
#         0.1,#side_diff,
#         ## interval of belief values of neutral agents
#         0.3,#neutral_low = 0,
#         0.7,#neutral_high = 1,
#         ## will we use backfire-effect? (or boomerang effect?)
#         True,#is_backfire = True
#         False# ignore_constant = False
#     )
#     backfire_agent.append(gr)
# many_sides_param_list.append((backfire_agent,"backfire_agent"+NAME))
# boomerang_agents = []
# for i in range(100):
#     gr = many_sides(
#         ## number of sides, agents initially defending sides and neutral agents
#         5,#num_sides,
#         [2 for i in range(5)],#num_agents_sides,
#         10,#num_neutral_agents,
#         ## influences from the sides to agents, and from agent to agent
#         1,#influences_sides_agent,
#         0.5,#influence_agent_agent,
#         ## update function
#         FUNCTION,#agent_update,
#         ## tolerances
#         1,#in_tolerance_agent,
#         2*i/99-1,#out_tolerance_agent,
#         1,#out_tolerance_sides,
#         ## value of agent defend side is side_value +- side_diff
#         0.1,#side_diff,
#         ## interval of belief values of neutral agents
#         0.3,#neutral_low = 0,
#         0.7,#neutral_high = 1,
#         ## will we use backfire-effect? (or boomerang effect?)
#         False,#is_backfire = True
#         False# ignore_constant = False
#     )
#     boomerang_agents.append(gr)
# many_sides_param_list.append((boomerang_agents,"boomerang_agents"+NAME))
# boomerang_sides = []
# for i in range(100):
#     gr = many_sides(
#         ## number of sides, agents initially defending sides and neutral agents
#         5,#num_sides,
#         [2 for i in range(5)],#num_agents_sides,
#         10,#num_neutral_agents,
#         ## influences from the sides to agents, and from agent to agent
#         1,#influences_sides_agent,
#         0.5,#influence_agent_agent,
#         ## update function
#         FUNCTION,#agent_update,
#         ## tolerances
#         1,#in_tolerance_agent,
#         1,#out_tolerance_agent,
#         2*i/99-1,#out_tolerance_sides,
#         ## value of agent defend side is side_value +- side_diff
#         0.1,#side_diff,
#         ## interval of belief values of neutral agents
#         0.3,#neutral_low = 0,
#         0.7,#neutral_high = 1,
#         ## will we use backfire-effect? (or boomerang effect?)
#         False,#is_backfire = True
#         False# ignore_constant = False
#     )
#     boomerang_sides.append(gr)
# many_sides_param_list.append((boomerang_sides,"boomerang_sides"+NAME))
# unilateral_amt = []
# for i in range(100):
#     gr = many_sides(
#         ## number of sides, agents initially defending sides and neutral agents
#         5,#num_sides,
#         [int(100*i/99+2)]+[2 for i in range(4)],#num_agents_sides,
#         10,#num_neutral_agents,
#         ## influences from the sides to agents, and from agent to agent
#         1,#influences_sides_agent,
#         0.5,#influence_agent_agent,
#         ## update function
#         FUNCTION,#agent_update,
#         ## tolerances
#         1,#in_tolerance_agent,
#         1,#out_tolerance_agent,
#         1,#out_tolerance_sides,
#         ## value of agent defend side is side_value +- side_diff
#         0.1,#side_diff,
#         ## interval of belief values of neutral agents
#         0.3,#neutral_low = 0,
#         0.7,#neutral_high = 1,
#         ## will we use backfire-effect? (or boomerang effect?)
#         True,#is_backfire = True
#         False# ignore_constant = False
#     )
#     unilateral_amt.append(gr)
# many_sides_param_list.append((unilateral_amt,"unilateral_amt"+NAME))
# neutral_amt = []
# for i in range(100):
#     gr = many_sides(
#         ## number of sides, agents initially defending sides and neutral agents
#         5,#num_sides,
#         [2 for i in range(5)],#num_agents_sides,
#         int(100*i/99+2),#num_neutral_agents,
#         ## influences from the sides to agents, and from agent to agent
#         1,#influences_sides_agent,
#         0.5,#influence_agent_agent,
#         ## update function
#         FUNCTION,#agent_update,
#         ## tolerances
#         1,#in_tolerance_agent,
#         1,#out_tolerance_agent,
#         1,#out_tolerance_sides,
#         ## value of agent defend side is side_value +- side_diff
#         0.1,#side_diff,
#         ## interval of belief values of neutral agents
#         0.3,#neutral_low = 0,
#         0.7,#neutral_high = 1,
#         ## will we use backfire-effect? (or boomerang effect?)
#         True,#is_backfire = True
#         False# ignore_constant = False
#     )
#     neutral_amt.append(gr)
# many_sides_param_list.append((neutral_amt,"neutral_amt"+NAME))
# simulate((many_sides_param_list,"many_sides"+NAME))
# del many_sides_param_list