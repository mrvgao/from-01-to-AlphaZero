from icecream import ic

from collections import defaultdict
from functools import reduce

kown_links = [
    ('A', 'S1'),
    ('A', 'S2'),
    ('A', 'S3'),
    ('S1', 'S4'),
    ('S2', 'S4'),
    ('S3', 'S5'),
    ('S4', 'S6'),
    ('S5', 'S7'),
    ('S6', 'S8'),
    ('S6', 'S9'),
    ('S7', 'S10'),
    ('S9', 'S10'),
    ('S8', 'S11'),
    ('S10', 'P'),
    ('S11', 'P'),
]

precedure = defaultdict(list) # Graph

for link in kown_links:
    start, end = link   
    precedure[start].append(end)



while precedure:
    all_nodes_have_outputs = set(precedure.keys())
    all_nodes_have_inputs = set(reduce(lambda x, y: x + y, list(precedure.values())))

    
    node_only_output_no_input = all_nodes_have_outputs - all_nodes_have_inputs

    for node in node_only_output_no_input:
        print('node: {}, only output, no input'.format(node))
        for link in precedure[node]:
            print('Get link: {} --> {}'.format(node, link))

        del precedure[node]


# How to represent
# Topological Sorting: Neural Netowrk Framework, auto-grad








