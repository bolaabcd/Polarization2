from types import FunctionType
import numpy as np

def same(num_agents : int, f : FunctionType) -> np.ndarray:
    return np.full((num_agents,num_agents), f)