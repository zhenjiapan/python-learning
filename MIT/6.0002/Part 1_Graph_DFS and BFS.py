class Node:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + ' -> ' + self.dest.getName()

class Digraph:
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        self.edges[node] = []

    def addEdge(self, edge):
        src, dest = edge.getSource(), edge.getDestination()
        if src not in self.edges or dest not in self.edges:
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for node in self.edges:
            if node.getName() == name:
                return node
        raise NameError(name + ' not found')

class Graph(Digraph):
    def addEdge(self, edge):
        super().addEdge(edge)
        reverseEdge = Edge(edge.getDestination(), edge.getSource())
        super().addEdge(reverseEdge)

def buildCityGraph(graphType = Digraph):
    g = graphType()
    names = ('Boston', 'Providence', 'New York', 'Chicago',
             'Denver', 'Phoenix', 'Los Angeles')
    for name in names:
        g.addNode(Node(name))

    connections = (
        ('Boston', 'Providence'),
        ('Boston', 'New York'),
        ('Providence', 'Boston'),
        ('Providence', 'New York'),
        ('New York', 'Chicago'),
        ('Chicago', 'Denver'),
        ('Chicago', 'Phoenix'),
        ('Denver', 'Phoenix'),
        ('Denver', 'New York'),
        ('Los Angeles', 'Boston')
    )
    for source, destination in connections:
        g.addEdge(Edge(g.getNode(source), g.getNode(destination)))
    return g

def printPath(path):
    return ' -> '.join(str(node) for node in path)

# DFS Method
def DFS(graph, start, end, path = [], shortest = None, toPrint = False):
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))

    if start == end:
        return path

    for node in graph.childrenOf(start):
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath is not None:
                    shortest = newPath
        elif toPrint:
            print('Already visited:', node)

    return shortest

from collections import deque

# BFS Method: Path Queue
def BFS_pathQueue(graph, start, end, toPrint = False):
    pathQueue = deque([[start]])

    while len(pathQueue) > 0: # while pathQueue:
        tmpPath = pathQueue.popleft()

        if toPrint:
            print('Current BFS path:', printPath(tmpPath))

        lastNode = tmpPath[-1]

        if lastNode == end:
            return tmpPath

        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                pathQueue.append(tmpPath + [nextNode])

    return None

# BFS: Node Queue
def BFS_nodeQueue(graph, start, end, toPrint = False):
    nodeQueue = deque([start])
    parent = {start: None}

    while len(nodeQueue) > 0:
        current = nodeQueue.popleft()
        if current == end:
            result = []
            while current is not None:
                result.append(current)
                current = parent[current]
            return result[::-1]

        for nextNode in graph.childrenOf(current):
            if nextNode not in parent:
                parent[nextNode] = current
                nodeQueue.append(nextNode)

    return None

cityGraph = buildCityGraph()
print(printPath(DFS(cityGraph, cityGraph.getNode('Los Angeles'), cityGraph.getNode('Denver'))))
print(printPath(BFS_pathQueue(cityGraph, cityGraph.getNode('Los Angeles'), cityGraph.getNode('Denver'))))
print(printPath(BFS_nodeQueue(cityGraph, cityGraph.getNode('Los Angeles'), cityGraph.getNode('Denver'))))
