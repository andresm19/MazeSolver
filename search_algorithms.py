
import os
import csv
import DFS
import BFS
from searching import *

coor_list = []

# Todas las funciones para buscar el camino correcto
def create_txt_instructions():
    pass

def dfs_search(map_data, start, end):
    DFS.DFS(map_data, start, end)
    #print(DFS.coor_list)

def bfs_search(map_data, start, end):
    BFS.BFS(map_data, start, end)

def iter_deep_search():
    """
    Procedimiento
    """
    create_txt_instructions()

def uniform_cost_search():
    """
    Procedimiento
    """
    create_txt_instructions()

def greedy_search():
    """
    Procedimiento
    """
    create_txt_instructions()

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

def solve(file_name, mode):
    map_data = read_csv(file_name)
    NUMBER_TILES = len(map_data)
    start = (0, map_data[0].index("c"))
    end = (NUMBER_TILES-1, map_data[NUMBER_TILES-1].index("c"))
    global coor_list

    if mode == 'dfs':
        dfs_search(map_data[:], start, end)
        coor_list = DFS.coor_list[1:]
            
        DFS.update_instructions()

        return [t[::-1] for t in coor_list], DFS.instructions
    
    else:
        bfs_search(map_data[:], start, end)
        coor_list = BFS.coor_list[1:]

        coor_list2 = []
        for coor in BFS.coor_list:
            if coor != (0,0):
                coor_list2.append(coor)

        map_data = read_csv(file_name)
        BFS.update_instructions(map_data[:])

        return [t[::-1] for t in coor_list2[1:]], BFS.instructions



