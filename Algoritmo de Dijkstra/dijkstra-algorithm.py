#File name: dijkstra-algorithm.py
#Author: Luis Carlos <luiscarlos.sf@outlook.com>

import networkx as nx
from filaprioritaria import PriorityQueue
import sys

"""
O algoritmo de Dijkstra tem como objetivo encontrar o menor caminho entre quaisquer
dois vérticas do grafo, quando todos os arcos tem comprimento não-negativos.

O algoritmo utiliza um procedimento iterativo, determinando, na iteração 1, o vértice mais
próximo de 1, na segunda iteração, o segundo vértice mais próximo do vértice 1, e assim sucessivamente,
até que em alguma iteração o vértice N seja atingido.
"""

def dijkstra(grafo, fonte):
    #Passo 1
    """
    dist = list()
    dist.append((0,fonte))
    for node in grafo:
        if not(node == fonte):
            dist.append((sys.maxsize, node))
    """
    dist = list()
    for node in grafo:
        grafo.nodes[node]['distance']=sys.maxsize
    grafo.nodes[fonte]['distance']= 0
    dist.append(( grafo.nodes[fonte]['distance'], fonte))
    #Passo 2
    q = PriorityQueue()

    #for node in list(grafo):
    lista=[(grafo.nodes[node]['distance'], node) for node in list(grafo)]
        #q.insert((grafo.nodes[node]['distance'], node)) #({'distance': value}, node)
        #print("haha", node, "Tamanho \n", q.getTamanho() )

    q.build_min_heap(lista)

    while q.getTamanho()!=0:
        #Passo 2.1
        u = q.remove_min()
        a=u[1]
        
        dist.append(u)
        for v in list(grafo.successors(a)):
            #if not v in dist:
                novo_custo = grafo.nodes[a]['distance']+grafo.edges[a, v]['weight']
                print(novo_custo)
                if novo_custo < grafo.nodes[v]['distance']:
                    grafo.nodes[v]['distance'] = novo_custo
                    print((grafo.nodes[v]['distance'], v))
                    q.increase_key(v, novo_custo)
    return dist

class Teste():

    def main(self):
        grafo = nx.DiGraph()
        grafo.add_nodes_from(range(1, 10))
        grafo.add_edges_from([(1,2,{'weight':11}),(1,3,{'weight':9}),(2,4,{'weight':17}),\
                            (2,5,{'weight':8}), (3,4,{'weight':8}), (3,5,{'weight':6}), \
                            (4,6,{'weight':6}),(4,7,{'weight':5}), (5,7,{'weight':6}),\
                            (5,8,{'weight':4}), (6,9,{'weight':6}),(7,9,{'weight':4}), (8,9,{'weight':6})])

        print("Nodes\n", grafo.nodes())
        print("Edges\n", grafo.edges(data=True))

        fonte = input("Digite o vértice fonte: ")
        try:
            fonte = int(fonte)
        except():
            pass

        if fonte in grafo:
            print(fonte)
            custos = dijkstra(grafo, fonte)
            print("Distâncias do ",fonte,"para todos os outros vértices:\n",custos)
        else:
            print("Não existe nenhum vértice com essa definição")


if __name__=="__main__":
    Teste().main()

