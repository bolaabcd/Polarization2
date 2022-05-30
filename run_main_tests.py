from main_cases import *
from example_cases import simulate
from default_beliefs import build_belief

FUNCTION = belief_update_fs.quadratic_update
NAME = "Quadratic"

scientists_buffer_param_list = []
print(0)
backfire_others = []
for i in range(100):
    gr = scientists_buffer(
	    10,# num_scientists,
	    3,# num_comunicators, # extra scientists
	    20,# num_others,
	    1,# inf_truth,
	    0.5,# inf_scientists_scientists,
	    0.2,# inf_scientists_others,
	    0.0,# inf_others_scientists,
	    0.3,# inf_others_others,
	    FUNCTION,# updt_truth,
	    FUNCTION,# updt_scientists,
	    FUNCTION,# updt_others
	    # # tolerance values
	    1,# out_tol_truth,
	    1,# in_tol_scientists,
	    1,# out_tol_scientists,
	    2*i/99-1,# in_tol_others,
	    1,# out_tol_others,
	    (build_belief, (3/5,1)),# bel_scientists_distr,
	    (build_belief, (0,1/4)),# bel_others_distr,
	    1,# bel_truth = 1.0,
	    True,# backfire_effect = True,
	    False#comunicators_see_truth
    )
    backfire_others.append(gr)
scientists_buffer_param_list.append((backfire_others,"backfire_others"+NAME))
backfire_scientists = []
for i in range(100):
    gr = scientists_buffer(
        10,# num_scientists,
	    3,# num_comunicators, # extra scientists
	    20,# num_others,
	    1,# inf_truth,
	    0.5,# inf_scientists_scientists,
	    0.2,# inf_scientists_others,
	    0.0,# inf_others_scientists,
	    0.3,# inf_others_others,
	    FUNCTION,# updt_truth,
	    FUNCTION,# updt_scientists,
	    FUNCTION,# updt_others
	    # # tolerance values
	    1,# out_tol_truth,
	    2*i/99-1,# in_tol_scientists,
	    1,# out_tol_scientists,
	    1,# in_tol_others,
	    1,# out_tol_others,
	    (build_belief, (3/5,1)),# bel_scientists_distr,
	    (build_belief, (0,1/4)),# bel_others_distr,
	    1,# bel_truth = 1.0,
	    True,# backfire_effect = True,
	    False#comunicators_see_truth
    )
    backfire_scientists.append(gr)
scientists_buffer_param_list.append((backfire_scientists,"backfire_scientists"+NAME))
backfire_all = []
for i in range(100):
    gr = scientists_buffer(
        10,# num_scientists,
	    3,# num_comunicators, # extra scientists
	    20,# num_others,
	    1,# inf_truth,
	    0.5,# inf_scientists_scientists,
	    0.2,# inf_scientists_others,
	    0.0,# inf_others_scientists,
	    0.3,# inf_others_others,
	    FUNCTION,# updt_truth,
	    FUNCTION,# updt_scientists,
	    FUNCTION,# updt_others
	    # # tolerance values
	    1,# out_tol_truth,
	    2*i/99-1,# in_tol_scientists,
	    1,# out_tol_scientists,
	    2*i/99-1,# in_tol_others,
	    1,# out_tol_others,
	    (build_belief, (3/5,1)),# bel_scientists_distr,
	    (build_belief, (0,1/4)),# bel_others_distr,
	    1,# bel_truth = 1.0,
	    True,# backfire_effect = True,
	    False#comunicators_see_truth
    )
    backfire_all.append(gr)
scientists_buffer_param_list.append((backfire_all,"backfire_all"+NAME))

boomerang_others = []
for i in range(100):
    gr = scientists_buffer(
	    10,# num_scientists,
	    3,# num_comunicators, # extra scientists
	    20,# num_others,
	    1,# inf_truth,
	    0.5,# inf_scientists_scientists,
	    0.2,# inf_scientists_others,
	    0.0,# inf_others_scientists,
	    0.3,# inf_others_others,
	    FUNCTION,# updt_truth,
	    FUNCTION,# updt_scientists,
	    FUNCTION,# updt_others
	    # # tolerance values
	    1,# out_tol_truth,
	    1,# in_tol_scientists,
	    1,# out_tol_scientists,
	    1,# in_tol_others,
	    2*i/99-1,# out_tol_others,
	    (build_belief, (3/5,1)),# bel_scientists_distr,
	    (build_belief, (0,1/4)),# bel_others_distr,
	    1,# bel_truth = 1.0,
	    False,# backfire_effect = False,
	    False#comunicators_see_truth
    )
    boomerang_others.append(gr)
scientists_buffer_param_list.append((boomerang_others,"boomerang_others"+NAME))
boomerang_scientists = []
for i in range(100):
    gr = scientists_buffer(
        10,# num_scientists,
	    3,# num_comunicators, # extra scientists
	    20,# num_others,
	    1,# inf_truth,
	    0.5,# inf_scientists_scientists,
	    0.2,# inf_scientists_others,
	    0.0,# inf_others_scientists,
	    0.3,# inf_others_others,
	    FUNCTION,# updt_truth,
	    FUNCTION,# updt_scientists,
	    FUNCTION,# updt_others
	    # # tolerance values
	    1,# out_tol_truth,
	    1,# in_tol_scientists,
	    2*i/99-1,# out_tol_scientists,
	    1,# in_tol_others,
	    1,# out_tol_others,
	    (build_belief, (3/5,1)),# bel_scientists_distr,
	    (build_belief, (0,1/4)),# bel_others_distr,
	    1,# bel_truth = 1.0,
	    False,# backfire_effect = False,
	    False#comunicators_see_truth
    )
    boomerang_scientists.append(gr)
scientists_buffer_param_list.append((boomerang_scientists,"boomerang_scientists"+NAME))
boomerang_all = []
for i in range(100):
    gr = scientists_buffer(
        10,# num_scientists,
	    3,# num_comunicators, # extra scientists
	    20,# num_others,
	    1,# inf_truth,
	    0.5,# inf_scientists_scientists,
	    0.2,# inf_scientists_others,
	    0.0,# inf_others_scientists,
	    0.3,# inf_others_others,
	    FUNCTION,# updt_truth,
	    FUNCTION,# updt_scientists,
	    FUNCTION,# updt_others
	    # # tolerance values
	    1,# out_tol_truth,
	    1,# in_tol_scientists,
	    2*i/99-1,# out_tol_scientists,
	    1,# in_tol_others,
	    2*i/99-1,# out_tol_others,
	    (build_belief, (3/5,1)),# bel_scientists_distr,
	    (build_belief, (0,1/4)),# bel_others_distr,
	    1,# bel_truth = 1.0,
	    False,# backfire_effect = False,
	    False#comunicators_see_truth
    )
    boomerang_all.append(gr)
scientists_buffer_param_list.append((boomerang_all,"boomerang_all"+NAME))
simulate((scientists_buffer_param_list,"scientists_buffer"+NAME))
del scientists_buffer_param_list



many_sides_param_list = []
print(1)
numsides = []
for i in range(100):
    gr = many_sides(
	    ## number of sides, agents initially defending sides and neutral agents
        int(100*i/99+2),#num_sides,
        [2 for i in range(int(100*i/99+2))],#num_agents_sides,
        10,#num_neutral_agents,
        ## influences from the sides to agents, and from agent to agent
        1,#influences_sides_agent,
        0.5,#influence_agent_agent,
        ## update function
        FUNCTION,#agent_update,
        ## tolerances
        1,#in_tolerance_agent,
        1,#out_tolerance_agent,
        1,#out_tolerance_sides,
        ## value of agent defend side is side_value +- side_diff
        0.1,#side_diff,
        ## interval of belief values of neutral agents
        0.3,#neutral_low = 0,
        0.7,#neutral_high = 1,
        ## will we use backfire-effect? (or boomerang effect?)
        True,#is_backfire = True
        True# ignore_constant = False
    )
    numsides.append(gr)
many_sides_param_list.append((numsides,"numsides"+NAME))
sideinf = []
for i in range(100):
    gr = many_sides(
        ## number of sides, agents initially defending sides and neutral agents
        5,#num_sides,
        [2 for i in range(5)],#num_agents_sides,
        10,#num_neutral_agents,
        ## influences from the sides to agents, and from agent to agent
        i/99,#influences_sides_agent,
        0.5,#influence_agent_agent,
        ## update function
        FUNCTION,#agent_update,
        ## tolerances
        1,#in_tolerance_agent,
        1,#out_tolerance_agent,
        1,#out_tolerance_sides,
        ## value of agent defend side is side_value +- side_diff
        0.1,#side_diff,
        ## interval of belief values of neutral agents
        0.3,#neutral_low = 0,
        0.7,#neutral_high = 1,
        ## will we use backfire-effect? (or boomerang effect?)
        True,#is_backfire = True
        False# ignore_constant = False
    )
    sideinf.append(gr)
many_sides_param_list.append((sideinf,"sideinf"+NAME))
sideagentssize = []
for i in range(100):
    gr = many_sides(
        ## number of sides, agents initially defending sides and neutral agents
        5,#num_sides,
        [int(100*i/99+2) for j in range(5)],#num_agents_sides,
        10,#num_neutral_agents,
        ## influences from the sides to agents, and from agent to agent
        1,#influences_sides_agent,
        0.5,#influence_agent_agent,
        ## update function
        FUNCTION,#agent_update,
        ## tolerances
        1,#in_tolerance_agent,
        1,#out_tolerance_agent,
        1,#out_tolerance_sides,
        ## value of agent defend side is side_value +- side_diff
        0.1,#side_diff,
        ## interval of belief values of neutral agents
        0.3,#neutral_low = 0,
        0.7,#neutral_high = 1,
        ## will we use backfire-effect? (or boomerang effect?)
        True,#is_backfire = True
        False# ignore_constant = False
    )
    sideagentssize.append(gr)
many_sides_param_list.append((sideagentssize,"sideagentssize"+NAME))

backfire_agent = []
for i in range(100):
    gr = many_sides(
	    ## number of sides, agents initially defending sides and neutral agents
        5,#num_sides,
        [2 for i in range(5)],#num_agents_sides,
        10,#num_neutral_agents,
        ## influences from the sides to agents, and from agent to agent
        1,#influences_sides_agent,
        0.5,#influence_agent_agent,
        ## update function
        FUNCTION,#agent_update,
        ## tolerances
        2*i/99-1,#in_tolerance_agent,
        1,#out_tolerance_agent,
        1,#out_tolerance_sides,
        ## value of agent defend side is side_value +- side_diff
        0.1,#side_diff,
        ## interval of belief values of neutral agents
        0.3,#neutral_low = 0,
        0.7,#neutral_high = 1,
        ## will we use backfire-effect? (or boomerang effect?)
        True,#is_backfire = True
        False# ignore_constant = False
    )
    backfire_agent.append(gr)
many_sides_param_list.append((backfire_agent,"backfire_agent"+NAME))
boomerang_agents = []
for i in range(100):
    gr = many_sides(
        ## number of sides, agents initially defending sides and neutral agents
        5,#num_sides,
        [2 for i in range(5)],#num_agents_sides,
        10,#num_neutral_agents,
        ## influences from the sides to agents, and from agent to agent
        1,#influences_sides_agent,
        0.5,#influence_agent_agent,
        ## update function
        FUNCTION,#agent_update,
        ## tolerances
        1,#in_tolerance_agent,
        2*i/99-1,#out_tolerance_agent,
        1,#out_tolerance_sides,
        ## value of agent defend side is side_value +- side_diff
        0.1,#side_diff,
        ## interval of belief values of neutral agents
        0.3,#neutral_low = 0,
        0.7,#neutral_high = 1,
        ## will we use backfire-effect? (or boomerang effect?)
        False,#is_backfire = True
        False# ignore_constant = False
    )
    boomerang_agents.append(gr)
many_sides_param_list.append((boomerang_agents,"boomerang_agents"+NAME))
boomerang_sides = []
for i in range(100):
    gr = many_sides(
        ## number of sides, agents initially defending sides and neutral agents
        5,#num_sides,
        [2 for i in range(5)],#num_agents_sides,
        10,#num_neutral_agents,
        ## influences from the sides to agents, and from agent to agent
        1,#influences_sides_agent,
        0.5,#influence_agent_agent,
        ## update function
        FUNCTION,#agent_update,
        ## tolerances
        1,#in_tolerance_agent,
        1,#out_tolerance_agent,
        2*i/99-1,#out_tolerance_sides,
        ## value of agent defend side is side_value +- side_diff
        0.1,#side_diff,
        ## interval of belief values of neutral agents
        0.3,#neutral_low = 0,
        0.7,#neutral_high = 1,
        ## will we use backfire-effect? (or boomerang effect?)
        False,#is_backfire = True
        False# ignore_constant = False
    )
    boomerang_sides.append(gr)
many_sides_param_list.append((boomerang_sides,"boomerang_sides"+NAME))
unilateral_amt = []
for i in range(100):
    gr = many_sides(
        ## number of sides, agents initially defending sides and neutral agents
        5,#num_sides,
        [int(100*i/99+2)]+[2 for i in range(4)],#num_agents_sides,
        10,#num_neutral_agents,
        ## influences from the sides to agents, and from agent to agent
        1,#influences_sides_agent,
        0.5,#influence_agent_agent,
        ## update function
        FUNCTION,#agent_update,
        ## tolerances
        1,#in_tolerance_agent,
        1,#out_tolerance_agent,
        1,#out_tolerance_sides,
        ## value of agent defend side is side_value +- side_diff
        0.1,#side_diff,
        ## interval of belief values of neutral agents
        0.3,#neutral_low = 0,
        0.7,#neutral_high = 1,
        ## will we use backfire-effect? (or boomerang effect?)
        True,#is_backfire = True
        False# ignore_constant = False
    )
    unilateral_amt.append(gr)
many_sides_param_list.append((unilateral_amt,"unilateral_amt"+NAME))
neutral_amt = []
for i in range(100):
    gr = many_sides(
        ## number of sides, agents initially defending sides and neutral agents
        5,#num_sides,
        [2 for i in range(5)],#num_agents_sides,
        int(100*i/99+2),#num_neutral_agents,
        ## influences from the sides to agents, and from agent to agent
        1,#influences_sides_agent,
        0.5,#influence_agent_agent,
        ## update function
        FUNCTION,#agent_update,
        ## tolerances
        1,#in_tolerance_agent,
        1,#out_tolerance_agent,
        1,#out_tolerance_sides,
        ## value of agent defend side is side_value +- side_diff
        0.1,#side_diff,
        ## interval of belief values of neutral agents
        0.3,#neutral_low = 0,
        0.7,#neutral_high = 1,
        ## will we use backfire-effect? (or boomerang effect?)
        True,#is_backfire = True
        False# ignore_constant = False
    )
    neutral_amt.append(gr)
many_sides_param_list.append((neutral_amt,"neutral_amt"+NAME))
simulate((many_sides_param_list,"many_sides"+NAME))
del many_sides_param_list