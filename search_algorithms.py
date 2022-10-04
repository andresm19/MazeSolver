
import os
import csv

# Todas las funciones para buscar el camino correcto

def read_csv():
    map_data = []
    with open(os.path.join(os.path.dirname(__file__), 'maze_5x5.csv'), 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    map_data.append(row)
    print(map_data)
    

def create_txt_search():
    pass

def create_txt_instructions():
    pass

def dfs_search():
    read_csv()
    """
    Procedimiento
    """
    create_txt_instructions()

def bfs_search():
    read_csv()
    """
    Procedimiento
    """
    create_txt_instructions()

def iter_deep_search():
    read_csv()
    """
    Procedimiento
    """
    create_txt_instructions()

def uniform_cost_search():
    read_csv()
    """
    Procedimiento
    """
    create_txt_instructions()

def greedy_search():
    read_csv()
    """
    Procedimiento
    """
    create_txt_instructions()

def a_star_search():
    read_csv()
    """
    Procedimiento
    """
    create_txt_instructions()


coor_list = [(1, 1), (1, 2), (1, 3), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4)]
read_csv()

coor_list2 = [(3,1), (4, 1), (3, 2), (5, 1), (2, 2), (6, 1), (2, 3), (3, 2), (7, 1), (1, 3),
              (6, 2), (1, 4), (8, 1), (1, 5), (8, 2), (2, 5), (1, 6), (8, 3), (3, 5), (1, 7),
              (4, 5), (6, 3), (1, 8), (4, 4), (3, 6), (6, 4), (5, 4), (3, 7), (6, 5), (3, 8), (7, 5),
              (4, 8), (7, 6), (8, 6), (7, 7), (7, 8), (6, 7), (8, 8), (8, 9)]

