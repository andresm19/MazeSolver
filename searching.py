
class Node():
    def __init__(self, coor):
        self.next = None
        self.data = coor

class Stack():
    def __init__(self):
        self.head = None

    def push(self, node):
        node.next = self.head
        self.head = node

    def pop(self):
        e = None
        if self.head != None:
            e = self.head
            self.head = self.head.next
        return e
    
    def show(self):
        print("-------")
        act = self.head
        while act != None:
            print(act.data)
            act = act.next
        print("-------------------------")


class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def empty(self):
        return self.tail == None

    def enqueue(self, node):
        if self.empty(): self.head = node
        else: self.tail.next = node
        self.tail = node 
    
    def dequeue(self):
        if self.empty(): return
        if self.tail == self.head:
            self.tail = None
        e = self.head
        self.head = self.head.next
        return e
    
    def show(self):
        act = self.head
        while act != None:
            print(act.data, end=' ')
            act = act.next
        print()

def availables(point, map_data, mode='dfs'):
    
    n_tiles = len(map_data)
    list_av = []

    if mode == 'bfs':
        list_av = [(0,0), (0,0), (0,0), (0,0)]
        if point == (0,0):
            return list_av

    # Down
    if point[1] + 1 < n_tiles:
        if map_data[point[0]][point[1] + 1] == 'c':
            if mode == 'bfs':
                list_av[0] = (point[0], point[1] + 1)
            else:
                list_av.append((point[0], point[1] + 1))
    
    # Right
    if point[0] + 1 < n_tiles:
        if map_data[point[0] + 1][point[1]] == 'c':
            if mode == 'bfs':
                list_av[1] = (point[0] + 1, point[1])
            else:
                list_av.append((point[0] + 1, point[1]))
    
    # Up
    if point[1] - 1 >= 0:
        if map_data[point[0]][point[1] - 1] == 'c':
            if mode == 'bfs':
                list_av[2] = (point[0], point[1] - 1)
            else:
                list_av.append((point[0], point[1] - 1))
    
    # Left
    if point[0] - 1 >= 0:
        if map_data[point[0] - 1][point[1]] == 'c':
            if mode == 'bfs':
                list_av[3] = (point[0] - 1, point[1])
            else:
                list_av.append((point[0] - 1, point[1]))

    return list_av
