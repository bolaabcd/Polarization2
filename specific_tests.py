import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
from networkx.drawing import draw_networkx,multipartite_layout
from sqlalchemy import false

from belief_update_fs import quadratic_update, cubic_update, modulus_update
from default_beliefs import build_belief, Default_Belief
from default_influences import build_influence, Default_Influence
from example_cases import simple_clique_uniform, all_edges
from society_graph import Society_Graph
from main_cases import scientists_buffer

# # Counter-example to show that varying functions and keeping the trigger point can vary
# # the final result (even consensus x not consensus)
# f1 = modulus_update

# f2 = quadratic_update

# consensus = Society_Graph(
#     3,
#     [0,1/2,1],
#     np.array([
#         [0,1,1],
#         [1,0,1],
#         [1,1,0]
#     ]),
#     [-1/4+0.08,-1/4+0.08,-1/4+0.08],
#     [f1,f1,f1]
# )

# not_consensus = Society_Graph(
#     3,
#     [0,1/2,1],
#     np.array([
#         [0,1,1],
#         [1,0,1],
#         [1,1,0]
#     ]),
#     [-1/4+0.08,-1/4+0.08,-1/4+0.08],
#     [f2,f2,f2]
# )

# consensus.quick_update(10000)

# not_consensus.quick_update(10000)

# plt.close()
# consensus.plot_history()
# plt.show()

# plt.close()
# not_consensus.plot_history()
# plt.show()


# # ??? I don't remember what is this one below

# amt = np.float128(32) # need to be > 16 to have error. Doesn't seem like precision error
# amtint = int(32) # Precision error if not potency of 2
# sufficient_backfire = Society_Graph(
#     amtint,
#     [i/(amt/2) for i in range(int(amtint/2+1))] + [((amt/2)-i)/(amt/2) for i in range(1,int(amtint/2))],
#     np.zeros((amtint,amtint)),
#     [-1+1/(amt/2)+1/amt for i in range(amtint)],
#     [ modulus_update for i in range(amtint)]
# )

# edges_list = []
# for i in range(amtint):
#     edges_list.append((i,(i+1)%int(amtint)))
# sufficient_backfire.graph.add_edges_from(edges_list,inf = 1/2**1)

# sufficient_backfire.quick_update(100000)
# plt.close()
# sufficient_backfire.plot_history()
# plt.show()
# plt.close()
# sufficient_backfire.draw_graph()
# plt.show()


# # Counter-example for conjecture 0: only the upper area has possibility of loop
# def custom_update(x: float, k: float):
#     # if x == 21/44:
#     #     return 1/11
#     # elif x == 23/44:
#     #     return 2/11
#     # else:
#     #     return x
#     # return -0.5980613476016168*x+3.4616976781016175*x**3
#     # return -0.8522587531805252*x+5.507925284014483*x**3-4.084017159640487*x**5
#     # return np.clip(0.6095308226130123*x**1-9.033574506100722*x**3+41.73519403531996*x**5-44.57516331569474*x**7,-1,1)
#     return np.clip(+0.7352331639166123*x**1-13.137943850988574*x**3+74.86656948902157*x**5-146.2998593949886*x**7+115.89143560705207*x**9-31.91752272632385*x**11,-1,1)
# val = 21/44
# loop_in_yellow_area = Society_Graph(
#     3,
#     [1,val,0],
#     np.array([[0,1,0],[0,0,0],[0,1,0]]),
#     [1,1,1],
#     [custom_update for i in range(3)]
# )
# loop_in_yellow_area.quick_update(100)
# # for i in range(100):
# #     loop_in_yellow_area.update_beliefs()
# plt.close()
# loop_in_yellow_area.plot_history()
# plt.show()
# plt.close()
# loop_in_yellow_area.draw_graph()
# plt.show()
# plt.close()
# x = np.linspace(-1,1,1000)
# # y =-1.0066483574307916*x**1+6.750724240059645*x**3-6.564490127459426*x**5
# # y = -0.5980613476016168*x+3.4616976781016175*x**3
# y =+0.7352331639166123*x**1-13.137943850988574*x**3+74.86656948902157*x**5-146.2998593949886*x**7+115.89143560705207*x**9-31.91752272632385*x**11
# y = np.clip(y,-1,1)
# plt.plot(x,y)
# plt.plot(x,x)
# plt.plot(x,np.zeros(x.shape))
# plt.plot(np.zeros(y.shape),x)
# plt.show()
# plt.close()


# # Case where backfire-effect is good:

# f1 = quadratic_update
# # tolv = 1 # not consensus
# tolv = -1/2 # consensus (except extremes)
# # tolv = -1/2-1/8-1/256-1/512-1/2**13-1/2**15 # as many time steps as wanted, groups reverse
# # tolv=-1/2-1/16-1/64-1/128-1/512 # 5 agents in the middle
# # tolv=-1/2-1/8-1/256-1/512-1/2**13-1/2**15-1/2**16-1/2**20-1/2**22 # with 500 time steps
# # tolv = -3/4
# good_bf = Society_Graph(
#     1,
#     [0],
#     np.array([[0]]),
#     [1],
#     [f1]
# )

# botton_group = simple_clique_uniform(10,f1,0.1,0.3,tolv,1)
# middle_group = simple_clique_uniform(10,f1,0.4,0.6,tolv,1)
# top_group = simple_clique_uniform(10,f1,0.7,0.9,tolv,1)
# last_one = Society_Graph(1,[1],np.array([[0]]),[1],[f1])

# # nx.set_node_attributes(good_bf.graph,1,"subset")
# # nx.set_node_attributes(botton_group.graph,2,"subset")
# # nx.set_node_attributes(middle_group.graph,3,"subset")
# # nx.set_node_attributes(top_group.graph,4,"subset")


# good_bf.append(botton_group)
# fin1 = good_bf.num_agents
# r1 = range(1,fin1)
# good_bf.append(middle_group)
# fin2 = good_bf.num_agents
# r2 = range(fin1,fin2)
# good_bf.append(top_group)
# r3 = range(fin2,good_bf.num_agents)
# good_bf.append(last_one)
# lpos = good_bf.num_agents-1
# good_bf.graph.add_edges_from(all_edges([0],r1),inf=1)
# good_bf.graph.add_edges_from(all_edges([lpos],r3),inf=1)
# good_bf.graph.add_edges_from(all_edges(r1,r2),inf=1)
# good_bf.graph.add_edges_from(all_edges(r3,r2),inf=1)
# good_bf.graph.add_edges_from(all_edges(r2,r1),inf=1)
# good_bf.graph.add_edges_from(all_edges(r2,r3),inf=1)

# red = (1,0,0)
# green = (0,1,0)
# blue = (0,0,1)
# orange = (1,0.5,0)
# lblue = (0,0.5,1)
# # draw_networkx(
# #     good_bf.graph,
# #     node_color=[red]+[orange for i in r1]+[green for i in r2]+[lblue for i in r3] + [blue],
# #     with_labels=False,
# #     pos = multipartite_layout(good_bf.graph)
# # )

# plt.close()
# plt.figure(figsize=(16,10))
# draw_networkx(
#     good_bf.graph,
#     node_color=[red]+[orange for i in r1]+[green for i in r2]+[lblue for i in r3] + [blue],
#     with_labels=False,
#     pos = nx.shell_layout(good_bf.graph,[r2,list(r1)+list(r3),[0,lpos]]),
# )
# if not os.path.exists("generated/Quadratic/two_opposing_groups/"):
#     os.mkdir("generated/Quadratic/two_opposing_groups/")
# plt.savefig("generated/Quadratic/two_opposing_groups/two_opposing_groups.svg")
# # plt.show()


# plt.close()
# good_bf.quick_update(100)
# good_bf.plot_history()
# plt.savefig(f"generated/Quadratic/two_opposing_groups/tol{tolv}.svg")
# # plt.show()

# print(good_bf.get_beliefs()[1], good_bf.get_beliefs()[r2[0]], good_bf.get_beliefs()[r3[0]])

# plt.close()
# good_bf.plot_polarization()
# siz = len(good_bf.polarization_history)
# plt.title(f"Final value = {good_bf.polarization_history[siz-1]}")
# plt.savefig(f"generated/Quadratic/two_opposing_groups/pol_tol{tolv}.svg")
# plt.close()

# # Why I believe we should change the polarization measure:

# from polarization_measure import pol_ER_discretized
# x = np.linspace(0,0.5,1000)
# xp = [[0,0.5-i,0.5+i,1] for i in x]
# y = [pol_ER_discretized(i) for i in xp]
# plt.plot(x,y)
# plt.xlabel('i')
# plt.ylabel('pol([0,0.5-i,0.5+i,1])')
# plt.show()

# # It is bigger if all agents are in the middle!
# # This is why I added the idea that constant agents don't count for polarization.


# # Non-monotonicity of max^t and min^t
# f = quadratic_update
# name = "non_mon"

# gr = Society_Graph(
#     100,
#     [0.03+i/(100 - 1)*0.94 for i in range(100)],
#     build_influence(Default_Influence.CLIQUE,100,general_influence=0.5),
#     [-0.42 for i in range(100)],
#     [f for i in range(100)]
# )
# gr.quick_update(200)
# plt.close()
# gr.plot_history()
# if not os.path.exists("generated/Quadratic/"+name):
#     os.mkdir("generated/Quadratic/"+name)
# plt.savefig("generated/Quadratic/"+name+'/ags.jpg')
# # plt.show()
# plt.close()
# siz = len(gr.polarization_history)
# plt.title(f"Final value = {gr.polarization_history[siz-1]}")
# gr.plot_polarization()
# plt.savefig("generated/Quadratic/"+name+'/pol.jpg')
# # plt.show()
# plt.close()
# gr.draw_graph()
# plt.savefig("generated/Quadratic/"+name+'/'+name+'.jpg')
# # plt.show()
# plt.close()
# x = np.linspace(-1,1)
# y = f(x,-0.42)
# y = np.clip(y,-1,1)
# plt.plot(x,y)
# plt.plot(x,x)
# plt.plot(x,np.zeros(x.shape))
# plt.plot(np.zeros(y.shape),x)
# plt.savefig("generated/Quadratic/"+name+'/f.jpg')
# # plt.show()
# plt.close()


# # necessity of x > 0
# def xgtzero(x,k):
#     k=0.5*k+0.5 # g(k)
    
#     sigx = None
#     sig2 = None
#     if type(x) is float: 
#         sigx = -1
#         sig2 = -1
#         if x >= 0:
#             sigx = 1
#         if 1/2-abs(x) >= 0:
#             sig2 = 1
#     else:
#         sigx = np.copy(x)
#         sigx[sigx >= 0] = 1
#         sigx[sigx <  0] = -1
#         sig2 = np.copy(x)
#         sig2 = 1/2-np.abs(sig2)
#         sig2[sig2 >= 0] = 1
#         sig2[sig2 < 0] = -1



#     y = sigx*(-abs(abs(x)-k)+k)*sig2
#     return y*1/2
# f = xgtzero
# name = "x_greater_than_zero"
# nags = 2
# gr = Society_Graph(
#     nags,
#     [i/(nags-1) for i in range(nags)],
#     build_influence(Default_Influence.CLIQUE,nags,general_influence=1,diagonal_value=1),
#     [(-1/2,-1/2) for i in range(nags)],
#     [f for i in range(nags)]
# )
# gr.quick_update(100)
# plt.close()
# gr.plot_history()
# if not os.path.exists("generated/"+name):
#     os.mkdir("generated/"+name)
# plt.savefig("generated/"+name+'/ags.jpg')
# # plt.show()
# plt.close()
# siz = len(gr.polarization_history)
# plt.title(f"Final value = {gr.polarization_history[siz-1]}")
# gr.plot_polarization()
# plt.savefig("generated/"+name+'/pol.jpg')
# # plt.show()
# plt.close()
# gr.draw_graph()
# plt.savefig("generated/"+name+'/'+name+'.jpg')
# # plt.show()
# plt.close()
# x = np.linspace(-1,1,1000)
# y = f(x,-1/2)
# y = np.clip(y,-1,1)
# plt.plot(x,y)
# plt.plot(x,x)
# plt.plot(x,np.zeros(x.shape))
# plt.plot(np.zeros(y.shape),x)
# plt.savefig("generated/"+name+'/f.jpg')
# # plt.show()
# plt.close()

nsc = 3#10
ncom = 2#3
num = 5#20
f = quadratic_update
name = "scientists_buffer"
gr = scientists_buffer(
    # # ammount of each class (1 truth always)
    nsc,# num_scientists,
    ncom,# num_comunicators, # extra scientists
    num,# num_others,
    # # influence values
    1,# inf_truth,
    0.5,# inf_scientists_scientists,
    0.2,# inf_scientists_others,
    0.1,# inf_others_scientists,
    0.3,# inf_others_others,
    # # update functions
    f,# updt_truth,
    f,# updt_scientists,
    f,# updt_others
    # # tolerance values
    1,# out_tol_truth,
    1,# in_tol_scientists,
    1,# out_tol_scientists,
    1,# in_tol_others,
    1,# out_tol_others,
    # # belief values
    (build_belief, (3/5,1)),# bel_scientists_distr,
    (build_belief, (0,1/4)),# bel_others_distr,
    1,# bel_truth = 1.0,
    # # is this Backfire-Effect? (or is it Boomerang-Effect)
    True# backfire_effect = True
    )
gr.quick_update(700)
plt.close()
gr.plot_history()
if not os.path.exists("generated/"+name):
    os.mkdir("generated/"+name)
# plt.savefig("generated/"+name+'/ags.jpg')
plt.show()
plt.close()
siz = len(gr.polarization_history)
plt.title(f"Final value = {gr.polarization_history[siz-1]}")
gr.plot_polarization()
# plt.savefig("generated/"+name+'/pol.jpg')
plt.show()
plt.close()
red = (1,0,0)
green = (0,1,0)
blue = (0,0,1)
orange = (1,0.5,0)
lblue = (0,0.5,1)
black = (0,0,0)
r1 = range(1,nsc+1)
r2 = range(nsc+1,nsc+ncom+1)
r3 = range(nsc+ncom+1,nsc+ncom+num+1)
# draw_networkx(
#     gr.graph,
#     node_color=[red]+[orange for i in r1]+[green for i in r2]+[blue for i in r3],
#     with_labels=False,
#     pos = nx.shell_layout(gr.graph,[[0],list(r2)+list(r1),list(r3)]),
# )
dic = multipartite_layout(gr.graph, subset_key = "subset")

# # array_op = lambda x: [10*x[0], x[1]]
# array_op = lambda x: np.array([x[0]*10, x[1]])
# # array_op = lambda x: print(np.array(x[0]*2, x[1]))
# # array_op = lambda x: np.array(x[0],x[1])
# # array_op = lambda x: print(np.array([x[0],x[1]]))
# print(dic)
# dic = {p:array_op(dic[p]) for p in dic}
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(dic)

print(gr.graph.number_of_edges())
re1 = range(nsc)
re2 = range(nsc, nsc+ncom)
re3 = range(nsc+ncom,num+nsc)
re4 = range(num+nsc, gr.graph.number_of_edges())
draw_networkx(
    gr.graph,
    node_color = [red]+[orange for i in r1]+[green for i in r2]+[blue for i in r3],
    edge_color = [orange for i in re1] + [green for i in re2] + [blue for i in re4] + [blue for i in re3],
    with_labels = False,
    pos = multipartite_layout(gr.graph, subset_key = "subset"),
    # node_size = 30, # 300
    # arrowsize = 3, # 10
    linewidths = 0.1 # 1.0
)

# plt.savefig("generated/"+name+'/'+name+'.jpg')
plt.show()
plt.close()