from society_graph import Society_Graph
import numpy as np
from belief_update_fs import quadratic_update, cubic_update, modulus_update
import matplotlib.pyplot as plt


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