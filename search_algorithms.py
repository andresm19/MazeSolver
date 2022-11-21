
import os, csv
import csv, DFS, BFS, ITERATIVE, UCS, GREEDY
from searching import *

coor_list = []

# Todas las funciones para buscar el camino correcto
def create_txt_instructions():
    pass

def dfs_search(map_data, start, end):
    DFS.DFS(map_data, start, end)

def bfs_search(map_data, start, end):
    BFS.BFS(map_data, start, end)

def iter_deep_search(map_data, start, end, depth):
    ITERATIVE.instructions = []
    ITERATIVE.coor_list = []
    ITERATIVE.found = False
    ITERATIVE.stack = Stack()
    ITERATIVE.ITERATIVE(map_data, start, end, depth)

def uniform_cost_search(map_data, start, end):
    UCS.instructions = []
    UCS.coor_list = []
    UCS.pq = UCS.PriorityQueue()
    UCS.UCS(map_data, start, end)

def greedy_search(map_data, start, end):
    GREEDY.found = False
    GREEDY.instructions = []
    GREEDY.coor_list = []
    GREEDY.stack = Stack()
    GREEDY.GREEDY(map_data, start, end)

def a_star_search():
    """
    Procedimiento
    """
    create_txt_instructions()


# Funcion para leer el archivo csv
def read_csv(file_name):
    map_data = []
    with open(os.path.join(os.path.dirname(__file__), file_name), 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    map_data.append(row)
    return map_data

def solve(file_name, mode, depth=0):
    map_data = read_csv(file_name)
    NUMBER_TILES = len(map_data)
    start = (0, map_data[0].index("c"))
    end = (NUMBER_TILES-1, map_data[NUMBER_TILES-1].index("c"))
    global coor_list

    if mode == 'iter':
        iter_deep_search(map_data[:], start, end, depth)

        coor_list = ITERATIVE.coor_list[1:]      
        ITERATIVE.update_instructions()
        
        return [t[::-1] for t in coor_list], ITERATIVE.instructions
    
    elif mode == 'dfs':
        DFS.instructions = []
        DFS.coor_list = []
        DFS.stack = Stack()
        DFS.found = False
        dfs_search(map_data[:], start, end)
        coor_list = DFS.coor_list[1:]
            
        DFS.update_instructions()

        return [t[::-1] for t in coor_list], DFS.instructions
    
    elif mode == 'bfs':
        BFS.instructions = []
        BFS.coor_list = []
        BFS.queue = Queue()
        BFS.found = False
        BFS.n_buscados = []
        
        bfs_search(map_data[:], start, end)
        coor_list = BFS.coor_list[1:]

        coor_list2 = []
        for coor in BFS.coor_list:
            if coor != (0,0):
                coor_list2.append(coor)

        map_data = read_csv(file_name)
        BFS.update_instructions(map_data[:])

        return [t[::-1] for t in coor_list2[1:]], BFS.instructions

    elif mode == 'ucs':
        uniform_cost_search(map_data[:], start, end)
        coor_list = UCS.coor_list[1:]

        map_data = read_csv(file_name)
        UCS.update_instructions(map_data[:])

        return [t[::-1] for t in coor_list[1:]], UCS.instructions

    else:
        greedy_search(map_data[:], start, end)
        coor_list = GREEDY.coor_list

        GREEDY.update_instructions()

        return [t[::-1] for t in coor_list[1:]], GREEDY.instructions




