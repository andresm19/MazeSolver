
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
        if self.empty():
            self.head = node
        else: 
            self.tail.next = node
        self.tail = node 
    
    def dequeue(self):
        if self.empty(): return
        e = self.head
        if self.tail == self.head:
            self.tail = None
            self.head = None
            return e
        self.head = self.head.next
        return e
    
    def show(self):
        act = self.head
        while act != None:
            print(act.data, end=' ')
            act = act.next
        print()


class PriorityQueue():
    def __init__(self):
        self.max_size = 200
        self.size = 0
        self.array = [None] * self.max_size
    
    def parent(self, i):
        return int(i/2)
    
    def left_child(self, i):
        return i*2 + 1

    def right_child(self, i):
        return i*2 + 2

    def sift_up(self, i):
        while i > 0 and self.array[self.parent(i)][1] <= self.array[i][1]:
            aux = self.array[self.parent(i)]
            self.array[self.parent(i)] = self.array[i]
            self.array[i] = aux
            i = self.parent(i)
    
    def sift_down(self, i):
        max_ind = i
        
        l = self.left_child(i)
        if l < self.size:
            if self.array[l][1] > self.array[max_ind][1]:
                max_ind = l
        
        r = self.right_child(i)
        if r < self.size:
            if self.array[r][1] > self.array[max_ind][1]:
                max_ind = r

        if i != max_ind:
            aux = self.array[i]
            self.array[i] = self.array[max_ind]
            self.array[max_ind] = aux
            self.sift_down(max_ind)

    def insert(self, n):
        if self.size == self.max_size:
            print("ERROR!!!")
            return "Error"

        self.array[self.size] = n
        self.sift_up(self.size)
        self.size += 1

    def extract_max(self):
        n = self.array[0]
        self.array[0] = self.array[self.size-1]
        self.array[self.size-1] = None
        self.size -= 1

        if self.size > 0:
            self.sift_down(0)

        return n

    def extract_min(self):
        n = self.array[self.size-1]
        self.array[self.size-1] = None
        self.size -= 1

        return n

    def get_max(self):
        return self.array[0]




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
    
                
    # Left
    if point[0] - 1 >= 0:
        if map_data[point[0] - 1][point[1]] == 'c':
            if mode == 'bfs':
                list_av[3] = (point[0] - 1, point[1])
            else:
                list_av.append((point[0] - 1, point[1]))
    
                
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
    
    

    return list_av


def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
