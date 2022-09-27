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
plt.close()
x = np.linspace(-1,1,1000)
y = func(x,k)
y = np.clip(y,-1,1)
plt.plot(x,x, color = 'k')
plt.plot(x,np.zeros(x.shape), color = 'k')
plt.plot(np.zeros(y.shape),x, color = 'k')
plt.plot(x,y, color = '#880000')
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
plt.close()
x = np.linspace(-1,1,1000)
y = func(x,k)
y = np.clip(y,-1,1)
plt.plot(x,x, color = 'k')
plt.plot(x,np.zeros(x.shape), color = 'k')
plt.plot(np.zeros(y.shape),x, color = 'k')
plt.plot(x,y, color = '#880000')
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
plt.close()
x = np.linspace(-1,1,1000)
y = func(x,k)
y = np.clip(y,-1,1)
plt.plot(x,x, color = 'k')
plt.plot(x,np.zeros(x.shape), color = 'k')
plt.plot(np.zeros(y.shape),x, color = 'k')
plt.plot(x,y, color = '#880000')
plt.savefig("generated/paper/func_reac.svg")
plt.close()

# 4) Super-susceptibility example
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
plt.close()
x = np.linspace(-1,1,1000)
y = func(x,k)
y = np.clip(y,-1,1)
plt.plot(x,x, color = 'k')
plt.plot(x,np.zeros(x.shape), color = 'k')
plt.plot(np.zeros(y.shape),x, color = 'k')
plt.plot(x,y, color = '#880000')
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
