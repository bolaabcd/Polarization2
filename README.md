# Evolution of belief simulator

This repository implements update functions for the (extension of) multi-agent model introduced [here](https://link.springer.com/chapter/10.1007/978-3-030-78089-0_2).

The main focus of this repository is to test the update functions and their effects on the evolution of agents beliefs.

## About the model
In the model we implement, society is represented as a directed weighted graph: people are represented as nodes and influence is represented by edges. We deal with some true-or-false proposition **p** ("the earth is not flat" for instance), and each node has an associeted value between *0* and *1*: the closest to *1*, the more the agent believes **p** is true. Each directed edge has a weight between *0* and *1* that represents how strongly one agent influences the other. How exactly each agent influences and is influenced is represented by the **update-function**, a function that recieves as input the current state of the society graph and returns it's next state (our model considers discrete time steps and syncrhonous influence, all influences are applied at once).

All update-functions we test have the same general format:


$$B_i^{t+1} = B_i^t + \Sigma_{i\in A_i} (\frac{I_{j,i}}{\Sigma_{k\in A_i} I_{k,i}} f_{j,i}(B_j^t-B_i^t))$$

Where:

- $B_i^t$ is the beleif value of agent $i$ at time step $t$.
- $I_{j,i}$ is how much agent $i$ influences agent $j$ (a value between 0 and 1).
- $A_i$ is the set of all agents that exerce some influence on agent $i$ (all $j$ such that $I_{j,i} > 0$).
- $f_{j,i}$ is the function that captures the cognitive biases we want to consider, when agent j tries to influence agent i. We consider biases that depend on the disagreement level (B_j-B_i) only.

# Modules and scripts (these descriptions might not be updated)

## belief_update_fs.py
This module determine the possible $f$ parts of the functions we test.

## default_beliefs.py
This module is used to build some useful initial belief configurations.

## default_fs.py
This module is used to build default distribution of $f$ functions among agents (distinct agents are allowed to have distinct $f$'s).

## default_influences.py
This module has implementations for some default influence configurations as adjacency matrixes.

## default_tolerances.py
This module has implementations for some basic tolerance distributions on society.

## society_graph.py
This module implements the society graph class, which implements all elements of the model with an networkx DiGraph.

## example_cases.py
This module implements some example of tests and a `simulate` function that runs test cases with changing parameters.

## run_base_tests.py
This script runs many simulations with changing parameters, to check what happens in each case.

## paper.py and paper2.py

Examples of the paper (probably not all will make it to the paper).
