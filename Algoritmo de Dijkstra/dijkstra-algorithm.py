#File name: dijkstra-algorithm.py
#Author: Luis Carlos <luiscarlos.sf@outlook.com>

import networkx as nx
from filaprioritaria import PriorityQueue

"""
O algoritmo de Dijkstra tem como objetivo encontrar o menor caminho entre quaisquer
dois vérticas do grafo, quando todos os arcos tem comprimento não-negativos.

O algoritmo utiliza um procedimento iterativo, determinando, na iteração 1, o vértice mais
próximo de 1, na segunda iteração, o segundo vértice mais próximo do vértice 1, e assim sucessivamente,
até que em alguma iteração o vértice N seja atingido.
"""
"""
def dijkstra(grafo, vertex_fonte):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                      + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)
"""
