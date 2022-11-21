
from searching import *

coor_list = []
instructions = []
stack = Stack()
found = False

def GREEDY(map_data, start, end):
    
    global found, coor_list, stack

    coor_list.append(start)
    stack.push(Node(start))

    if start == end:
        found = True

    map_data[start[0]][start[1]] = "r"

    if not found:
        for av in greedy_sort(availables(start, map_data), end):
            GREEDY(map_data, av, end)
            if found:
                break

        if not found:
            stack.pop()



def greedy_sort(list_avs, end):

    if list_avs == []:
        return []

    l = list_avs

    for i in range(len(l) - 1):
        for j in range(len(l)-1-i):
            if distance(l[j], end) > distance(l[j+1], end):
                aux = l[j]
                list_avs[j] = l[j+1]
                list_avs[j+1] = aux

    return l
            

def update_instructions():
    global instructions
    while stack.head.next != None:
        if stack.head.data == (stack.head.next.data[0] + 1, stack.head.next.data[1]):
            instructions.append("D")
        elif stack.head.data == (stack.head.next.data[0] - 1, stack.head.next.data[1]):
            instructions.append("U")
        elif stack.head.data == (stack.head.next.data[0], stack.head.next.data[1] - 1):
            instructions.append("L")
        elif stack.head.data == (stack.head.next.data[0], stack.head.next.data[1] + 1):
            instructions.append("R")
        
        stack.pop()

    instructions.reverse()