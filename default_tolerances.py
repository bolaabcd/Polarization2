from enum import Enum
import numpy as np

def build_tol_list_constant(num_agents,tolerance_value):
    return [tolerance_value for i in range(num_agents)]

def build_tol_list_random(num_agents):
    return np.ndarray.tolist(np.random.uniform(-1,1,num_agents))

class Tolerance(Enum):
    CONSTANT = 0
    RANDOM = 1

def build_tol_list(
        tol_type: Tolerance,
        num_agents,
        tolerance_value=None,
        ):
    if tol_type is Tolerance.CONSTANT:
        if tolerance_value is None:
            raise ValueError("Invalid tolerance value.")
        return build_tol_list_constant(num_agents, tolerance_value)
    if tol_type is Tolerance.RANDOM:
        return build_tol_list_random(num_agents)
    raise Exception("tol_type not recognized. Expected an `Tolerance`")
