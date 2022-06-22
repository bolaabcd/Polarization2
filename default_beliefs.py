"""
Copyright (c) 2020 Santiago Quintero Pabón <Sirquini>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import math
import numpy as np

from enum import Enum

class Belief_Type(Enum):
    UNIFORM = 0
    MILD = 1
    EXTREME = 2
    TRIPLE = 3
    RANDOM = 4

def build_belief(belief_type: Belief_Type, num_agents : int, initval: float = 0, finval: float = 1) -> np.ndarray:
    if finval < initval:
        raise ValueError("Interval given ends before it begins.")
    dif = finval-initval

    if num_agents == 1 and belief_type != Belief_Type.RANDOM:
        return np.array([(initval + finval)/2])

    if belief_type is Belief_Type.MILD:
        middle = math.ceil(num_agents / 2)
        return np.array([initval+dif*(0.2 + 0.2 * i / middle) if i < middle else initval+dif*(0.6 + 0.2 * (i - middle) / (num_agents - middle)) for i in range(num_agents)], dtype = np.float64)

    elif belief_type is Belief_Type.EXTREME:
        middle = math.ceil(num_agents / 2)
        return np.array([initval + dif*(0.2 * i / middle) if i < middle else initval+dif*(0.8 + 0.2 * (i - middle) / (num_agents - middle)) for i in range(num_agents)], dtype = np.float64)
    
    elif belief_type is Belief_Type.TRIPLE:
        beliefs = np.full(num_agents, 0.0, dtype = np.float64)
        first_third = num_agents // 3
        middle_third = math.ceil(num_agents * 2 / 3) - first_third
        last_third = num_agents - middle_third - first_third
        offset = 0
        for i, segment in enumerate((first_third, middle_third, last_third)):
            for j in range(segment):
                beliefs[j+offset] = initval+dif*(0.2 * j / segment + (0.4 * i))
            offset += segment
        return beliefs
    
    elif belief_type is Belief_Type.UNIFORM:
        return np.array([initval+dif*(i/(num_agents - 1)) for i in range(num_agents)], dtype = np.float64)
    
    elif belief_type is Belief_Type.RANDOM:
        return np.random.uniform(initval,finval,num_agents)
    
    else:
        return ValueError('belief_type not recognized. Expected a "Belief_Type"')