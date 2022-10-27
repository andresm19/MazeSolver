
import os
import csv
import DFS
from searching import *

coor_list = []

# Todas las funciones para buscar el camino correcto
def create_txt_instructions():
    pass

def dfs_search(map_data, start, end):
    DFS.DFS(map_data, start, end)
    print(DFS.coor_list)
    create_txt_instructions()

def bfs_search():
    """
    Procedimiento
    """
    create_txt_instructions()

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

def solve(file_name):
    map_data = read_csv(file_name)
    NUMBER_TILES = len(map_data)
    start = (0, map_data[0].index("c"))
    end = (NUMBER_TILES-1, map_data[NUMBER_TILES-1].index("c"))
    dfs_search(map_data[:], start, end)
    global coor_list
    coor_list = DFS.coor_list[1:]
        
    DFS.update_instructions()

    return [t[::-1] for t in coor_list], DFS.instructions



