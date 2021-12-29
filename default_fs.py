from types import FunctionType


def same(num_agents : int, f : FunctionType):
    return [f for i in range(num_agents)]