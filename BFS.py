from searching import *

instructions = []
coor_list = []
queue = Queue()
found = False
n_buscados = []

def BFS(map_data, start, end):
    global coor_list
    global found
    global queue
    coor_list.append(start)
    queue.enqueue(Node(start))
    map_data[start[0]][start[1]] = "r"
    global n_buscados
    while not queue.empty() and not found:
        k = 0
        for av in availables(queue.head.data, map_data, mode='bfs'):
            if av == end:
                found = True
            map_data[av[0]][av[1]] = "r"
            coor_list.append(av)
            if av != (0,0):
                queue.enqueue(Node(av))
                k += 1

        n_buscados.append(k)
        queue.dequeue()


def update_instructions(map_data):
    global instructions
    global coor_list

    coor_list2 = []
    for coor in coor_list:
        if coor != (0,0):
            coor_list2.append(coor)

    coor_list = []
    coor_list.append(coor_list2[-1])
    cur = coor_list2[-1]

    for h in range(coor_list2.index(cur) - 1, -1, -1):
        avs = availables(coor_list2[h], map_data, mode='bfs')
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
