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