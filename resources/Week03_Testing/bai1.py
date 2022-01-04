import os
import random

def generateRandomNumber(LowerBound, UpperBound, Type):
    if Type == int:
        return random.randint(LowerBound, UpperBound)
    elif Type == float:
        return random.uniform(LowerBound, UpperBound)
    else:
        raise Exception("Invalid type of number: " + str(Type))
    
def generateRandomArray(LowerBound, UpperBound, Length, Type):
    return [generateRandomNumber(LowerBound, UpperBound, Type) for i in range(Length)]

def generateRandomString(Length):
    return ''.join([chr(generateRandomNumber(0, 25, int) + 97) for i in range(Length)])

def generateUnweightedTree(NodeAmount):
    # Idea: Generate a fully-connected weighted graph, and then, find a MST on that graph, remove the weight.
    # A bit weirdo, but fun actually :)

    if (NodeAmount < 1):
        raise ValueError("NodeAmount must not be less than 1")
    
    EdgeList = []
    Parent = [i for i in range(NodeAmount)]
    TreeEdge = []

    def Root(u):
        if (Parent[u] != u):
            Parent[u] = Root(Parent[u])
        return Parent[u]
    
    for i in range(NodeAmount):
        for j in range(i + 1, NodeAmount):
            EdgeList.append((i, j, generateRandomNumber(1, NodeAmount * 10, int)))
    EdgeList = sorted(EdgeList, key=lambda tuple: tuple[2]) # Sorted by the third element of tuple

    for Edge in EdgeList:
        u, v, EdgeWeight = Edge
        if (Root(u) != Root(v)):
            TreeEdge.append((u + 1, v + 1)) # Current u and v are in 0-index, must add 1
            if (u < v):
                u, v = v, u
            Parent[Root(u)] = Parent[Root(v)]
    
    return TreeEdge

def generateUnweightedAndDirectedGraph(NodeAmount):
    if (NodeAmount < 1):
        raise ValueError("NodeAmount must not be less than 1")
    
    n = generateRandomNumber(1, 10000, int)
    m = generateRandomNumber(1, 10000, int)

    print(n, m)

    EdgeList = []

    for i in range(m):
        while True:
            u = generateRandomNumber(1, n, int)
            v = generateRandomNumber(1, n, int)

            if ((u, v) not in EdgeList and (v, u) not in EdgeList):
                EdgeList.append((u, v))
                break
    
    return EdgeList

print("Random int:", generateRandomNumber(0, 100, int))
print("Random float:", generateRandomNumber(0, 100, float))
print("Random string:", generateRandomString(100))
print("Random unweighted tree:", generateUnweightedTree(100))
print("Random unweighted and directed graph:", generateUnweightedAndDirectedGraph(100))


