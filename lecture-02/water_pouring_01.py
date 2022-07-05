import math


def path_successor(mapping):
    def _wrap(state):
        return {node: '=>' for node in mapping[state]}
    return _wrap


def path_goal(goal):
    def _wrap(path):
        return goal in path
    return _wrap


def w_successor(A, B):
    def _successor(state):
        a, b = state

        return {
            (0, b): '清空a',
            (a, 0): '清空b',
            (A, b): '灌满a',
            (a, B): '灌满b',
            (0, a + b) if a + b <= B else (a + b - B, B): 'a => b',
            (a + b, 0) if a + b <= A else (A, a + b - A): 'b => a'
        }

    return _successor


def reach_capacity(goal):
    def _wrap(path):
        return goal in path[-1]
    return _wrap



def search(start, goal_f, successor_f, sort_f=lambda a: a):
    explored = set()
    paths = [ [start] ]

    while paths:
        # path = paths.pop(-1)
        # if we expand latest: Depth First Search 深度优先遍历
        path = paths.pop(0)
        # if we expand oldest: Breadth First Search 广度优先遍历

        if goal_f(path): return path

        frontier = path[-1]

        if frontier in explored: continue

        for (state, action) in successor_f(frontier).items():
            if state in explored: continue

            new_path = path + [action, state]

            paths.append(new_path)

        paths = sorted(paths, key=sort_f)

        explored.add(frontier)

    return []


if __name__ == '__main__':

    from collections import defaultdict
    import pickle

    # map = {
    #     "全聚德": "重庆小面 湖南米粉 龙抄手".split(),
    #     "重庆小面": "龙抄手 便宜坊".split(),
    #     "便宜坊": "牛排 重庆小面".split(),
    #     "港式火锅": "云水谣 龙抄手".split(),
    #     "海底捞": "港式火锅".split(),
    # }
    #
    # bimapping = defaultdict(set)
    #
    # for rest, links in map.items():
    #     bimapping[rest] |= set(links)
    #
    #     for link in links:
    #         bimapping[link] |= {rest}
    #
    # print(bimapping)
    #
    # result = search(start='全聚德', goal_f=path_goal('海底捞'), successor_f=path_successor(bimapping))
    #
    # print(result)
    #
    # solutions = search(start=(0, 0), goal_f=reach_capacity(70),
    #                    successor_f=w_successor(90, 40), sort_f=lambda p: len(p))
    #
    # for s in solutions:
    #     print(s)
    #

    with open('line_with_station.pkl', 'rb') as f:
        stations = pickle.load(f)

    print(stations)

    def sub_goal(goal):
        def _wrap(path):
            return path[-1] == goal
        return _wrap

    def sub_successors(stations_map):
        def _wrap(station):
            next_station = {}
            for line_num, stations in stations_map.items():
                if station in stations:
                    index = stations.index(station)

                    left_index, right_index = index - 1, index + 1

                    if left_index >= 0:
                        next_station[stations[left_index]] = line_num + "=>"
                    if right_index < len(stations):
                        next_station[stations[right_index]] = line_num + "<="

            return next_station

        return _wrap


    print(sub_successors(stations)('崇文门'))

    solution = search(start='清华东路西口', goal_f=sub_goal('传媒大学'),
                 successor_f=sub_successors(stations), sort_f=lambda p: len(p))

    for s in solution:
        print(s)
