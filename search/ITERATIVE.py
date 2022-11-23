
from search.searching import *

instructions = []
coor_list = []
stack = Stack()
found = False
dep = 0
ending = (0,0)

def ITERATIVE(map_data, start, end, depth):
    global found
    global coor_list
    global stack
    global ending

    ending = end
    coor_list.append(start)
    stack.push(Node(start))
    map_data[start[0]][start[1]] = "r"

    global dep
    dep = depth
    if dep > 0:
        dep -= 1
        for av in availables(start, map_data):
            if found:
                break
            ITERATIVE(map_data, av, end, dep)
        dep = depth
        if start == end:
            found = True
            return
        if not found:
            stack.pop()
    
    


def update_instructions():
    global instructions
    global stack
    global coor_list
    global ending

    if ending != coor_list[-1]:
        return
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

