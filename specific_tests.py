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