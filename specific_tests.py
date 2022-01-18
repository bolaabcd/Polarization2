from society_graph import Society_Graph
import numpy as np
from belief_update_fs import quadratic_update, cubic_update, modulus_update
import matplotlib.pyplot as plt

f1 = modulus_update

f2 = quadratic_update

consensus = Society_Graph(
    3,
    [0,1/2,1],
    np.array([
        [0,1,1],
        [1,0,1],
        [1,1,0]
    ]),
    [-1/4+0.08,-1/4+0.08,-1/4+0.08],
    [f1,f1,f1]
)

not_consensus = Society_Graph(
    3,
    [0,1/2,1],
    np.array([
        [0,1,1],
        [1,0,1],
        [1,1,0]
    ]),
    [-1/4+0.08,-1/4+0.08,-1/4+0.08],
    [f2,f2,f2]
)

consensus.quick_update(10000)

not_consensus.quick_update(10000)

plt.close()
consensus.plot_history()
plt.show()

plt.close()
not_consensus.plot_history()
plt.show()

amt = np.float128(32) # need to be > 16 to have error. Doesn't seem like precision error
amtint = int(32) # Precision error if not potency of 2
sufficient_backfire = Society_Graph(
    amtint,
    [i/(amt/2) for i in range(int(amtint/2+1))] + [((amt/2)-i)/(amt/2) for i in range(1,int(amtint/2))],
    np.zeros((amtint,amtint)),
    [-1+1/(amt/2)+1/amt for i in range(amtint)],
    [ modulus_update for i in range(amtint)]
)

edges_list = []
for i in range(amtint):
    edges_list.append((i,(i+1)%int(amtint)))
sufficient_backfire.graph.add_edges_from(edges_list,inf = 1/2**1)

sufficient_backfire.quick_update(100)
plt.close()
sufficient_backfire.plot_history()
plt.show()


