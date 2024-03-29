"""
Copyright (c) 2020 Santiago Quintero Pabón <Sirquini>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from enum import Enum

import math
import numpy as np

#######################################
## Parameters for influence graphs
#######################################

## for clique influence-graph: influence value of all agents on a clique influence graph
CLIQUE_INF_VALUE = 0.5

## for 2_groups_disconnected influence-graph: influence value of all agents that can communicate in a 2 groups_disconnected influence graph
GROUPS_DISCONNECTED_INF_VALUE = 0.5

## for 2_groups_faint ineraction-function: influence value of all agents that can strongly communicate in a 2 groups faintly connected influence graph
GROUPS_FAINTLY_INF_VALUE_STRONG = 0.5
## for 2_groups_faint ineraction-function: influence value of all agents that can weakly communicate in a 2 groups faintly connected influence graph
GROUPS_FAINTLY_INF_VALUE_WEAK = 0.1

## for 2_influencers_unbalanced influence-graph: level of influence both influencers exert on all others
INFLUENCERS_UNBALANCED_OUTGOING_BOTH = 0.6
## for 2_influencers_unbalanced influence-graph: level of influence both influencers receive from all others
INFLUENCERS_UNBALANCED_INCOMING_BOTH = 0.0
## for 2_influencers_unbalanced influence-graph: level of influence all other agents exert on all others
INFLUENCERS_UNBALANCED_OTHERS = 0.1

## Note that this influence graph is not really balanced by our definition of balanced
## for 2_influencers_balanced influence-graph: level of influence agent 0 exerts on all others
INFLUENCERS_BALANCED_OUTGOING_FIRST = 0.8
## for 2_influencers_balanced influence-graph: level of influence agent n-1 exerts on all others
INFLUENCERS_BALANCED_OUTGOING_SECOND = 0.8
## for 2_influencers_balanced influence-graph: level of influence agent 0 receives from all others
INFLUENCERS_BALANCED_INCOMING_FIRST = 0.1
## for 2_influencers_balanced influence-graph: level of influence agent n-1 receives from all others
INFLUENCERS_BALANCED_INCOMING_SECOND = 0.1
## for 2_influencers_balanced influence-graph: level of influence all other agents exert on all others
INFLUENCERS_BALANCED_OTHERS = 0.2

## for circular influence-graph: influence value of all agents on a circular influence graph
CIRCULAR_INF_VALUE = 0.5

## for random influence graph: minimum influence value
MIN_INF = 0


#####################################
## Default_Influence graphs implementation
#####################################

def build_inf_graph_clique(num_agents : int, influence_value : np.float64, diagonal_value : np.float64 = 0) -> np.ndarray:
    """Returns the influence graph for "clique" scenario."""
    inf_graph = np.full((num_agents, num_agents), influence_value)
    if diagonal_value != None:
        np.fill_diagonal(inf_graph, diagonal_value)
    return inf_graph

def build_inf_graph_2_groups_disconnected(num_agents: int, influence_value : np.float64, diagonal_value : np.float64 = 0) -> np.ndarray:
    """Returns the influence graph for for "disconnected" scenario."""
    inf_graph = np.zeros((num_agents, num_agents))
    middle = math.ceil(num_agents/2)
    inf_graph[:middle, :middle] = influence_value
    inf_graph[middle:, middle:] = influence_value
    if diagonal_value != None:
        np.fill_diagonal(inf_graph, diagonal_value)
    return inf_graph

def build_inf_graph_2_groups_faint(num_agents : int, weak_influence_value : np.float64, strong_influence_value : np.float64, diagonal_value : np.float64 = 0) -> np.ndarray:
    """Returns the influence graph for for "faintly-connected" scenario."""
    inf_graph = np.full((num_agents, num_agents), weak_influence_value)
    middle = math.ceil(num_agents/2)
    inf_graph[:middle, :middle] = strong_influence_value
    inf_graph[middle:, middle:] = strong_influence_value
    if diagonal_value != None:
        np.fill_diagonal(inf_graph, diagonal_value)
    return inf_graph

def build_inf_graph_2_influencers_unbalanced(num_agents : int, influencers_incoming_value : np.float64, influencers_outgoing_value : np.float64, others_influence_value : np.float64, diagonal_value : np.float64 = 0) -> np.ndarray:
    """Returns the influence graph for for "unbalanced 2-influencers" scenario."""
    inf_graph = np.full((num_agents, num_agents), others_influence_value)
    ## Sets the influence of agent 0 on all others
    inf_graph[0, :-1] = influencers_outgoing_value
    ## Sets the influence of agent n-1 on all others
    inf_graph[-1, 1:] = influencers_outgoing_value
    ## Sets the influence of all other agents on agent 0.
    inf_graph[1:,0] = influencers_incoming_value
    ## Sets the influence of all other agents on agent n-1.
    inf_graph[:-1, -1] = influencers_incoming_value
    if diagonal_value != None:
        np.fill_diagonal(inf_graph, diagonal_value)
    return inf_graph

## Note that this influence graph is not really balanced by our definition of balanced
def build_inf_graph_2_influencers_balanced(num_agents : int, influencers_outgoing_value_first : np.float64, influencers_outgoing_value_second : np.float64, influencers_incoming_value_first : np.float64, influencers_incoming_value_second : np.float64, others_influence_value, diagonal_value : np.float64 = 0) -> np.ndarray:
    """Returns the influence graph for for "balanced 2-influencers" scenario."""
    inf_graph = np.full((num_agents, num_agents), others_influence_value)
    ## Sets the influence of agent 0 on all others
    inf_graph[0, :-1] = influencers_outgoing_value_first
    ## Sets the influence of agent n-1 on all others
    inf_graph[-1, 1:] = influencers_outgoing_value_second
    ## Sets the influence of all other agents on agent 0.
    inf_graph[1:, 0] = influencers_incoming_value_first
    ## Sets the influence of all other agents on agent n-1.
    inf_graph[:-1, -1] = influencers_incoming_value_second
    if diagonal_value != None:
        np.fill_diagonal(inf_graph, diagonal_value)
    return inf_graph

def build_inf_graph_circular(num_agents : int, value : np.float64, diagonal_value : np.float64 = 0) -> np.ndarray:
    """Returns the imfluemce graph for "circular influence" scenario."""
    inf_graph = np.zeros((num_agents, num_agents))
    for i in range(num_agents):
        inf_graph[i, i] = 1.0
        inf_graph[i, (i+1) % num_agents] = value
    if diagonal_value != None:
        np.fill_diagonal(inf_graph, diagonal_value)
    return inf_graph

def build_inf_graph_random(num_agents : int, diagonal_value : np.float64 = 0, minimum_influence : np.float64 = MIN_INF) -> np.ndarray:
    conects = np.random.random_integers(0, 1, (num_agents, num_agents))
    rands = np.random.uniform(minimum_influence, 1, (num_agents,num_agents))
    inf_graph = conects*rands
    if diagonal_value != None:
        np.fill_diagonal(inf_graph, diagonal_value)
    return inf_graph

def build_inf_graph_vaccine():
    inf_graph = np.zeros((6,6))
    inf_graph[0][1] = 0.6
    inf_graph[1][0] = 0.6
    inf_graph[1][3] = 0.4
    inf_graph[2][3] = 0.2
    inf_graph[3][2] = 0.2
    inf_graph[3][5] = 0.4
    inf_graph[2][4] = 0.6
    inf_graph[4][5] = 0.6
    inf_graph[5][0] = 1.0
    return inf_graph + np.identity(6)

class Default_Influence(Enum):
    CLIQUE = 0
    GROUP_2_DISCONECTED = 1
    GROUP_2_FAINT = 2
    INFLUENCERS_2_UNBALANCED = 3
    INFLUENCERS_2_BALANCED = 4
    CIRCULAR = 5
    RANDOM = 6

def build_influence(
        inf_type: Default_Influence,
        num_agents : int,
        weak_influence : np.float64 = GROUPS_FAINTLY_INF_VALUE_WEAK,
        strong_influence : np.float64 = GROUPS_FAINTLY_INF_VALUE_STRONG,
        general_influence : np.float64 = None,
        influencer_incoming_influence : np.float64 = None,
        influencer_outgoing_influence : np.float64 = None,
        influencer2_incoming_influence : np.float64 = INFLUENCERS_BALANCED_INCOMING_SECOND,
        influencer2_outgoing_influence : np.float64 = INFLUENCERS_BALANCED_OUTGOING_SECOND,
        minimum_influence : np.float64 = MIN_INF,
        diagonal_value : np.float64 = 0):
    """Builds the initial influence graph according to the `inf_type`.

    Helper function when iterating over the `Default_Influence` enum. The default values
    are the constants defined at the beginning of the polarization module.
    """
    if inf_type is Default_Influence.CLIQUE:
        if general_influence is None:
            general_influence = CLIQUE_INF_VALUE
        return build_inf_graph_clique(num_agents, general_influence, diagonal_value = diagonal_value)
    
    if inf_type is Default_Influence.GROUP_2_DISCONECTED:
        if general_influence is None:
            general_influence = GROUPS_DISCONNECTED_INF_VALUE
        return build_inf_graph_2_groups_disconnected(num_agents, general_influence, diagonal_value = diagonal_value)
    
    if inf_type is Default_Influence.GROUP_2_FAINT:
        return build_inf_graph_2_groups_faint(num_agents, weak_influence, strong_influence, diagonal_value = diagonal_value)
    
    if inf_type is Default_Influence.INFLUENCERS_2_UNBALANCED:
        if general_influence is None:
            general_influence = INFLUENCERS_UNBALANCED_OTHERS
        if influencer_incoming_influence is None:
            influencer_incoming_influence = INFLUENCERS_UNBALANCED_INCOMING_BOTH
        if influencer_outgoing_influence is None:
            influencer_outgoing_influence = INFLUENCERS_UNBALANCED_OUTGOING_BOTH
        return build_inf_graph_2_influencers_unbalanced(num_agents, influencer_incoming_influence, influencer_outgoing_influence, general_influence, diagonal_value = diagonal_value)

    ## Note that this influence graph is not really balanced by our definition of balanced
    if inf_type is Default_Influence.INFLUENCERS_2_BALANCED:
        if general_influence is None:
            general_influence = INFLUENCERS_BALANCED_OTHERS
        if influencer_incoming_influence is None:
            influencer_incoming_influence = INFLUENCERS_BALANCED_INCOMING_FIRST
        if influencer2_incoming_influence is None:
            influencer2_incoming_influence = INFLUENCERS_BALANCED_INCOMING_SECOND
        if influencer_outgoing_influence is None:
            influencer_outgoing_influence = INFLUENCERS_BALANCED_OUTGOING_FIRST
        if influencer2_outgoing_influence is None:
            influencer2_outgoing_influence = INFLUENCERS_BALANCED_OUTGOING_SECOND
        return build_inf_graph_2_influencers_balanced(num_agents, influencer_outgoing_influence, influencer2_outgoing_influence, influencer_incoming_influence, influencer2_incoming_influence, general_influence, diagonal_value = diagonal_value)
    
    if inf_type is Default_Influence.CIRCULAR:
        if general_influence is None:
            general_influence = CIRCULAR_INF_VALUE
        return build_inf_graph_circular(num_agents, general_influence, diagonal_value = diagonal_value) 
    
    if inf_type is Default_Influence.RANDOM:
        return build_inf_graph_random(
            num_agents,
            diagonal_value = diagonal_value,
            minimum_influence = minimum_influence
            )
    
    raise NotImplementedError('inf_type not recognized. Expected an `Default_Influence`')
