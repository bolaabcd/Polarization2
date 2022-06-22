from enum import Enum
import numpy as np

def build_tol_matrix_constant(num_agents : int, tolerance_value : np.float64) -> np.ndarray:
    return np.full((num_agents, num_agents), tolerance_value)

def build_tol_matrix_random(num_agents : int) -> np.ndarray:
    return np.random.uniform(-1, 1, (num_agents, num_agents))


def build_tol_matrix_backfire(num_agents : int, tolerance_list : np.ndarray) -> np.ndarray:
    return np.zeros((num_agents,num_agents)) + np.array([tolerance_list])
def build_tol_matrix_boomerang(num_agents : int, tolerance_list : np.ndarray) -> np.ndarray:
    return build_tol_matrix_backfire(num_agents, tolerance_list).T


class Tolerance(Enum):
    CONSTANT = 0
    RANDOM = 1

def build_tol_list(
        tol_type: Tolerance,
        num_agents: int,
        tol_val : np.float64 = 1
        ):
    if num_agents < 0:
        raise ValueError('Invalid number of agents.')
    if tol_type is Tolerance.CONSTANT:
        return build_tol_list_constant(num_agents, tol_val)
    if tol_type is Tolerance.RANDOM:
        return build_tol_list_random(num_agents)
    raise ValueError('tol_type not recognized. Expected a "Tolerance"')
