import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
from networkx.drawing import draw_networkx,multipartite_layout

from belief_update_fs import non_norm_quadratic_update, line_update, sig, non_norm_interpolated_update
from default_beliefs import build_belief, Belief_Type
from default_influences import build_influence, Default_Influence
from default_tolerances import build_tol_matrix_backfire
from example_cases import simple_clique_uniform, tripartite_uniform, vaccine
from society_graph import Society_Graph, INFLUENCE_VALUE, COLOR
from main_cases import scientists_buffer, many_sides

np.random.seed(123456)

if not os.path.exists("generated/"):
    os.mkdir("generated/")
if not os.path.exists("generated/paper2/"):
    os.mkdir("generated/paper2/")

def plot_function(f,k, color = '#880000'):
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
	ax.plot(x,y, color = color, linewidth=2)

# Vaccine example
funcs = np.full((6,6), line_update)
funcs[1][0] = non_norm_quadratic_update
funcs[5][0] = non_norm_quadratic_update
funcs[1][3] = non_norm_quadratic_update
funcs[2][3] = non_norm_quadratic_update
tols = np.full((6,6), 1)
tols[1][0] = 0
tols[5][0] = 0
tols[1][3] = 0
tols[2][3] = 0
vac1 = vaccine(tols, functions = funcs)
for i in range(30):
    vac1.update_beliefs_slow()
plt.close()
vac1.plot_history()
plt.savefig("generated/paper2/vaccineCbiasClassic.svg")
plt.close()

# Backfire and Puppet
plot_function(non_norm_quadratic_update,-0.5)
plt.savefig("generated/paper2/func_backfire_05.svg")
plt.close()
plot_function(sig,1)
plt.savefig("generated/paper2/func_sig.svg")
plt.close()

# Vaccine backfire
funcs = np.full((6,6), non_norm_quadratic_update)
tols = np.full((6,6), -0.5)
vac2 = vaccine(tols, functions = funcs)
vac2.quick_update(15)
plt.close()
vac2.plot_history()
plt.savefig("generated/paper2/vaccineBF.svg")
plt.close()



# Vaccine puppet
funcs = np.full((6,6), line_update)
funcs[5][0] = sig
funcs[2][4] = sig
tols = np.full((6,6), 1)
vac3 = vaccine(tols, functions = funcs)
for i in range(50):
    vac3.update_beliefs_slow()
plt.close()
vac3.plot_history()
plt.savefig("generated/paper2/vaccinePuppet.svg")
plt.close()


# Parameter k < 0
plot_function(non_norm_interpolated_update,-1.0)
plt.savefig("generated/paper2/func_kneg_1.svg")
plt.close()
plot_function(non_norm_interpolated_update,-0.25)
plt.savefig("generated/paper2/func_kneg_025.svg")
plt.close()
plot_function(non_norm_interpolated_update,-0.5)
plt.savefig("generated/paper2/func_kneg_05.svg")
plt.close()


# Parameter k >= 0
plot_function(non_norm_interpolated_update,0)
plt.savefig("generated/paper2/func_k_0.svg")
plt.close()
plot_function(non_norm_interpolated_update,0.5)
plt.savefig("generated/paper2/func_k_05.svg")
plt.close()
plot_function(non_norm_interpolated_update,1.0)
plt.savefig("generated/paper2/func_k_1.svg")
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
plt.savefig("generated/paper2/sc_buffer.svg")
plt.close()
scbuffer30.draw_graph()
plt.savefig("generated/paper2/sc_buffer_bad_plot.svg")
plt.close()

scbuffer30.quick_update(30)
plt.close()
scbuffer30.plot_history()
plt.savefig("generated/paper2/hist_scbuffer30.svg")
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
plt.savefig("generated/paper2/hist_scbuffer1000.svg")
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
plt.box(False)

plt.savefig("generated/paper2/good_bf.svg")
plt.close()

good_bf1_const.quick_update(30)
plt.close()
good_bf1_const.plot_history()
plt.savefig("generated/paper2/hist_good_bf1_const.svg")
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
plt.savefig("generated/paper2/hist_good_bfminus1_const.svg")
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
plt.savefig("generated/paper2/hist_good_bfbest_const.svg")
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
plt.savefig("generated/paper2/hist_good_bf0_const.svg")
plt.close()




#23 Regions (daltonism-friendly colors: "#D81B60" "#1E88E5" "#FFC107" "#004D40")
plt.close()
x = np.linspace(-1,1,1000)
plt.fill_between(x,-x/abs(x),color="#D81B60") # reactance
plt.text(0.5,-0.5,"(B)",size='xx-large')
plt.fill_between(x,x,color="#FFC107") # resistance
plt.text(0.7,0.3,"(R)",size='xx-large')
plt.fill_between(x,x/abs(x),x,color="#1E88E5") # susceptibility
plt.text(0.3,0.7,"(M)",size='xx-large')

plt.plot(np.zeros(1000),x,color='#777777')

#plt.plot(x,x,color="#004D40") # neutral
#plt.plot(x,x,color="k",linestyle='-.') # neutral
plt.text(-0.5,-0.03,"(I)",size='xx-large')
#plt.plot(x,np.zeros(1000),color="#777777")# balanced
plt.plot(x,np.zeros(1000),color="k",linestyle = 'dotted')# balanced
#plt.text(-0.7,-0.67,"(I)",size='xx-large')


plt.savefig("generated/paper2/regions.svg")


#23 Functions in three main regions (daltonism-friendly colors: "#D81B60" "#1E88E5" "#FFC107" "#004D40")
pink = "#D81B60"
blue = "#1E88E5"
yellow = "#FFC107"
green = "#00BF7D"
green, pink = pink, green
plt.close()
x = np.linspace(-1,1,1000)
plot_function(lambda v,k:v,1, color = pink)
plt.plot(x,-x**3, linewidth=2, color = yellow)
plt.plot(x,x*(1-np.abs(x)), linewidth=2, color = blue)
#plt.plot(x,sig(x,1), color = "#004D40") # linewidth=2
eps = 0.008
x1 = np.linspace(-1,-eps,1000)
x2 = 0
x3 = np.linspace(eps,1,1000)
plt.plot(x1,sig(x1,1), linewidth=2, color = green)
plt.plot(x3,sig(x3,1), linewidth=2, color = green)
#plt.scatter(x2,sig(x2,1), color = green)
plt.plot(x2,sig(x2,1),'o', color = green, linewidth=2, markersize=4, markerfacecolor=green, markeredgewidth=1)
plt.plot(x2,-1,'o', color = green, linewidth=2, markersize=4, markerfacecolor='#FFFFFF', markeredgewidth=1)
plt.plot(x2, 1,'o', color = green, linewidth=2, markersize=4, markerfacecolor='#FFFFFF', markeredgewidth=1)

plt.savefig("generated/paper2/three_functions.svg")


# Distinct vaccine examples (with distinct biases):
def backf(x,k):
    return -x**3
def degr(x,k):
    return x
# Vaccine Consensus
funcs = np.full((6,6), non_norm_quadratic_update)
funcs[0][1] = sig
funcs[5][0] = backf
funcs[1][3] = degr
funcs[1][0] = degr
tols = np.full((6,6), 0)
vacC = vaccine(tols, functions = funcs)
for i in range(75):
    vacC.update_beliefs_slow()
plt.close()
vacC.plot_history()
plt.savefig("generated/paper2/vaccineCmany.svg")
plt.close()

# Vaccine Flip Flop
funcs = np.full((6,6), non_norm_quadratic_update)
funcs[2][4] = sig
funcs[2][3] = backf
funcs[4][5] = degr
funcs[5][0] = degr
tols = np.full((6,6), 0)
vacFF = vaccine(tols, functions = funcs)
for i in range(75):
    vacFF.update_beliefs_slow()
plt.close()
vacFF.plot_history()
plt.savefig("generated/paper2/vaccineFFmany.svg")
plt.close()

# Vaccine Stable Disagreement
funcs = np.full((6,6), non_norm_quadratic_update)
funcs[0][1] = sig
funcs[5][0] = backf
funcs[2][4] = backf
funcs[3][5] = degr
funcs[4][5] = degr
tols = np.full((6,6), 0)
vacSD = vaccine(tols, functions = funcs)
for i in range(75):
    vacSD.update_beliefs_slow()
plt.close()
vacSD.plot_history()
plt.savefig("generated/paper2/vaccineSDmany.svg")
plt.close()


# Vaccine with only one bias:
# Vaccine deGroot-only:
funcs = np.full((6,6), degr)
tols = np.full((6,6), 0)
vacDG = vaccine(tols, functions = funcs)
for i in range(75):
    vacDG.update_beliefs_slow()
plt.close()
vacDG.plot_history()
plt.savefig("generated/paper2/vaccineDG.svg")
plt.close()
# Vaccine Cbias-only:
funcs = np.full((6,6), non_norm_quadratic_update)
tols = np.full((6,6), 0)
vacCB = vaccine(tols, functions = funcs)
for i in range(75):
    vacCB.update_beliefs_slow()
plt.close()
vacCB.plot_history()
plt.savefig("generated/paper2/vaccineCB.svg")
plt.close()
# Vaccine fan-only:
funcs = np.full((6,6), sig)
tols = np.full((6,6), 0)
vacF = vaccine(tols, functions = funcs)
for i in range(75):
    vacF.update_beliefs_slow()
plt.close()
vacF.plot_history()
plt.savefig("generated/paper2/vaccineF.svg")
plt.close()
# Vaccine backf-only:
funcs = np.full((6,6), backf)
tols = np.full((6,6), 0)
vacBF = vaccine(tols, functions = funcs)
for i in range(7500):
    vacBF.update_beliefs_slow()
plt.close()
vacBF.plot_history()
plt.savefig("generated/paper2/vaccineBF.svg")
plt.close()


# TEST NO CONSENSUS ON RESILIENCY REGION:
def discontinuous(x,k):
    if x <= 1/2 and x >= -1/2:
        return x
    elif x > 1/2:
        return (x-1/2)/5
    else:
        return (x+1/2)/5
f = discontinuous
Gr = Society_Graph(
2,#num_agents : int, 
[0,1],#initial_belief_vector : np.ndarray,
[[0,1],[1,0]],#initial_influence_matrix : np.ndarray,
[[f,f],[f,f]],#initial_fs_matrix : np.ndarray,
[[0,0],[0,0]],#initial_tolerance_matrix : np.ndarray,
#node_colors_vector : np.ndarray = None,
#edge_colors_matrix : np.ndarray = None,
#node_groups_vector : np.ndarray = None,
#see_constant_agents: bool = True,
#constant_agents_tol: bool = False,
#pol_measure : FunctionType = pol_ER_discretized
)

for i in range(10000):
    Gr.update_beliefs_slow()
Gr.plot_history()
#plt.show()
plt.savefig("generated/paper2/TEST_consensus_on_resiliency_region.svg")
plt.close()



 Remaking examples:

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
plt.savefig("generated/paper2/func_extra_supsuc1.svg")
plt.close()

supsuc = simple_clique_uniform(15,func,0,1,k,1)
supsuc.quick_update(30)
plt.close()
supsuc.plot_history()
plt.savefig("generated/paper2/hist_extra_supsuc1.svg")
plt.close()


func = supsuc2
plot_function(func,k)
plt.savefig("generated/paper2/func_extra_supsuc2.svg")
plt.close()

supsuc = simple_clique_uniform(15,func,0,1,k,1)
supsuc.quick_update(30)
plt.close()
supsuc.plot_history()
plt.savefig("generated/paper2/hist_extra_supsuc2.svg")
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
plt.savefig("generated/paper2/func_extra_cbias1.svg")
plt.close()

cbias = simple_clique_uniform(15,func,0,1,k,1)
cbias.quick_update(15)
plt.close()
cbias.plot_history()
plt.savefig("generated/paper2/hist_extra_cbias1.svg")
plt.close()


func = cbias2
plot_function(func,k)
plt.savefig("generated/paper2/func_extra_cbias2.svg")
plt.close()

cbias = simple_clique_uniform(15,func,0,1,k,1)
cbias.quick_update(10000)
plt.close()
cbias.plot_history()
plt.savefig("generated/paper2/hist_extra_cbias2.svg")
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
plt.savefig("generated/paper2/func_extra_reac1.svg")
plt.close()

reac = simple_clique_uniform(15,func,0,1,k,1)
reac.quick_update(30)
plt.close()
reac.plot_history()
plt.savefig("generated/paper2/hist_extra_reac1.svg")
plt.close()


func = reac2
plot_function(func,k)
plt.savefig("generated/paper2/func_extra_reac2.svg")
plt.close()

reac = simple_clique_uniform(15,func,0,1,k,1)
reac.quick_update(30)
plt.close()
reac.plot_history()
plt.savefig("generated/paper2/hist_extra_reac2.svg")
plt.close()
