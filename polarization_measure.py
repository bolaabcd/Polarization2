"""
Copyright (c) 2020 Santiago Quintero Pabón <Sirquini>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import math
from functools import partial

import numpy as np

######################################################
## Parameters for the Esteban-Ray polarization measure
######################################################

## number of bins when discretizing the belief state
NUM_BINS = 51
## parameter alpha set to what Esteban and Ray suggest
ALPHA = 1.6
## scaling factor for polarization measure
K = 1000

######################################################
## The Esteban-Ray polarization measure implementation
######################################################

def belief_2_dist(belief_vec, num_bins=NUM_BINS):
    """Takes a belief state `belief_vec` and discretizes it into a fixed
    number of bins.
    """
    # stores labels of bins
    # the value of a bin is the medium point of that bin
    bin_labels = [(i + 0.5)/num_bins for i in range(num_bins)]

    # stores the distribution of labels
    bin_prob = [0] * num_bins
    # for all agents...
    for belief in belief_vec:
        # computes the bin into which the agent's belief falls
        bin_ = math.floor(belief * num_bins)
        # treats the extreme case in which belief is 1, putting the result in the right bin.
        if bin_ == num_bins:
            bin_ = num_bins - 1
        # updates the frequency of that particular belief
        bin_prob[bin_] += 1 / len(belief_vec)
    # bundles into a matrix the bin_labels and bin_probabilities.
    dist = np.array([bin_labels,bin_prob])
    # returns the distribution.
    return dist

def make_belief_2_dist_func(num_bins=NUM_BINS):
    """Returns a function that discretizes a belief state into a `num_bins`
    number of bins.
    """
    _belief_2_dist = partial(belief_2_dist, num_bins=num_bins)
    _belief_2_dist.__name__ = belief_2_dist.__name__
    _belief_2_dist.__doc__ = belief_2_dist.__doc__
    return _belief_2_dist

def pol_ER(dist, alpha=ALPHA, K=K):
    """Computes the Esteban-Ray polarization of a distribution.
    """
    # recover bin labels
    bin_labels = dist[0]
    # recover bin probabilities
    bin_prob = dist[1]

    diff = np.ones((len(bin_labels), 1)) @ bin_labels[np.newaxis]
    diff = np.abs(diff - np.transpose(diff))
    pol = (bin_prob ** (1 + alpha)) @ diff @ bin_prob
    # scales the measure by the constant K, and returns it.
    return K * pol

def make_pol_er_func(alpha=ALPHA, K=K):
    """Returns a function that computes the Esteban-Ray polarization of a
    distribution with set parameters `alpha` and `K`
    """
    _pol_ER = partial(pol_ER, alpha=alpha, K=K)
    _pol_ER.__name__ = pol_ER.__name__
    _pol_ER.__doc__ = pol_ER.__doc__
    return _pol_ER

def pol_ER_discretized(belief_state:list, ignore_these_indexes:list = [], alpha=ALPHA, K=K, num_bins=NUM_BINS):
    """Discretize belief state as necessary for computing Esteban-Ray
    polarization and computes it.
    """
    # ignore_these_indexes = []
    filtered_belief_state = [v for i ,v in enumerate(belief_state) if i not in ignore_these_indexes]
    return pol_ER(belief_2_dist(filtered_belief_state, num_bins), alpha, K)

def make_pol_er_discretized_func(alpha=ALPHA, K=K, num_bins=NUM_BINS):
    """Returns a function that computes the Esteban-Ray polarization of a
    belief state, discretized into a `num_bins` number of bins, with set
    parameters `alpha` and `K`.
    """
    _pol_ER_discretized = partial(pol_ER_discretized, alpha=alpha, K=K, num_bins=num_bins)
    _pol_ER_discretized.__name__ = pol_ER_discretized.__name__
    _pol_ER_discretized.__doc__ = pol_ER_discretized.__doc__
    return _pol_ER_discretized


######################################################
## Extra
######################################################

def get_max_pol(number_of_agents):
    elements1 = [0 for i in range(number_of_agents//2)] + [1 for i in range(number_of_agents//2 + number_of_agents%2)]
    elements2 = [0 for i in range(number_of_agents//2 + number_of_agents%2)] + [1 for i in range(number_of_agents//2)]
    return max(pol_ER_discretized(elements1),pol_ER_discretized(elements2))