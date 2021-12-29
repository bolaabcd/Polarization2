from base_tests import *
simple_tripartite_param_list = []
print(0)
tolerance_0 = []
for i in range(100):
    gr = simple_tripartite(
        33,
        belief_update_fs.quadratic_update,
        0,
        0.5,
        1,
        2*i/99-1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )
    tolerance_0.append(gr)
simple_tripartite_param_list.append((tolerance_0,"tolerance_0"))
out_influence_0 = []
for i in range(100):
    gr = simple_tripartite(
        33,
        belief_update_fs.quadratic_update,
        0,
        0.5,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        i/99,
        1,
        1,
        1,
    )
    out_influence_0.append(gr)
simple_tripartite_param_list.append((out_influence_0,"out_influence_0"))
in_influence_0 = []
for i in range(100):
    gr = simple_tripartite(
        33,
        belief_update_fs.quadratic_update,
        0,
        0.5,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        i/99,
        1,
        1,
    )
    in_influence_0.append(gr)
simple_tripartite_param_list.append((in_influence_0,"in_influence_0"))
simulate((simple_tripartite_param_list,"simple_tripartite"))
del simple_tripartite_param_list


simple_clique_uniform_param_list = []
print(1)
tolerance_value = []
for i in range(100):
    gr = simple_clique_uniform(
        33,
        belief_update_fs.quadratic_update,
        0,
        1,
        2*i/99-1,
        1
    )
    tolerance_value.append(gr)
simple_clique_uniform_param_list.append((tolerance_value,"tolerance_value"))

simulate((simple_clique_uniform_param_list,"simple_clique_uniform"))
del simple_clique_uniform_param_list




clique_tripartite_param_list = []
print(2)
tolerance_middle = []
for i in range(100):
    gr = clique_tripartite(
        False,
        33,
        belief_update_fs.quadratic_update,
        0,
        0.2,
        0.4,
        0.6,
        0.8,
        1,
        1,
        2*i/99-1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )
    tolerance_middle.append(gr)
clique_tripartite_param_list.append((tolerance_middle,"tolerance_middle"))
tolerance_0 = []
for i in range(100):
    gr = clique_tripartite(
        False,
        33,
        belief_update_fs.quadratic_update,
        0,
        0.2,
        0.4,
        0.6,
        0.8,
        1,
        2*i/99-1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )
    tolerance_0.append(gr)
clique_tripartite_param_list.append((tolerance_0,"tolerance_0"))
influence_0 = []
for i in range(100):
    gr = clique_tripartite(
        False,
        33,
        belief_update_fs.quadratic_update,
        0,
        0.2,
        0.4,
        0.6,
        0.8,
        1,
        1,
        1,
        1,
        i/99,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )
    influence_0.append(gr)
clique_tripartite_param_list.append((influence_0,"influence_0"))
influence_middle = []
for i in range(100):
    gr = clique_tripartite(
        False,
        33,
        belief_update_fs.quadratic_update,
        0,
        0.2,
        0.4,
        0.6,
        0.8,
        1,
        1,
        1,
        1,
        1,
        i/99,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )
    influence_middle.append(gr)
clique_tripartite_param_list.append((influence_middle,"influence_middle"))
interaction_0 = []
for i in range(100):
    gr = clique_tripartite(
        False,
        33,
        belief_update_fs.quadratic_update,
        0,
        0.2,
        0.4,
        0.6,
        0.8,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        i/99,
        i/99,
        1,
        1,
        i/99,
        i/99,
    )
    interaction_0.append(gr)
clique_tripartite_param_list.append((interaction_0,"interaction_0"))
interaction_middle = []
for i in range(100):
    gr = clique_tripartite(
        False,
        33,
        belief_update_fs.quadratic_update,
        0,
        0.2,
        0.4,
        0.6,
        0.8,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        i/99,
        i/99,
        i/99,
        i/99,
        1,
        1,
    )
    interaction_middle.append(gr)
clique_tripartite_param_list.append((interaction_middle,"interaction_middle"))

simulate((clique_tripartite_param_list,"clique_tripartite"))
del clique_tripartite_param_list

clique_two_constant_influencers_uniform_param_list = []
print(3)
tolerance_middle = []
for i in range(100):
    gr = clique_two_influencers_uniform(
        31,
        belief_update_fs.quadratic_update,
        0,
        1,
        2*i/99-1,
        1,
        0,
        1,
        1,
        1,
        0.1,
        0.1,
        1,
        1,
        True
    )
    tolerance_middle.append(gr)
clique_two_constant_influencers_uniform_param_list.append((tolerance_middle,"tolerance_middle"))
influence_middle = []
for i in range(100):
    gr = clique_two_influencers_uniform(
        31,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        i/99,
        0,
        1,
        1,
        1,
        0.1,
        0.1,
        1,
        1,
        True
    )
    influence_middle.append(gr)
clique_two_constant_influencers_uniform_param_list.append((influence_middle,"influence_middle"))
influence_0 = []
for i in range(100):
    gr = clique_two_influencers_uniform(
        31,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0.1,
        0.1,
        i/99,
        1,
        True
    )
    influence_0.append(gr)
clique_two_constant_influencers_uniform_param_list.append((influence_0,"influence_0"))

simulate((clique_two_constant_influencers_uniform_param_list,"clique_two_constant_influencers_uniform"))
del clique_two_constant_influencers_uniform_param_list




clique_two_nonconstant_influencers_uniform_param_list = []
print(4)
tolerance_middle = []
for i in range(100):
    gr = clique_two_influencers_uniform(
        31,
        belief_update_fs.quadratic_update,
        0,
        1,
        2*i/99-1,
        1,
        0,
        1,
        1,
        1,
        0.1,
        0.1,
        1,
        1,
        False
    )
    tolerance_middle.append(gr)
clique_two_nonconstant_influencers_uniform_param_list.append((tolerance_middle,"tolerance_middle"))
influence_middle = []
for i in range(100):
    gr = clique_two_influencers_uniform(
        31,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        i/99,
        0,
        1,
        1,
        1,
        0.1,
        0.1,
        1,
        1,
        False
    )
    influence_middle.append(gr)
clique_two_nonconstant_influencers_uniform_param_list.append((influence_middle,"influence_middle"))
influence_0 = []
for i in range(100):
    gr = clique_two_influencers_uniform(
        31,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0.1,
        0.1,
        i/99,
        1,
        False
    )
    influence_0.append(gr)
clique_two_nonconstant_influencers_uniform_param_list.append((influence_0,"influence_0"))
influence_0 = []
for i in range(100):
    gr = clique_two_influencers_uniform(
        31,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0.1,
        0.1,
        i/99,
        1,
        False
    )
    influence_0.append(gr)
clique_two_nonconstant_influencers_uniform_param_list.append((influence_0,"influence_0"))
tolerance_0 = []
for i in range(100):
    gr = clique_two_influencers_uniform(
        31,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        1,
        0,
        1,
        2*i/99-1,
        1,
        0.1,
        0.1,
        1,
        1,
        False
    )
    tolerance_0.append(gr)
clique_two_nonconstant_influencers_uniform_param_list.append((tolerance_0,"tolerance_0"))
weak_inf_0 = []
for i in range(100):
    gr = clique_two_influencers_uniform(
        31,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        i/99,
        0.1,
        1,
        1,
        False
    )
    weak_inf_0.append(gr)
clique_two_nonconstant_influencers_uniform_param_list.append((weak_inf_0,"weak_inf_0"))


simulate((clique_two_nonconstant_influencers_uniform_param_list,"clique_two_nonconstant_influencers_uniform"))
del clique_two_nonconstant_influencers_uniform_param_list




clique_one_constant_influencer_uniform_param_list = []
print(5)
tolerance_middle = []
for i in range(100):
    gr = clique_one_influencer_uniform(
        32,
        belief_update_fs.quadratic_update,
        0,
        1,
        2*i/99-1,
        1,
        0,
        1,
        0.1,
        1,
        True
    )
    tolerance_middle.append(gr)
clique_one_constant_influencer_uniform_param_list.append((tolerance_middle,"tolerance_middle"))
influence_middle = []
for i in range(100):
    gr = clique_one_influencer_uniform(
        32,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        i/99,
        0,
        1,
        0.1,
        1,
        True
    )
    influence_middle.append(gr)
clique_one_constant_influencer_uniform_param_list.append((influence_middle,"influence_middle"))
influence_0 = []
for i in range(100):
    gr = clique_one_influencer_uniform(
        32,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        1,
        0,
        1,
        0.1,
        i/99,
        True
    )
    influence_0.append(gr)
clique_one_constant_influencer_uniform_param_list.append((influence_0,"influence_0"))

simulate((clique_one_constant_influencer_uniform_param_list,"clique_one_constant_influencer_uniform"))
del clique_one_constant_influencer_uniform_param_list




clique_one_nonconstant_influencer_uniform_param_list = []
print(6)
tolerance_middle = []
for i in range(100):
    gr = clique_one_influencer_uniform(
        32,
        belief_update_fs.quadratic_update,
        0,
        1,
        2*i/99-1,
        1,
        0,
        1,
        0.1,
        1,
        False
    )
    tolerance_middle.append(gr)
clique_one_nonconstant_influencer_uniform_param_list.append((tolerance_middle,"tolerance_middle"))
influence_middle = []
for i in range(100):
    gr = clique_one_influencer_uniform(
        32,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        i/99,
        0,
        1,
        0.1,
        1,
        False
    )
    influence_middle.append(gr)
clique_one_nonconstant_influencer_uniform_param_list.append((influence_middle,"influence_middle"))
influence_0 = []
for i in range(100):
    gr = clique_one_influencer_uniform(
        32,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        1,
        0,
        1,
        0.1,
        i/99,
        False
    )
    influence_0.append(gr)
clique_one_nonconstant_influencer_uniform_param_list.append((influence_0,"influence_0"))
tolerance_0 = []
for i in range(100):
    gr = clique_one_influencer_uniform(
        32,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        1,
        0,
        2*i/99-1,
        0.1,
        1,
        False
    )
    tolerance_0.append(gr)
clique_one_nonconstant_influencer_uniform_param_list.append((tolerance_0,"tolerance_0"))
weak_inf_0 = []
for i in range(100):
    gr = clique_one_influencer_uniform(
        32,
        belief_update_fs.quadratic_update,
        0,
        1,
        1,
        1,
        0,
        1,
        i/99,
        1,
        False
    )
    weak_inf_0.append(gr)
clique_one_nonconstant_influencer_uniform_param_list.append((weak_inf_0,"weak_inf_0"))

simulate((clique_one_nonconstant_influencer_uniform_param_list,"clique_one_nonconstant_influencer_uniform"))
del clique_one_nonconstant_influencer_uniform_param_list


tripartite_one_constant_influencer_param_list = []
print(7)
influence_0 = []
for i in range(100):
    gr = tripartite_one_influencer(
        i/99,
        1,
        0,
        1,
        1,
        1,
        belief_update_fs.quadratic_update,
        33,
        True,
        0.1
    )
    influence_0.append(gr)
tripartite_one_constant_influencer_param_list.append((influence_0,"influence_0"))
tolerance_middle = []
for i in range(100):
    gr = tripartite_one_influencer(
        1,
        1,
        0,
        1,
        1,
        2*i/99-1,
        belief_update_fs.quadratic_update,
        33,
        True,
        0.1
    )
    tolerance_middle.append(gr)
tripartite_one_constant_influencer_param_list.append((tolerance_middle,"tolerance_middle"))

simulate((tripartite_one_constant_influencer_param_list,"tripartite_one_constant_influencer"))
del tripartite_one_constant_influencer_param_list




tripartite_one_nonconstant_influencer_param_list = []
print(8)
influence_0 = []
for i in range(100):
    gr = tripartite_one_influencer(
        i/99,
        1,
        0,
        1,
        1,
        1,
        belief_update_fs.quadratic_update,
        33,
        False,
        0.1
    )
    influence_0.append(gr)
tripartite_one_nonconstant_influencer_param_list.append((influence_0,"influence_0"))
tolerance_middle = []
for i in range(100):
    gr = tripartite_one_influencer(
        1,
        1,
        0,
        1,
        1,
        2*i/99-1,
        belief_update_fs.quadratic_update,
        33,
        False,
        0.1
    )
    tolerance_middle.append(gr)
tripartite_one_nonconstant_influencer_param_list.append((tolerance_middle,"tolerance_middle"))
tolerance_0 = []
for i in range(100):
    gr = tripartite_one_influencer(
        1,
        1,
        0,
        1,
        2*i/99-1,
        1,
        belief_update_fs.quadratic_update,
        33,
        False,
        0.1
    )
    tolerance_0.append(gr)
tripartite_one_nonconstant_influencer_param_list.append((tolerance_0,"tolerance_0"))
weak_inf_0 = []
for i in range(100):
    gr = tripartite_one_influencer(
        1,
        1,
        0,
        1,
        1,
        1,
        belief_update_fs.quadratic_update,
        33,
        False,
        i/99
    )
    weak_inf_0.append(gr)
tripartite_one_nonconstant_influencer_param_list.append((weak_inf_0,"weak_inf_0"))

simulate((tripartite_one_nonconstant_influencer_param_list,"tripartite_one_nonconstant_influencer"))
del tripartite_one_nonconstant_influencer_param_list




tripartite_two_constant_influencers_param_list = []
print(9)
influence_0 = []
for i in range(100):
    gr = tripartite_two_influencers(
        i/99,
        1,
        1,
        0,
        1,
        1,
        1,
        1,
        belief_update_fs.quadratic_update,
        33,
        True,
        1,
        1
    )
    influence_0.append(gr)
tripartite_two_constant_influencers_param_list.append((influence_0,"influence_0"))
tolerance_middle = []
for i in range(100):
    gr = tripartite_two_influencers(
        1,
        1,
        1,
        0,
        1,
        1,
        2*i/99-1,
        1,
        belief_update_fs.quadratic_update,
        33,
        True,
        1,
        1
    )
    tolerance_middle.append(gr)
tripartite_two_constant_influencers_param_list.append((tolerance_middle,"tolerance_middle"))

simulate((tripartite_two_constant_influencers_param_list,"tripartite_two_constant_influencers"))
del tripartite_two_constant_influencers_param_list




tripartite_two_nonconstant_influencers_param_list = []
print(10)
influence_0 = []
for i in range(100):
    gr = tripartite_two_influencers(
        i/99,
        1,
        1,
        0,
        1,
        1,
        1,
        1,
        belief_update_fs.quadratic_update,
        33,
        False,
        0.1,
        0.1
    )
    influence_0.append(gr)
tripartite_two_nonconstant_influencers_param_list.append((influence_0,"influence_0"))
tolerance_middle = []
for i in range(100):
    gr = tripartite_two_influencers(
        1,
        1,
        1,
        0,
        1,
        1,
        2*i/99-1,
        1,
        belief_update_fs.quadratic_update,
        33,
        False,
        0.1,
        0.1
    )
    tolerance_middle.append(gr)
tripartite_two_nonconstant_influencers_param_list.append((tolerance_middle,"tolerance_middle"))
tolerance_0 = []
for i in range(100):
    gr = tripartite_two_influencers(
        1,
        1,
        1,
        0,
        1,
        2*i/99-1,
        1,
        1,
        belief_update_fs.quadratic_update,
        33,
        False,
        0.1,
        0.1
    )
    tolerance_0.append(gr)
tripartite_two_nonconstant_influencers_param_list.append((tolerance_0,"tolerance_0"))
weak_inf_0 = []
for i in range(100):
    gr = tripartite_two_influencers(
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        1,
        belief_update_fs.quadratic_update,
        33,
        False,
        i/99,
        0.1
    )
    weak_inf_0.append(gr)
tripartite_two_nonconstant_influencers_param_list.append((weak_inf_0,"weak_inf_0"))

simulate((tripartite_two_nonconstant_influencers_param_list,"tripartite_two_nonconstant_influencers"))
del tripartite_two_nonconstant_influencers_param_list
print(11)