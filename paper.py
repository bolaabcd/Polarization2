import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
from networkx.drawing import draw_networkx,multipartite_layout

from belief_update_fs import non_norm_quadratic_update, line_update
from default_beliefs import build_belief, Belief_Type
from default_influences import build_influence, Default_Influence
from default_tolerances import build_tol_matrix_backfire
from example_cases import simple_clique_uniform, tripartite_uniform
from society_graph import Society_Graph, INFLUENCE_VALUE, COLOR
from main_cases import scientists_buffer, many_sides

np.random.seed(123456)

if not os.path.exists("generated/"):
    os.mkdir("generated/")
if not os.path.exists("generated/paper/"):
    os.mkdir("generated/paper/")

def plot_function(f,k):
	plt.close()
	x = np.linspace(-1,1,1000)
	y = f(x,k)
	y = np.clip(y,-1,1)
	fig, ax = plt.subplots()
	line, = ax.plot([])
	ax.set_xlim(-1, 1)
	ax.set_ylim(-1.02, 1.02)
	ax.grid(True, which='both')
	ax.axhline(y=0, color='k')
	ax.axvline(x=0, color='k')
	ax.plot(x,y, color = '#880000')

# 1) Simple classical model example: influence for each edge
func = line_update 
k = 1
classical = simple_clique_uniform(15,func,0,1,k,1)
for i in range(15):
    for j in range(15):
        if i != j:
            num = np.random.random()
            while num == 0:
                num = np.random.random()
            classical.graph[i][j][INFLUENCE_VALUE] = num

classical.quick_update(30)
plt.close()
classical.plot_history()
plt.savefig("generated/paper/hist_classical.svg")
plt.close()
classical.plot_polarization()
plt.savefig("generated/paper/pol_classical.svg")
plt.close()
classical.plot_hist_pol()
plt.savefig("generated/paper/hp_classical.svg")
plt.close()
classical.draw_graph()
plt.savefig("generated/paper/clique.svg")
plot_function(func,k)
plt.savefig("generated/paper/func_classical.svg")
plt.close()

# 2) Confirmation-Bias example from last paper: influence + beta 
func = non_norm_quadratic_update
k = 0
cbias = simple_clique_uniform(15,func,0,1,k,1)
for i in range(15):
    for j in range(15):
        if i != j:
            cbias.graph[i][j][INFLUENCE_VALUE] = classical.graph[i][j][INFLUENCE_VALUE]

cbias.quick_update(30)
plt.close()
cbias.plot_history()
plt.savefig("generated/paper/hist_cbias.svg")
plt.close()
cbias.plot_polarization()
plt.savefig("generated/paper/pol_cbias.svg")
plt.close()
cbias.plot_hist_pol()
plt.savefig("generated/paper/hp_cbias.svg")
plot_function(func,k)
plt.savefig("generated/paper/func_cbias.svg")
plt.close()


# 3) Reactance example: opposite effect
func = non_norm_quadratic_update
k = -1
reac = simple_clique_uniform(15,func,0,1,k,1)
for i in range(15):
    for j in range(15):
        if i != j:
            reac.graph[i][j][INFLUENCE_VALUE] = classical.graph[i][j][INFLUENCE_VALUE]

reac.quick_update(30)
plt.close()
reac.plot_history()
plt.savefig("generated/paper/hist_reac.svg")
plt.close()
reac.plot_polarization()
plt.savefig("generated/paper/pol_reac.svg")
plt.close()
reac.plot_hist_pol()
plt.savefig("generated/paper/hp_reac.svg")
plot_function(func,k)
plt.savefig("generated/paper/func_reac.svg")
plt.close()

# 4) Super-susceptibility example 1
func = non_norm_quadratic_update
k = 1
supsuc = simple_clique_uniform(15,func,0,1,k,1)
for i in range(15):
    for j in range(15):
        if i != j:
            supsuc.graph[i][j][INFLUENCE_VALUE] = classical.graph[i][j][INFLUENCE_VALUE]

supsuc.quick_update(30)
plt.close()
supsuc.plot_history()
plt.savefig("generated/paper/hist_supsuc.svg")
plt.close()
supsuc.plot_polarization()
plt.savefig("generated/paper/pol_supsuc.svg")
plt.close()
supsuc.plot_hist_pol()
plt.savefig("generated/paper/hp_supsuc.svg")
plot_function(func,k)
plt.savefig("generated/paper/func_supsuc.svg")
plt.close()

#5 Authority Bias
func = non_norm_quadratic_update
k = 1
authbias = tripartite_uniform(
    15,#num_ags_middle,
    0,#belief_value1,
    1,#belief_value2,
    func,#update_function,
    1,#influence_value_1,
    1,#influence_value_mid,
    1,#influence_value_2,
    0,#tolerance_value_1,
    0,#tolerance_value_mid,
    0,#tolerance_value_2,
    1,#influence_value_1mid,
    1,#influence_value_2mid,
    1,#influence_value_mid1,
    1,#influence_value_mid2,
    k,#tolerance_value_1mid,
    0,#tolerance_value_2mid,
    0,#tolerance_value_mid1,
    0,#tolerance_value_mid2,
)

plt.close()
authbias.draw_graph()
plt.savefig("generated/paper/tripartite_graph.svg")
plt.close()

authbias.quick_update(30)
plt.close()
authbias.plot_history()
plt.savefig("generated/paper/hist_authbias.svg")
plt.close()
authbias.plot_polarization()
plt.savefig("generated/paper/pol_authbias.svg")
plt.close()
authbias.plot_hist_pol()
plt.savefig("generated/paper/hp_authbias.svg")
plt.close()

#6 Confirmation-Bias
func = non_norm_quadratic_update
k = 0
cbias2 = tripartite_uniform(
    15,#num_ags_middle,
    0,#belief_value1,
    1,#belief_value2,
    func,#update_function,
    1,#influence_value_1,
    1,#influence_value_mid,
    1,#influence_value_2,
    0,#tolerance_value_1,
    0,#tolerance_value_mid,
    0,#tolerance_value_2,
    1,#influence_value_1mid,
    1,#influence_value_2mid,
    1,#influence_value_mid1,
    1,#influence_value_mid2,
    k,#tolerance_value_1mid,
    0,#tolerance_value_2mid,
    0,#tolerance_value_mid1,
    0,#tolerance_value_mid2,
)

cbias2.quick_update(30)
plt.close()
cbias2.plot_history()
plt.savefig("generated/paper/hist_cbias2.svg")
plt.close()
cbias2.plot_polarization()
plt.savefig("generated/paper/pol_cbias2.svg")
plt.close()
cbias2.plot_hist_pol()
plt.savefig("generated/paper/hp_cbias2.svg")
plt.close()

#7 Backfire-Effect
func = non_norm_quadratic_update
k = -1
bfeffect = tripartite_uniform(
    15,#num_ags_middle,
    0,#belief_value1,
    1,#belief_value2,
    func,#update_function,
    1,#influence_value_1,
    1,#influence_value_mid,
    1,#influence_value_2,
    0,#tolerance_value_1,
    0,#tolerance_value_mid,
    0,#tolerance_value_2,
    1,#influence_value_1mid,
    1,#influence_value_2mid,
    1,#influence_value_mid1,
    1,#influence_value_mid2,
    0,#tolerance_value_1mid,
    0,#tolerance_value_2mid,
    k,#tolerance_value_mid1,
    0,#tolerance_value_mid2,
)

bfeffect.quick_update(30)
plt.close()
bfeffect.plot_history()
plt.savefig("generated/paper/hist_bfeffect.svg")
plt.close()
bfeffect.plot_polarization()
plt.savefig("generated/paper/pol_bfeffect.svg")
plt.close()
bfeffect.plot_hist_pol()
plt.savefig("generated/paper/hp_bfeffect.svg")
plt.close()

#8 Boomerang-Effect
func = non_norm_quadratic_update
k = -1
boomeffect = tripartite_uniform(
    15,#num_ags_middle,
    0,#belief_value1,
    1,#belief_value2,
    func,#update_function,
    1,#influence_value_1,
    1,#influence_value_mid,
    1,#influence_value_2,
    0,#tolerance_value_1,
    0,#tolerance_value_mid,
    0,#tolerance_value_2,
    1,#influence_value_1mid,
    1,#influence_value_2mid,
    1,#influence_value_mid1,
    1,#influence_value_mid2,
    k,#tolerance_value_1mid,
    0,#tolerance_value_2mid,
    0,#tolerance_value_mid1,
    0,#tolerance_value_mid2,
)

boomeffect.quick_update(30)
plt.close()
boomeffect.plot_history()
plt.savefig("generated/paper/hist_boomeffect.svg")
plt.close()
boomeffect.plot_polarization()
plt.savefig("generated/paper/pol_boomeffect.svg")
plt.close()
boomeffect.plot_hist_pol()
plt.savefig("generated/paper/hp_boomeffect.svg")
plt.close()

#9 Puppet-Effect
func = non_norm_quadratic_update
k = 1
puppeteffect = tripartite_uniform(
    15,#num_ags_middle,
    0,#belief_value1,
    1,#belief_value2,
    func,#update_function,
    1,#influence_value_1,
    1,#influence_value_mid,
    1,#influence_value_2,
    0,#tolerance_value_1,
    0,#tolerance_value_mid,
    0,#tolerance_value_2,
    1,#influence_value_1mid,
    1,#influence_value_2mid,
    1,#influence_value_mid1,
    1,#influence_value_mid2,
    0,#tolerance_value_1mid,
    0,#tolerance_value_2mid,
    k,#tolerance_value_mid1,
    0,#tolerance_value_mid2,
)

puppeteffect.quick_update(30)
plt.close()
puppeteffect.plot_history()
plt.savefig("generated/paper/hist_puppeteffect.svg")
plt.close()
puppeteffect.plot_polarization()
plt.savefig("generated/paper/pol_puppeteffect.svg")
plt.close()
puppeteffect.plot_hist_pol()
plt.savefig("generated/paper/hp_puppeteffect.svg")
plt.close()

#10 Scientists Buffer (30 steps)
func = non_norm_quadratic_update
nsc = 7 # scientists
ncom = 3 # comunicators
num = 10 # others
scbuffer30 = scientists_buffer (
    ## ammount of each class (1 truth always)
    nsc,#num_scientists,
    ncom,#num_comunicators, # extra scientists
    num,#num_others,
    ## influence values
    1,#inf_truth_scientists,
    1,#inf_scientists_scientists,
    1,#inf_scientists_others,
    1,#inf_others_scientists,
    1,#inf_others_others,
    ## update functions
    func,#upf_truth_scientists,
    func,#upf_scientists_scientists,
    func,#upf_scientists_others,
    func,#upf_others_scientists,
    func,#upf_others_others,
    ## tolerance values
    0,#tol_truth_scientists,
    0,#tol_scientists_scientists,
    0,#tol_scientists_others,
    0,#tol_others_scientists,
    0,#tol_others_others,
    ## belief values
    (build_belief,(0.6,0.8)),#bel_scientists_distr,
    (build_belief,(0.0,0.4)),#bel_others_distr,
    constant_agents_tol = True,
    random_others = True,#random_others = False
)
plt.close()
draw_networkx(
    scbuffer30.graph,
    node_color = [scbuffer30.graph.nodes[n][COLOR] for n in scbuffer30.graph.nodes],
    edge_color = [scbuffer30.graph[e[0]][e[1]][COLOR] for e in scbuffer30.graph.edges],
    with_labels = False,
    pos = multipartite_layout(scbuffer30.graph, subset_key = "group"),
    # node_size = 30, # 300
    # arrowsize = 3, # 10
    linewidths = 0.1 # 1.0
)
plt.box(False)
#scbuffer30.draw_graph()
plt.savefig("generated/paper/sc_buffer.svg")
plt.close()
scbuffer30.draw_graph()
plt.savefig("generated/paper/sc_buffer_bad_plot.svg")
plt.close()

scbuffer30.quick_update(30)
plt.close()
scbuffer30.plot_history()
plt.savefig("generated/paper/hist_scbuffer30.svg")
plt.close()
scbuffer30.plot_polarization()
plt.savefig("generated/paper/pol_scbuffer30.svg")
plt.close()
scbuffer30.plot_hist_pol()
plt.savefig("generated/paper/hp_scbuffer30.svg")
plt.close()
#11 Scientists Buffer (1000 steps)
func = non_norm_quadratic_update
scbuffer1000 = scientists_buffer (
    ## ammount of each class (1 truth always)
    7,#num_scientists,
    3,#num_comunicators, # extra scientists
    10,#num_others,
    ## influence values
    1,#inf_truth_scientists,
    1,#inf_scientists_scientists,
    1,#inf_scientists_others,
    1,#inf_others_scientists,
    1,#inf_others_others,
    ## update functions
    func,#upf_truth_scientists,
    func,#upf_scientists_scientists,
    func,#upf_scientists_others,
    func,#upf_others_scientists,
    func,#upf_others_others,
    ## tolerance values
    0,#tol_truth_scientists,
    0,#tol_scientists_scientists,
    0,#tol_scientists_others,
    0,#tol_others_scientists,
    0,#tol_others_others,
    ## belief values
    (build_belief,(0.6,0.8)),#bel_scientists_distr,
    (build_belief,(0.0,0.4)),#bel_others_distr,
    constant_agents_tol = True,
    random_others = True,#random_others = False
)
scbuffer1000.quick_update(1000)
plt.close()
scbuffer1000.plot_history()
plt.savefig("generated/paper/hist_scbuffer1000.svg")
plt.close()
scbuffer1000.plot_polarization()
plt.savefig("generated/paper/pol_scbuffer1000.svg")
plt.close()
scbuffer1000.plot_hist_pol()
plt.savefig("generated/paper/hp_scbuffer1000.svg")
plt.close()

#12 Good Backfire (polarization with constant agents)
k = 1
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bf1_const = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    0,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    True,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)

neutralrange = list(range(nsides+nsides*nagsides,good_bf1_const.num_agents))
sidagentsrange = list(range(nsides,nsides+nsides*nagsides))
sidesrange = list(range(0,nsides))

draw_networkx(
    good_bf1_const.graph,
    node_color = [good_bf1_const.graph.nodes[n][COLOR] for n in good_bf1_const.graph.nodes],
    edge_color = [good_bf1_const.graph[e[0]][e[1]][COLOR] for e in good_bf1_const.graph.edges],
    with_labels = False,
    pos = nx.shell_layout(good_bf1_const.graph,[neutralrange,sidagentsrange,sidesrange]),
    # node_size = 30, # 300
    # arrowsize = 3, # 10
    linewidths = 0.1 # 1.0
)

plt.savefig("generated/paper/good_bf.svg")
plt.close()
good_bf1_const.draw_graph()
plt.savefig("generated/paper/good_bf_bad_plot.svg")
plt.close()

good_bf1_const.quick_update(30)
plt.close()
good_bf1_const.plot_history()
plt.savefig("generated/paper/hist_good_bf1_const.svg")
plt.close()
good_bf1_const.plot_polarization()
plt.savefig("generated/paper/pol_good_bf1_const.svg")
plt.close()
good_bf1_const.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bf1_const.svg")
plt.close()


#13 Good Backfire (polarization without constant agents)
k = 1
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bf1 = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    0,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    False,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bf1.quick_update(30)
plt.close()
good_bf1.plot_history()
plt.savefig("generated/paper/hist_good_bf1.svg")
plt.close()
good_bf1.plot_polarization()
plt.savefig("generated/paper/pol_good_bf1.svg")
plt.close()
good_bf1.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bf1.svg")
plt.close()

#14 Good Backfire (polarization with constant agents)
k = -1
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bfminus1_const = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    0,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    True,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bfminus1_const.quick_update(30)
plt.close()
good_bfminus1_const.plot_history()
plt.savefig("generated/paper/hist_good_bfminus1_const.svg")
plt.close()
good_bfminus1_const.plot_polarization()
plt.savefig("generated/paper/pol_good_bfminus1_const.svg")
plt.close()
good_bfminus1_const.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bfminus1_const.svg")
plt.close()


#15 Good Backfire (polarization without constant agents)
k = -1
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bfminus1 = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    0,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    False,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)

good_bfminus1.quick_update(30)
plt.close()
good_bfminus1.plot_history()
plt.savefig("generated/paper/hist_good_bfminus1.svg")
plt.close()
good_bfminus1.plot_polarization()
plt.savefig("generated/paper/pol_good_bfminus1.svg")
plt.close()
good_bfminus1.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bfminus1.svg")
plt.close()

#16 Good Backfire (polarization with constant agents)
k = -0.5
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bfbest_const = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    0,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    True,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bfbest_const.quick_update(30)
plt.close()
good_bfbest_const.plot_history()
plt.savefig("generated/paper/hist_good_bfbest_const.svg")
plt.close()
good_bfbest_const.plot_polarization()
plt.savefig("generated/paper/pol_good_bfbest_const.svg")
plt.close()
good_bfbest_const.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bfbest_const.svg")
plt.close()


#17 Good Backfire (polarization without constant agents)
k = -0.5
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bfbest = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    0,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    False,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bfbest.quick_update(30)
plt.close()
good_bfbest.plot_history()
plt.savefig("generated/paper/hist_good_bfbest.svg")
plt.close()
good_bfbest.plot_polarization()
plt.savefig("generated/paper/pol_good_bfbest.svg")
plt.close()
good_bfbest.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bfbest.svg")
plt.close()

#18 Good Backfire (polarization with constant agents)
k = 0
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bf0_const = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    0,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    True,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bf0_const.quick_update(30)
plt.close()
good_bf0_const.plot_history()
plt.savefig("generated/paper/hist_good_bf0_const.svg")
plt.close()
good_bf0_const.plot_polarization()
plt.savefig("generated/paper/pol_good_bf0_const.svg")
plt.close()
good_bf0_const.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bf0_const.svg")
plt.close()


#19 Good Backfire (polarization without constant agents)
k = 0
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bf0 = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    0,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    False,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bf0.quick_update(30)
plt.close()
good_bf0.plot_history()
plt.savefig("generated/paper/hist_good_bf0.svg")
plt.close()
good_bf0.plot_polarization()
plt.savefig("generated/paper/pol_good_bf0.svg")
plt.close()
good_bf0.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bf0.svg")
plt.close()

# Alternative version: all interactions with same k.
#12 Good Backfire (polarization with constant agents)
k = 1
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bf1_const = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    k,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    True,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)

neutralrange = list(range(nsides+nsides*nagsides,good_bf1_const.num_agents))
sidagentsrange = list(range(nsides,nsides+nsides*nagsides))
sidesrange = list(range(0,nsides))

draw_networkx(
    good_bf1_const.graph,
    node_color = [good_bf1_const.graph.nodes[n][COLOR] for n in good_bf1_const.graph.nodes],
    edge_color = [good_bf1_const.graph[e[0]][e[1]][COLOR] for e in good_bf1_const.graph.edges],
    with_labels = False,
    pos = nx.shell_layout(good_bf1_const.graph,[neutralrange,sidagentsrange,sidesrange]),
    # node_size = 30, # 300
    # arrowsize = 3, # 10
    linewidths = 0.1 # 1.0
)

good_bf1_const.quick_update(30)
plt.close()
good_bf1_const.plot_history()
plt.savefig("generated/paper/hist_good_bf1_const_alt.svg")
plt.close()
good_bf1_const.plot_polarization()
plt.savefig("generated/paper/pol_good_bf1_const_alt.svg")
plt.close()
good_bf1_const.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bf1_const_alt.svg")
plt.close()


#13 Good Backfire (polarization without constant agents)
k = 1
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bf1 = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    k,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    False,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bf1.quick_update(30)
plt.close()
good_bf1.plot_history()
plt.savefig("generated/paper/hist_good_bf1_alt.svg")
plt.close()
good_bf1.plot_polarization()
plt.savefig("generated/paper/pol_good_bf1_alt.svg")
plt.close()
good_bf1.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bf1_alt.svg")
plt.close()

#14 Good Backfire (polarization with constant agents)
k = -1
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bfminus1_const = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    k,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    True,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bfminus1_const.quick_update(30)
plt.close()
good_bfminus1_const.plot_history()
plt.savefig("generated/paper/hist_good_bfminus1_const_alt.svg")
plt.close()
good_bfminus1_const.plot_polarization()
plt.savefig("generated/paper/pol_good_bfminus1_const_alt.svg")
plt.close()
good_bfminus1_const.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bfminus1_const_alt.svg")
plt.close()


#15 Good Backfire (polarization without constant agents)
k = -1
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bfminus1 = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    k,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    False,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)

good_bfminus1.quick_update(30)
plt.close()
good_bfminus1.plot_history()
plt.savefig("generated/paper/hist_good_bfminus1_alt.svg")
plt.close()
good_bfminus1.plot_polarization()
plt.savefig("generated/paper/pol_good_bfminus1_alt.svg")
plt.close()
good_bfminus1.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bfminus1_alt.svg")
plt.close()

#16 Good Backfire (polarization with constant agents)
k = -0.26
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bfbest_const = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    k,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    True,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bfbest_const.quick_update(30)
plt.close()
good_bfbest_const.plot_history()
plt.savefig("generated/paper/hist_good_bfbest_const_alt.svg")
plt.close()
good_bfbest_const.plot_polarization()
plt.savefig("generated/paper/pol_good_bfbest_const_alt.svg")
plt.close()
good_bfbest_const.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bfbest_const_alt.svg")
plt.close()

#17 Good Backfire (polarization without constant agents)
k = -0.26
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bfbest = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    k,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    False,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bfbest.quick_update(30)
plt.close()
good_bfbest.plot_history()
plt.savefig("generated/paper/hist_good_bfbest_alt.svg")
plt.close()
good_bfbest.plot_polarization()
plt.savefig("generated/paper/pol_good_bfbest_alt.svg")
plt.close()
good_bfbest.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bfbest_alt.svg")
plt.close()

#18 Good Backfire (polarization with constant agents)
k = 0
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bf0_const = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    k,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    False,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bf0_const.quick_update(30)
plt.close()
good_bf0_const.plot_history()
plt.savefig("generated/paper/hist_good_bf0_const_alt.svg")
plt.close()
good_bf0_const.plot_polarization()
plt.savefig("generated/paper/pol_good_bf0_const_alt.svg")
plt.close()
good_bf0_const.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bf0_const_alt.svg")
plt.close()


#19 Good Backfire (polarization without constant agents)
k = 0
nsides = 2
nagsides = 3
func = non_norm_quadratic_update
good_bf0 = many_sides(
    ## number of sides, agents initially defending sides and neutral agents
    nsides,#num_sides : int,
    [nagsides for i in range(nsides)],#num_agents_sides : int,
    7,#num_neutral_agents : int,
    ## influences from the sides to agents, and from agent to agent
    1,#influence_sides_agent : np.float64,
    1,#influence_agent_agent : np.float64,
    ## update functions
    func,#update_sides_agent : np.float64,
    func,#update_agent_agent : np.float64,
    ## tolerances
    k,#tolerance_sides_agent : np.float64,
    k,#tolerance_agent_agent : np.float64,
    ## value of agent defend side is side_value +- side_diff
    0.1,#side_diff : np.float64,
    ## interval of belief values of neutral agents
    0,#neutral_low : np.float64 = 0,
    1,#neutral_high : np.float64 = 1,
    ## post-simulation settings
    True,#see_constant_agents: bool = True,
    False,#constant_agents_tol: bool = False,
    #pol_measure : FunctionType = pol_ER_discretized
)
good_bf0.quick_update(30)
plt.close()
good_bf0.plot_history()
plt.savefig("generated/paper/hist_good_bf0_alt.svg")
plt.close()
good_bf0.plot_polarization()
plt.savefig("generated/paper/pol_good_bf0_alt.svg")
plt.close()
good_bf0.plot_hist_pol()
plt.savefig("generated/paper/hp_good_bf0_alt.svg")
plt.close()

#20 Plotting one-to-one functions
func = line_update
k = 0.2
plot_function(func,k)
plt.savefig("generated/paper/func_line_0_2.svg")
plt.close()
k = -1
plot_function(func,k)
plt.savefig("generated/paper/func_line_minus1.svg")
plt.close()
func = non_norm_quadratic_update
k = -0.7
plot_function(func,k)
plt.savefig("generated/paper/func_quad_minus0_7.svg")
plt.close()
k = -0.2
plot_function(func,k)
plt.savefig("generated/paper/func_quad_minus0_2.svg")
plt.close()
k = 0.3
plot_function(func,k)
plt.savefig("generated/paper/func_quad_0_3.svg")
plt.close()
k = 0.6
plot_function(func,k)
plt.savefig("generated/paper/func_quad_0_6.svg")
plt.close()


#21 Super-Susceptibility example 2, 30 steps
func = non_norm_quadratic_update
k = 1
supsuc = simple_clique_uniform(15,func,0,1,k,1)
supsuc.quick_update(30)
plt.close()
supsuc.plot_history()
plt.savefig("generated/paper/hist_supsuc2.svg")
plt.close()
supsuc.plot_polarization()
plt.savefig("generated/paper/pol_supsuc2.svg")
plt.close()
supsuc.plot_hist_pol()
plt.savefig("generated/paper/hp_supsuc2.svg")
plot_function(func,k)
plt.savefig("generated/paper/func_supsuc2.svg")
plt.close()

#22 Super-Susceptibility example 2, 100 steps
func = non_norm_quadratic_update
k = 1
supsuc = simple_clique_uniform(15,func,0,1,k,1)
supsuc.quick_update(100)
plt.close()
supsuc.plot_history()
plt.savefig("generated/paper/hist_supsuc2_100_steps.svg")
plt.close()
supsuc.plot_polarization()
plt.savefig("generated/paper/pol_supsuc2_100_steps.svg")
plt.close()
supsuc.plot_hist_pol()
plt.savefig("generated/paper/hp_supsuc2_100_steps.svg")
plot_function(func,k)
plt.savefig("generated/paper/func_supsuc2.svg")
plt.close()



#23 Regions (daltonism-friendly colors: "#D81B60" "#1E88E5" "#FFC107" "#004D40")
plt.close()
x = np.linspace(-1,1,1000)
plt.fill_between(x,-x/abs(x),color="#D81B60") # reactance
plt.text(0.5,-0.5,"(3)")
plt.fill_between(x,x,color="#FFC107") # resistance
plt.text(0.7,0.3,"(2)")
plt.fill_between(x,x/abs(x),x,color="#1E88E5") # susceptibility
plt.text(0.3,0.7,"(1)")
plt.plot(x,x,color="#004D40") # neutral
plt.text(-0.5,-0.03,"(4)")
plt.plot(x,np.zeros(1000),color="#777777")# balanced
plt.text(-0.7,-0.67,"(5)")

plt.savefig("generated/paper/regions.svg")


#24 extra functions for puppet-effect
from math import atan
k = 1
def supsuc1(x,k):
	y = 0
	if len(np.array(x).shape) == 0:
		y = atan(x)
	elif len(x.shape) == 1:
		y = np.zeros(x.shape)
		for i in range(x.shape[0]):
			y[i] = atan(x[i])
	else:
		y = np.zeros(x.shape)
		assert(len(x.shape) == 2)
		for i in range(x.shape[0]):
			for j in range(x.shape[1]):
				y[i][j] = atan(x[i][j])
	return y/atan(1)
def supsuc2(x,k):
	return np.nan_to_num(x/np.sqrt(abs(x)))
func = supsuc1
plot_function(func,k)
plt.savefig("generated/paper/func_extra_supsuc1.svg")
plt.close()

supsuc = simple_clique_uniform(15,func,0,1,k,1)
supsuc.quick_update(30)
plt.close()
supsuc.plot_history()
plt.savefig("generated/paper/hist_extra_supsuc1.svg")
plt.close()


func = supsuc2
plot_function(func,k)
plt.savefig("generated/paper/func_extra_supsuc2.svg")
plt.close()

supsuc = simple_clique_uniform(15,func,0,1,k,1)
supsuc.quick_update(30)
plt.close()
supsuc.plot_history()
plt.savefig("generated/paper/hist_extra_supsuc2.svg")
plt.close()



#25 extra functions for reactance
from math import sin
k = 1
def reac1(x,k):
	y = 0
	if len(np.array(x).shape) == 0:
		y = -sin(x)
	elif len(x.shape) == 1:
		y = np.zeros(x.shape)
		for i in range(x.shape[0]):
			y[i] = -sin(x[i])
	else:
		y = np.zeros(x.shape)
		assert(len(x.shape) == 2)
		for i in range(x.shape[0]):
			for j in range(x.shape[1]):
				y[i][j] = -sin(x[i][j])
	return y
def reac2(x,k):
	return -x**3
func = reac1
plot_function(func,k)
plt.savefig("generated/paper/func_extra_reac1.svg")
plt.close()

reac = simple_clique_uniform(15,func,0,1,k,1)
reac.quick_update(30)
plt.close()
reac.plot_history()
plt.savefig("generated/paper/hist_extra_reac1.svg")
plt.close()


func = reac2
plot_function(func,k)
plt.savefig("generated/paper/func_extra_reac2.svg")
plt.close()

reac = simple_clique_uniform(15,func,0,1,k,1)
reac.quick_update(30)
plt.close()
reac.plot_history()
plt.savefig("generated/paper/hist_extra_reac2.svg")
plt.close()

#25 extra functions for resilliency
from math import sin
k = 1
def cbias1(x,k):
	y = 0
	if len(np.array(x).shape) == 0:
		y = sin(x)
	elif len(x.shape) == 1:
		y = np.zeros(x.shape)
		for i in range(x.shape[0]):
			y[i] = sin(x[i])
	else:
		y = np.zeros(x.shape)
		assert(len(x.shape) == 2)
		for i in range(x.shape[0]):
			for j in range(x.shape[1]):
				y[i][j] = sin(x[i][j])
	return y
def cbias2(x,k):
	return x**3
func = cbias1
plot_function(func,k)
plt.savefig("generated/paper/func_extra_cbias1.svg")
plt.close()

cbias = simple_clique_uniform(15,func,0,1,k,1)
cbias.quick_update(30)
plt.close()
cbias.plot_history()
plt.savefig("generated/paper/hist_extra_cbias1.svg")
plt.close()


func = cbias2
plot_function(func,k)
plt.savefig("generated/paper/func_extra_cbias2.svg")
plt.close()

cbias = simple_clique_uniform(15,func,0,1,k,1)
cbias.quick_update(30)
plt.close()
cbias.plot_history()
plt.savefig("generated/paper/hist_extra_cbias2.svg")
plt.close()

# Last and simplest plot
k = 0
func = line_update
neutral = simple_clique_uniform(15,func,0,1,k,1)
neutral.quick_update(30)
plt.close()
neutral.plot_history()
plt.savefig("generated/paper/hist_neutral.svg")
plt.close()

