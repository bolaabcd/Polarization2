from enum import Enum
import numpy as np

def build_tol_list_constant(num_agents, in_tolerance, out_tolerance):
    return [(in_tolerance, out_tolerance) for i in range(num_agents)]

def build_tol_list_random(num_agents):
    rlist = np.ndarray.tolist(np.random.uniform(-1,1,2*num_agents))
    return zip(rlist[::2], rlist[1::2])

class Tolerance(Enum):
    CONSTANT = 0
    RANDOM = 1

def build_tol_list(
        tol_type: Tolerance,
        num_agents,
        in_tolerance = None,
        out_tolerance = None
        ):
    if tol_type is Tolerance.CONSTANT:
        if in_tolerance is None:
            raise ValueError("Invalid tolerance value.")
        elif out_tolerance is None:
            out_tolerance = in_tolerance
        return build_tol_list_constant(num_agents, in_tolerance, out_tolerance)
    if tol_type is Tolerance.RANDOM:
        return build_tol_list_random(num_agents)
    raise Exception("tol_type not recognized. Expected an `Tolerance`")
