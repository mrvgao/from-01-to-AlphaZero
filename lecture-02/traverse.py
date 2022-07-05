from icecream import ic
import networkx as nx
import matplotlib.pyplot as plt
from copy import copy
import os
from collections import defaultdict


class LandMark:
    def __init__(self, name, position=None, monster=None, treasure=None):
        self.name = name
        self.position = position
        self.monster = name
        self.treasure = treasure

    def show(self):
        print('I am {}, I locate in {}, I have monste: {}, I have treasure: {}'.format(self.name, self.position, self.monster, self.treasure))

    def __repr__(self):
        return self.name


initial = LandMark('初始祭坛', (0, 20), 'None', 500)
valley = LandMark('神秘谷底', (100, 20), 'Great', 100)
island = LandMark('金银岛', (150, 150), 'Normal', 1000)
mountain = LandMark('高山', (300, 300), 'Normal', 50)
river = LandMark('河流', (350, 20), 'Good', 200)
canvey = LandMark('大峡谷', (400, 500), 'Great', 200)
ending = LandMark('终结之底', (600, 20), 'Hugu', 2000)

mapping = {
    initial: [valley, island],
    valley: [initial, mountain, river],
    mountain: [river, valley, canvey],
    island: [initial, mountain],
    river: [canvey, island],
    canvey: [ending]
}

#ic(mapping)

people_relation = {
    'CEO': "VP1 VP2 VP3".split(),
    "VP1": "D1 D2 D3".split(),
    "VP2": "D4 D5".split(),
    "VP3": "D6".split(),
    "D1": "M1 M2".split(),
    "D2": "M3".split(),
    "D3": "M4 M5".split(),
    "D4": "M6 M7".split(),
    "D5": "M8 M9".split(),
    "D6": "M10 M11 M12".split(),
    "M1": "W1 W2 W3".split(),
    "M2": "W4 W5 W6".split(),
    "M3": "W7 W8 W9".split(),
}

#def traverse(graph, start, end, get_froniter_fn):
def search(graph, start, end):
    known = [ [start] ]

    visited = set()


    while graph: # graph trverse algorithm
        #froniter = known.pop(-1)
        #path = get_froniter_fn(known)
        path = known.pop(0)

        froniter = path[-1]

        if froniter in visited or froniter not in graph: continue

        links = graph[froniter]

        print('{} ==> {}'.format(froniter, links))

        for link in links:
            if link == end: return path + [link]

            known.append(path+[link])

        visited.add(froniter)

        del graph[froniter]

        known = sorted(known, key=lambda p: len(p))

    return visited


def depth_first_traverse(*args):
    return traverse(*args, lambda k: k.pop(0))


def breadth_first_traverse(*args):
    return traverse(*args, lambda k: k.pop(-1))


'''
path = search(copy(mapping), initial, ending)

print('🚶=> '.join(list(map(lambda x: x.name, path))))

# 深度优先遍历和广度优先遍历
# start, end ==> Path Search

people_path = search(copy(people_relation), 'CEO', 'W6')

print('👀=> '.join(people_path))
'''

dir_name = 'subways'
files =  list(os.walk(dir_name))[-1][-1]

stations = defaultdict(set)

for f in files:
    line_stations = []

    for i, line in enumerate(open(os.path.join(dir_name, f))):
        if i == 0: continue
    
        if not line.strip(): continue

        print(line.strip())

        line_stations.append(line.strip())
    
    for i, s in enumerate(line_stations[:-1]):
        _next = line_stations[i+1]
        stations[s].add(_next)
        stations[_next].add(s)

        
ic(stations)

path = search(copy(stations), start='天安门西', end='雍和宫')
print('==>'.join(path))

path = search(copy(stations), start='天安门西', end='东单')
print('==>'.join(path))

path = search(copy(stations), start='天安门西', end='五棵松')
print('==>'.join(path))
