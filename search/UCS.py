
from search.searching import *

pq = PriorityQueue()
instructions = []
coor_list = []

costs = [1, 1, 4, 5]    # En orden [DOWN, RIGHT, UP, LEFT] (Será mas costoso hacer las acciones LEFT Y UP)

# Insertaremos a la cola prioritaria listas de la siguiente manera: [(c1, c2), cost] donde (c1, c2) es la coordenada

def UCS(map_data, start, end):

    global pq, coor_list, costs

    pq.insert([start, 800])
    coor_list.append(start)
    map_data[start[0]][start[1]] = "r"

    while pq.array[0] != None:
        c = pq.get_max()
        coor_list.append(c[0])
        avs = availables(c[0], map_data, mode='bfs')

        for i in range(len(avs)):
            if avs[i] != (0,0):
                map_data[avs[i][0]][avs[i][1]] = "r"
                pq.insert([avs[i], c[1]-costs[i]])

        maximum = pq.extract_max()[0]
        if maximum == end:
            break

    

def update_instructions(map_data):
    global instructions
    global coor_list

    coor_list2 = coor_list
    coor_list = []

    coor_list.append(coor_list2[-1])
    cur = coor_list2[-1]

    for h in range(len(coor_list2) - 2, -1, -1):
        avs = availables(coor_list2[h], map_data)
        if cur in avs:
            coor_list.append(coor_list2[h])
            cur = coor_list2[h]
    
    coor_list.reverse()

    for i in range(len(coor_list) - 1):
        if coor_list[i+1] == (coor_list[i][0] + 1, coor_list[i][1]):
            instructions.append("D")
        if coor_list[i+1] == (coor_list[i][0] - 1, coor_list[i][1]):
            instructions.append("U")
        if coor_list[i+1] == (coor_list[i][0], coor_list[i][1] + 1):
            instructions.append("R")
        if coor_list[i+1] == (coor_list[i][0], coor_list[i][1] - 1):
            instructions.append("L")
                

