import networkx as nx
parent = dict()
rank = dict()

def criar_conjunto(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def procurar(vertice):
    v = vertice
    while parent[vertice] != vertice:
        vertice = parent[vertice]
    parent[v] = parent[vertice]
    return parent[vertice]

def find2(vertice):
    if parent[vertice] != vertice:
        print("vertice = " + vertice)
        print(parent)
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def uniao(vertice1, vertice2):
    raiz1 = procurar(vertice1)
    raiz2 = procurar(vertice2)
    if raiz1 != raiz2:
        if rank[raiz1] > rank[raiz2]:
            parent[raiz2] = raiz1
        else:
            parent[raiz1] = raiz2
            if rank[raiz1] == rank[raiz2]: rank[raiz2] += 1

def kruskal(grafo):
    #cria um dicionário com todos os vertices do grafo
    lista_de_vertice = list(grafo.nodes())
    for vertice in lista_de_vertice:
        criar_conjunto(vertice)
    #cria a arvore geradora minima
    mst = nx.Graph()
    arestas = list(grafo.edges.data('weight'))
    arestas.sort(key = lambda x: x[2])
    for aresta in arestas:
        vertice1, vertice2, weight = aresta
        if procurar(vertice1) != procurar(vertice2):
            uniao(vertice1, vertice2)
            mst.add_edge(aresta[0], aresta[1], weigth = aresta[2])
    return mst






#####################################################


graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }
minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
grafo = nx.Graph()
grafo.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
grafo.add_edges_from([
                            ('A', 'B', {'weight': 1}), 
                            ('A', 'C', {'weight': 5}), 
                            ('A', 'D', {'weight': 3}),
                            ('B', 'C', {'weight': 4}),  
                            ('B', 'D', {'weight': 2}), 
                            ('C', 'D', {'weight': 1}), 
                            ])
arvore_minima = nx.Graph()
arvore_minima.add_nodes_from((['A', 'B', 'C', 'D']))
arvore_minima.add_edges_from([
                            ('A', 'B', {'weight': 1}), 
                            ('B', 'D', {'weight': 2}), 
                            ('C', 'D', {'weight': 1}),
                            ])
#assert kruskal(grafo) == arvore_minima
print(kruskal(grafo).edges())
print(arvore_minima.edges())