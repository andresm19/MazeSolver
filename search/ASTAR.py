
from search.searching import *

costs = [1, 1, 1, 1]    # En orden los costos de moverse [DOWN, RIGHT, UP, LEFT]

coor_list = []
instructions = []
open = PriorityQueue()
close = []
found = False
current = None

class Node2():
    def __init__(self, point, pred):
        self.data = point
        self.pred = pred
        self.h = 0
        self.g = 0
        self.f = 0


def ASTAR(map_data, start, end):
    
    global coor_list, instructions, open, close, found, current

    n = Node2(start, None)

    n.h = distance(start, end)
    n.g = 0
    n.f = n.h

    current = n

    open.insert([current, distance(current.data, end)])

    while found == False:
        if open.get_max() != None:    
            current = open.extract_min()[0]
            close.append(current)
            coor_list.append(current.data)

            for av in availables(current.data, map_data):
                if av not in [node.data for node in close]:
                    if av in [node[0].data for node in open.array[0:open.size]]:
                        for node in open.array[0:open.size]:
                            print(open.array[0:open.size], node[0].data, av)
                            if node[0].data == av:
                                node_av = node[0]

                        if current.g + cost(current.data, av, map_data) < node_av.g:
                            node_av.g = current.g + cost(current.data, av, map_data)
                            node_av.f = node_av.g + node_av.h

                    else:                              
                        node_av = Node2(av, current)
                        node_av.g = current.g + cost(current.data, av, map_data)
                        node_av.h = distance(av, end)
                        node_av.f = node_av.g + node_av.h
                        open.insert([node_av, node_av.f])

                        if node_av.data == end:
                            coor_list.append(av)
                            found = True
                            close.append(node_av)


def update_instructions():
    global close, instructions

    c = close[-1]
    while c.pred != None:
        if c.data == (c.pred.data[0] + 1, c.pred.data[1]):
            instructions.append("D")
        elif c.data == (c.pred.data[0] - 1, c.pred.data[1]):
            instructions.append("U")
        elif c.data == (c.pred.data[0], c.pred.data[1] - 1):
            instructions.append("L")
        elif c.data == (c.pred.data[0], c.pred.data[1] + 1):
            instructions.append("R")

        c = c.pred
    
    instructions.reverse()

def cost(p1, p2, map_data):
    # Costo por dirigirse desde p1 hasta p2
    
    global costs

    avs = availables(p1, map_data, mode='bfs')

    cost = costs[avs.index(p2)]

    return cost