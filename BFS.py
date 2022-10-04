from collections import deque

stack_nodes = deque()
lista = [['w', 'w', 'w', 'c', 'w', 'w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'], ['w', 'w', 'c', 'c', 'w', 'w', 'c', 'w', 'c', 'w'], ['w', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'c', 'w'], ['w', 'c', 'w', 'w', 'c', 'c', 'c', 'w', 'w', 'w'], 
['w', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'w', 'w'], ['w', 'c', 'w', 'c', 'w', 'w', 'w', 'c', 'c', 'w'], ['w', 'c', 'w', 'c', 'w', 'w', 'c', 'c', 'w', 'w'], ['w', 'c', 'w', 'c', 'c', 'w', 'w', 'c', 'c', 'w'], ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w']]

#lista = [[]]

for row, tiles in enumerate(lista):
    for col, tile in enumerate(tiles):
        if tile == 'c':
            stack_nodes.append((row, col))
        if row == 0 and tile == 'c':
            inicio = (row, col)
        
        if row == 9 and tile == 'c':
            final = (row, col)
def up(current):
    stack_nodes.append((current[0], current[1]+1))

    

print(inicio)
print(final)
print(stack_nodes)

class Node():
    def __init__(self, x, y):
        self.next = None
        self.prev = None
        self.x = x
        self.y = y
        self.visitado = False


start = Node(inicio[0], inicio[1])
end = Node(final[0], final[1])

disponibles = list(stack_nodes)

def opciones(nodo):
    disp = list()
    if (nodo.x + 1, nodo.y) in disponibles:
        disp.append(Node(nodo.x + 1, nodo.y))
    if (nodo.x, nodo.y + 1) in disponibles:
        disp.append(Node(nodo.x, nodo.y + 1))
    if (nodo.x - 1, nodo.y) in disponibles:
        disp.append(Node(nodo.x - 1, nodo.y))
    if (nodo.x, nodo.y - 1) in disponibles:
        disp.append(Node(nodo.x, nodo.y - 1))


def dfs(inicio : Node, fin : Node):
    
    stack_nodes.append(inicio)
    if (inicio.x, inicio.y) == fin:
        print("Encontrado")
        return 
    
    for c in opciones(inicio):
        if c.visitado == False:
            c.prev = inicio
            dfs(csv_data, c, fin)

    inicio.visitado =  True
    stack_nodes.pop()
    disponibles.remove((inicio.x, inicio.y))


dfs(start, end)

