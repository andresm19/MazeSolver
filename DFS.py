
from searching import *

instructions = []
coor_list = []
stack = Stack()
found = False

def DFS(map_data, start, end):
    global found
    global coor_list
    global stack
    
    coor_list.append(start)
    stack.push(Node(start))
    map_data[start[0]][start[1]] = "r"
    if start != end and not found:
        for av in availables(start, map_data):
            if found:
                break
            DFS(map_data, av, end)
        if not found:
            stack.pop()
    else:
        found = True


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
