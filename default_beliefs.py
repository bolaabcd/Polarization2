"""
Copyright (c) 2020 Santiago Quintero Pabón <Sirquini>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import math
from enum import Enum
import numpy as np

class Default_Belief(Enum):
    UNIFORM = 0
    MILD = 1
    EXTREME = 2
    TRIPLE = 3
    RANDOM = 4

def build_belief(belief_type: Default_Belief, num_agents : int, initval: float = 0, finval: float = 1):
    assert(finval >= initval)
    dif = finval-initval
    if belief_type is Default_Belief.MILD:
        middle = math.ceil(num_agents / 2)
        return [initval+dif*(0.2 + 0.2 * i / middle) if i < middle else initval+dif*(0.6 + 0.2 * (i - middle) / (num_agents - middle)) for i in range(num_agents)]
    if belief_type is Default_Belief.EXTREME:
        middle = math.ceil(num_agents / 2)
        return [initval + dif*(0.2 * i / middle) if i < middle else initval+dif*(0.8 + 0.2 * (i - middle) / (num_agents - middle)) for i in range(num_agents)]
    if belief_type is Default_Belief.TRIPLE:
        beliefs = [0.0] * num_agents
        first_third = num_agents // 3
        middle_third = math.ceil(num_agents * 2 / 3) - first_third
        last_third = num_agents - middle_third - first_third
        offset = 0
        for i, segment in enumerate((first_third, middle_third, last_third)):
            for j in range(segment):
                beliefs[j+offset] = initval+dif*(0.2 * j / segment + (0.4 * i))
            offset += segment
        return beliefs
    if belief_type is Default_Belief.UNIFORM:
        return [initval+dif*(i/(num_agents - 1)) for i in range(num_agents)]
    if belief_type is Default_Belief.RANDOM:
        return np.ndarray.tolist(np.random.uniform(initval,finval,num_agents))
