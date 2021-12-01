"""
Copyright (c) 2020 Santiago Quintero Pabón <Sirquini>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from society_graph import Society_Graph
import numpy as np

class Simulation:
    def __init__(self,society : Society_Graph):
        self.society = society
        
    def __iter__(self):
        return self

    def __next__(self):
        result = self.society.get_beliefs()
        self.society.update_beliefs()
        return result

    def run(self, max_time : int=100, smart_stop : bool=True):
        belief_history = []
        for _, belief_vec_state in zip(range(max_time), self):
            # Stop if a stable state is reached
            if smart_stop and belief_history and np.array_equal(belief_history[-1], belief_vec_state):
                break
            belief_history.append(belief_vec_state)
        return np.array(belief_history)
    def get_final_state(self,max_time=50000 ,tolerance=1e-6):
        previous_belief=np.array([])
        for _, (belief_vec_state, pol_state) in zip(range(max_time), self):
            if (previous_belief.size> 0) and np.linalg.norm(previous_belief-belief_vec_state)<=tolerance:
                return belief_vec_state
            previous_belief=belief_vec_state
        return belief_vec_state
        